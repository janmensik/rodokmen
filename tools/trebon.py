#!/usr/bin/env python3
"""Matriky SOA Třeboň (digi.ceskearchivy.cz) bez prohlížeče.

Použití (z kořene projektu):
  trebon.py misto "Obec"                 -> id místa a jeho název
  trebon.py svazky <id_mista|"Obec">     -> seznam matrik: id_knihy | kniha | druh | roky | obce
  trebon.py rejstrik <id_knihy> <písmeno> -> jmenný rejstřík
  trebon.py snimek <id_knihy> <snímek> <vystup.jpg> [nahled]
                                         -> stáhne snímek v plném rozlišení (nebo nahled)
  trebon.py svazek <id_knihy>            -> zapíše svazek do data/svazky.json (klíč trebon_<id_knihy>)
Trvalý odkaz na snímek: https://digi.ceskearchivy.cz/<id_knihy>/<snímek>
"""
import html, http.cookiejar, json, math, os, re, subprocess, sys, tempfile, unicodedata, urllib.parse, urllib.request

BASE = "https://digi.ceskearchivy.cz"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_cj = http.cookiejar.CookieJar()
_op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(_cj))
_op.addheaders = [
    ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"),
    ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"),
    ("Accept-Language", "cs,en-US;q=0.7,en;q=0.3"),
]


def get(path, referer=None, binary=False):
    url = path if path.startswith("http") else BASE + path
    req = urllib.request.Request(url)
    if referer:
        req.add_header("Referer", referer)
    for attempt in range(4):
        try:
            with _op.open(req, timeout=90) as r:
                data = r.read()
                return (data, r.geturl()) if binary else (data.decode("utf-8", "replace"), r.geturl())
        except OSError:
            if attempt == 3:
                raise


def text(s):
    return html.unescape(re.sub(r"<[^>]+>", " ", s)).replace("\xa0", " ").strip()


def misto(nazev):
    ascii_nazev = unicodedata.normalize("NFKD", nazev).encode("ascii", "ignore").decode()
    _, url = get("/" + urllib.parse.quote(ascii_nazev))
    m = re.search(r"[?&]id=(\d+)", url) or re.search(r"/(\d+)-", url)
    if not m:
        sys.exit(f"místo „{nazev}“ nenalezeno")
    pid = m.group(1)
    page, _ = get(f"/pages/klicova/rejinfo.php?typ=&id={pid}&l=&bookid=")
    t = re.search(r"document\.title=\"([^\"]*)\"", page)
    if not t:
        page, _ = get(f"/description.php?id={pid}&menu=4")
        t = re.search(r"document\.title=\"([^\"]*)\"", page)
    return pid, (t.group(1).strip() if t else "")


def svazky(arg):
    pid = arg if arg.isdigit() else misto(arg)[0]
    page, _ = get(f"/pages/klicova/klicmaterial1.php?typ=2&id={pid}&pomid={pid}&l=&bookid=")
    out = []
    for m in re.finditer(r"<tr[^>]*onclick=\"otevri\('menu=3&id=(\d+)'\)\">(.*?)</tr>", page, re.S):
        bid, row = m.group(1), m.group(2)
        cells = [text(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)]
        cells = [re.sub(r"\s+", " ", c) for c in cells]
        out.append((bid, cells))
    return out


def rejstrik(bid, pis):
    page, _ = get(f"/pages/indexes.php?druh=1&menu2=0&pis={urllib.parse.quote(pis)}&id={bid}&page=")
    rows = []
    for m in re.finditer(r"<tr id='\d+' onclick=\"otevri2\('[^']*page=(\d+)[^']*'\)\">(.*?)</tr>", page, re.S):
        cells = [text(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", m.group(2), re.S)]
        rows.append(cells + [m.group(1)])
    return rows


def extrahuj_token(html_str):
    # Moderní DigiArchiv (obfuscované konstanty)
    m_call = re.search(r'Z\.showImage\("myContainer",\s*([^,\{]+)', html_str)
    if m_call:
        parts_expr = m_call.group(1)
        var_names = re.findall(r'(_[a-zA-Z0-9]+)', parts_expr)
        if var_names:
            vars_dict = {}
            for m in re.finditer(r'(?:const|var)\s+(_[a-zA-Z0-9]+)\s*=\s*["\']([^"\']+)["\']', html_str):
                vars_dict[m.group(1)] = m.group(2).replace('\\/', '/')
            token = "".join(vars_dict.get(v, "") for v in var_names)
            if token:
                return token
    # Starší verze s přímým řetězcem
    m_old = re.search(r'showImage\("[^"]*","([^"]+)"', html_str)
    if m_old:
        return m_old.group(1)
    return None


def snimek(bid, n, out, nahled=False):
    ref_container = f"{BASE}/{bid}/{n}"
    get(ref_container)
    ref_view = f"{BASE}/view.php?menu=3&id={bid}&page={n}&r=0"
    page, _ = get(ref_view, referer=ref_container)
    token = extrahuj_token(page)
    if not token:
        sys.exit("token obrázku nenalezen (snímek neexistuje?)")
    
    # Zjisti vlastnosti obrázku
    desc_url = f"{BASE}/cgi-bin/i_M6Izlkmw?{token}.0.desc"
    desc_xml, _ = get(desc_url, referer=ref_view)
    m_dim = re.search(r'WIDTH="(\d+)"\s+HEIGHT="(\d+)".*?TILESIZE="(\d+)"', desc_xml)
    if not m_dim:
        sys.exit(f"chyba čtení rozměrů ze serveru: {desc_xml[:100]}")
    W, H, T = int(m_dim.group(1)), int(m_dim.group(2)), int(m_dim.group(3))

    # Zoomify vrstvy
    dims, w, h = [], W, H
    while True:
        dims.append((w, h))
        if w <= T and h <= T:
            break
        w, h = (w + 1) // 2, (h + 1) // 2
    dims = dims[::-1]
    counts = [math.ceil(a / T) * math.ceil(b / T) for a, b in dims]

    # Zvolení úrovně rozlišení
    L = max(0, len(dims) - 3) if nahled else len(dims) - 1
    w_target, h_target = dims[L]
    nx, ny = math.ceil(w_target / T), math.ceil(h_target / T)
    start = sum(counts[:L])

    d = tempfile.mkdtemp(prefix="trebon_")
    files = []
    try:
        for y in range(ny):
            for x in range(nx):
                g = (start + y * nx + x) // 256
                tile_url = f"{BASE}/cgi-bin/i_M6Izlkmw?{token}.{g}.{L}-{x}-{y}"
                tile_data, _ = get(tile_url, referer=ref_view, binary=True)
                p = os.path.join(d, f"{y:03d}_{x:03d}.jpg")
                with open(p, "wb") as f:
                    f.write(tile_data)
                files.append(p)

        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        tmp = os.path.abspath(out) + ".tmp.jpg"
        subprocess.run(["magick", "montage", *[os.path.basename(f) for f in files],
                        "-tile", f"{nx}x{ny}", "-geometry", "+0+0",
                        "-gravity", "NorthWest", "-background", "white", tmp], check=True, cwd=d)
        subprocess.run(["magick", tmp, "-crop", f"{w_target}x{h_target}+0+0", "+repage", "-quality", "88", out], check=True)
        if os.path.exists(tmp):
            os.remove(tmp)
    finally:
        for f in files:
            if os.path.exists(f):
                os.remove(f)
        if os.path.exists(d):
            os.rmdir(d)

    r = subprocess.run(["magick", "identify", "-format", "%wx%h", out], capture_output=True, text=True)
    print(out, r.stdout.strip(), "odkaz:", ref_container)


def svazek(bid):
    page, _ = get(f"/{bid}/1")
    t = re.search(r"document\.title=\"([^\"]*)\"", page) or re.search(r"<title>([^<]*)", page)
    nazev = t.group(1).strip() if t else f"kniha {bid}"
    if "DigiArchiv" in nazev:
        nazev = f"kniha {bid} (název doplň ručně)"
    path = os.path.join(ROOT, "data", "svazky.json")
    d = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    d[f"trebon_{bid}"] = {"archiv": "SOA Třeboň – Sbírka matrik", "portal": "digi.ceskearchivy.cz",
                          "svazek": nazev, "popis": "", "url": f"{BASE}/{bid}"}
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"trebon_{bid} -> {nazev}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    cmd = a[0]
    if cmd == "misto":
        print(*misto(a[1]))
    elif cmd == "svazky":
        for bid, c in svazky(a[1]):
            print(bid, "|", " | ".join(c))
    elif cmd == "rejstrik":
        for r in rejstrik(a[1], a[2]):
            print(" | ".join(r))
    elif cmd == "snimek":
        snimek(a[1], a[2], a[3], nahled=("nahled" in a[4:]))
    elif cmd == "svazek":
        svazek(a[1])
    else:
        sys.exit(__doc__)
