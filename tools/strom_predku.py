#!/usr/bin/env python3
"""Strom předků jedné osoby jako plakát k tisku (SVG + PDF + PNG náhled).

Použití:  strom_predku.py <kekulé číslo> [výstupní složka] [--papir A2|A1|A3] [--venovani "text"]
          [--popisy soubor.json]

Příklad:  python -I -X utf8 tools/strom_predku.py 7 vystupy --venovani "Pro Evu"

Osoba s číslem k je kořen stromu (dole), její předci rostou nahoru: otec vlevo, matka vpravo.
Bere jen to, co je v data/osoby.py; odhadnuté rozsahy („asi 1880–1885“) vynechá, protože nejsou doložené.
Volitelný JSON s krátkými popisy:  {"zam": {"14": "primář …"}, "misto": {"28": "…"}, "vetve": {"60": ["Černí", "kováři…"]}}
"""
import html, json, os, re, shutil, subprocess, sys, tempfile, datetime

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
sys.path.insert(0, TOOLS)
import fakta  # noqa: E402
import site
_usp = site.getusersitepackages()
if os.path.exists(_usp) and _usp not in sys.path:
    sys.path.append(_usp)

args = [a for a in sys.argv[1:]]


def opt(name, default=None):
    if name in args:
        i = args.index(name)
        v = args[i + 1]
        del args[i:i + 2]
        return v
    return default


PAPIR = opt("--papir", "A2").upper()
VENOVANI = opt("--venovani", "")
POPISY = opt("--popisy", None)
QR_URL = opt("--url", "https://rodokmen.mensik.cz")
if not args:
    sys.exit(__doc__)
ROOTK = int(args[0])
OUT = os.path.abspath(args[1]) if len(args) > 1 else os.path.join(ROOT, "vystupy")
os.makedirs(OUT, exist_ok=True)

ns = {}
exec(open(os.path.join(ROOT, "data", "osoby.py"), encoding="utf-8").read(), ns)
P = ns["P"]
CUSTOM = json.load(open(POPISY, encoding="utf-8")) if POPISY else {}

# ---------------------------------------------------------------- měření textu
try:
    from PIL import ImageFont
    _FONTS = {}

    def _font(style):
        if style not in _FONTS:
            name = {"r": "georgia.ttf", "b": "georgiab.ttf", "i": "georgiai.ttf"}[style]
            for d in ("C:/Windows/Fonts", "/Library/Fonts", "/System/Library/Fonts/Supplemental",
                      "/usr/share/fonts/truetype/msttcorefonts"):
                p = os.path.join(d, name)
                if os.path.exists(p):
                    _FONTS[style] = ImageFont.truetype(p, 100)
                    break
            else:
                _FONTS[style] = None
        return _FONTS[style]

    def text_w(t, size, style="r"):
        f = _font(style)
        if f is None:
            return len(t) * size * (0.58 if style == "b" else 0.52)
        return f.getlength(t) * size / 100
except ImportError:  # bez Pillow – hrubý odhad
    def text_w(t, size, style="r"):
        return len(t) * size * (0.58 if style == "b" else 0.52)


def wrap(text, size, width, style="r", max_lines=3):
    # nezalomitelné mezery: „čp. 22“, „21. 1. 1856“
    text = re.sub(r"\b(čp\.|č\.) (?=\d)", "\\1\u00a0", text)
    text = re.sub(r"(\d{1,2}\.) (?=\d)", "\\1\u00a0", text)
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if text_w(t, size, style) <= width or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while last and text_w(last + "…", size, style) > width:
            last = last[:-1]
        lines[-1] = last.rstrip(" ,") + "…"
    return lines


# ---------------------------------------------------------------- údaje osoby
def gen(k):
    return k.bit_length() - ROOTK.bit_length()


def strip_paren(s):
    return re.sub(r"\s*\([^)]*\)", "", s).strip(" ,")


def estimated(date):
    """„asi 1880–1885“ = odhad z věku dětí, ne doklad → nezobrazovat."""
    return bool(re.search(r"\d{4}\s*[–-]\s*\d{4}", date))


def event(fact):
    date, place = fakta.split_event(fact)
    if estimated(date):
        return ""
    date = re.sub(r"^cca\b", "asi", date)
    return " ".join(x for x in (date, strip_paren(place)) if x)


def short_job(k, p):
    c = CUSTOM.get("zam", {}).get(str(k))
    if c is not None:
        return c
    z = strip_paren(p.get("zam", ""))
    z = z.split(";")[0]
    parts = []
    for part in z.split(", "):
        part = re.sub(r"\s+(v|ve|na|u)\s+[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ].*$", "", part).strip()
        part = re.sub(r"\s+čp\..*$", "", part)
        if part:
            parts.append(part)
    return ", ".join(parts)


def place_line(k, p):
    c = CUSTOM.get("misto", {}).get(str(k))
    if c is not None:
        return c
    puvod = strip_paren(p.get("puvod", ""))
    bydl = strip_paren(p.get("bydl", "").split(";")[0].split(",")[0])
    if puvod and not bydl.startswith(puvod):
        return puvod
    return bydl or puvod


def qr_svg(url, x, y, size, fill="#2E241C"):
    try:
        import qrcode
        qr = qrcode.QRCode(border=0)
        qr.add_data(url)
        qr.make(fit=True)
        matrix = qr.get_matrix()
        n = len(matrix)
        s = size / n
        parts = []
        for r in range(n):
            for c in range(n):
                if matrix[r][c]:
                    rx = x + c * s
                    ry = y + r * s
                    parts.append(f"M{rx:.2f},{ry:.2f}h{s:.2f}v{s:.2f}h{-s:.2f}z")
        return f'<path d="{"".join(parts)}" fill="{fill}"/>'
    except Exception as e:
        print(f"QR kód nelze vytvořit: {e}", file=sys.stderr)
        return ""


def person(k):
    p = P[k]
    birth = death = ""
    for f in p.get("f", []):
        f = f.strip()
        if f.startswith("*") and not birth:
            birth = event(f[1:])
        elif f.startswith("†") and not death:
            death = event(f[1:])
    d = dict(k=k, name=p["n"], roz=p.get("roz", ""), job=short_job(k, p),
             birth=("* " + birth) if birth else "", death=("† " + death) if death else "")
    # místo, jen když není vidět z narození ani úmrtí
    has_place = bool((birth and fakta.split_event(birth)[1]) or (death and fakta.split_event(death)[1]))
    d["place"] = "" if has_place else place_line(k, p)
    return d


def marriage(fk, mk):
    """Datum a místo sňatku rodičů (z faktů otce, jinak matky), bez jména manželky."""
    for k, other in ((fk, mk), (mk, fk)):
        if k not in P:
            continue
        for f in P[k].get("f", []):
            f = f.strip()
            if not f.startswith("×"):
                continue
            date, rest = fakta.split_event(re.sub(r"^×\s*(\d\.\s*)?", "", f))
            if not date or estimated(date):
                continue
            if other in P:  # useknout jméno manžela/manželky
                o = P[other]
                names = [w for w in o["n"].split() if not w.endswith(".")]
                for cand in names[:1] + [o.get("roz", "")]:
                    if cand and cand in rest:
                        rest = rest[:rest.index(cand)]
                        break
            return ("⚭ " + date + " " + strip_paren(rest)).strip()
    return ""


# ---------------------------------------------------------------- rozložení
PAGES = {"A3": (420, 297), "A2": (594, 420), "A1": (841, 594)}
W, H = PAGES.get(PAPIR, PAGES["A2"])
S = W / 594  # měřítko vůči A2 (všechny rozměry níže jsou pro A2)

MARGIN = 16 * S
LABELW = 30 * S
FRAME = 7 * S

anc = {}  # k -> generace


def collect(k):
    if k in P:
        anc[k] = gen(k)
        collect(2 * k)
        collect(2 * k + 1)


collect(ROOTK)
NGEN = max(anc.values()) + 1


def parents(k):
    return [c for c in (2 * k, 2 * k + 1) if c in anc]


def units(k):
    ps = parents(k)
    if not ps:
        return 1.7 if anc[k] <= 3 else 1.0
    return sum(units(c) for c in ps)


TOTAL_U = units(ROOTK)
UNIT = (W - 2 * MARGIN - LABELW) / TOTAL_U
X0 = MARGIN + LABELW
xs = {}


def place(k, left):
    ps = parents(k)
    if not ps:
        xs[k] = left + units(k) * UNIT / 2
        return
    x = left
    for c in ps:
        place(c, x)
        x += units(c) * UNIT
    xs[k] = sum(xs[c] for c in ps) / len(ps)


place(ROOTK, X0)

# barvy větví – podle předka ve 3. generaci (praprarodiče), u kratších větví podle nejvyššího předka nad nimi
PALETTE = ["#4F6D8F", "#8E3B3B", "#5E7A3A", "#B0782A", "#7A4E7E", "#3E7F86", "#9A5B3C", "#6B6B9A"]
NEUTRAL = "#5B4636"


def branch_key(k):
    g = anc[k]
    if g >= 3:
        return k >> (g - 3)
    # osoba v nižší generaci: patří do větve, jen když nad ní nic dalšího není (např. 28/29 bez rodičů)
    sub = [c for c in anc if anc[c] > g and (c >> (anc[c] - g)) == k]
    if not sub and g >= 2:
        return k >> (g - 1)
    return None


branches = []
for k in sorted(anc, key=lambda k: xs[k]):
    b = branch_key(k)
    if b is not None and b not in branches:
        branches.append(b)
COLOR = {b: PALETTE[i % len(PALETTE)] for i, b in enumerate(branches)}


def color(k):
    b = branch_key(k)
    return COLOR.get(b, NEUTRAL)


# velikosti podle generace (mm na A2)
NAME = {0: 7.0, 1: 4.7, 2: 4.2, 3: 4.0, 4: 3.5, 5: 2.7, 6: 2.5}
MAXW = {0: 120, 1: 96, 2: 74, 3: 66, 4: 60}


def name_size(g):
    return NAME.get(g, 2.7) * S


def body_size(g):
    if g == 0:
        return 3.4 * S
    if g >= 5:
        return 2.15 * S
    if g == 4:
        return 2.45 * S
    return max(2.6 * S, name_size(g) * 0.7)


rows = {}
for k, g in anc.items():
    rows.setdefault(g, []).append(k)
for g in rows:
    rows[g].sort(key=lambda k: xs[k])

cards = {}
for g, ks in rows.items():
    for i, k in enumerate(ks):
        room = []
        if i > 0:
            room.append(xs[k] - xs[ks[i - 1]])
        if i < len(ks) - 1:
            room.append(xs[ks[i + 1]] - xs[k])
        avail = min(room) - (1.6 * S if g >= 5 else 2.2 * S) if room else 10 ** 6
        avail = min(avail, 2 * (xs[k] - X0 + 1.5 * S), 2 * (W - MARGIN - xs[k]))
        w = min(MAXW.get(g, 52) * S, avail)
        d = person(k)
        ns_, bs = name_size(g), body_size(g)
        pad = 1.5 * S if g >= 5 else (2.2 * S if g == 4 else 3.2 * S)
        inner = w - 2 * pad
        lines = []  # (text, size, style, color, gap_before)
        for t in wrap(d["name"], ns_, inner, "b", 3 if g >= 4 else 2):
            lines.append((t, ns_, "b", "#2E241C", 0))
        if d["roz"]:
            lines.append(("roz. " + d["roz"], bs * 1.02, "i", "#5A4A3E", 0))
        first = True
        for key in ("birth", "death"):
            if d[key]:
                for t in wrap(d[key], bs, inner, "r", 3 if g >= 5 else 2):
                    lines.append((t, bs, "r", "#3D3229", 1.2 * S if first else 0))
                    first = False
        if d["place"]:
            for t in wrap(d["place"], bs, inner, "r", 2):
                lines.append((t, bs, "r", "#3D3229", 1.2 * S if first else 0))
                first = False
        if d["job"]:
            for i2, t in enumerate(wrap(d["job"], bs, inner, "i", 3)):
                lines.append((t, bs, "i", color(k), 1.2 * S if i2 == 0 else 0))
        h = pad + 1.6 * S + sum(sz * 1.22 + gap for _, sz, _, _, gap in lines) + pad * 0.7
        cards[k] = dict(w=w, h=h, lines=lines, g=g)

# svislé rozvržení
HEADER = 62 * S if VENOVANI else 54 * S
row_h = {g: max(cards[k]["h"] for k in rows[g]) for g in rows}

# legenda větví (rody)
items = []
for b in branches:
    c = CUSTOM.get("vetve", {}).get(str(b))
    if c:
        title, desc = c
    else:  # automaticky: příjmení předka větve a místo
        p = P[b]
        title, desc = (p.get("roz") or p["n"].split()[-1]), place_line(b, p)
    items.append((COLOR[b], title, desc))


def layout(legend_h):
    gap = 13 * S
    avail_h = H - HEADER - legend_h - 2 * FRAME
    need = sum(row_h.values()) + gap * (NGEN - 1)
    if need < avail_h:
        gap = min(gap + (avail_h - need) / max(1, NGEN - 1), 17.5 * S)
    need = sum(row_h.values()) + gap * (NGEN - 1)
    ry, y = {}, HEADER + FRAME + max(0, (avail_h - need) / 2)
    for g in range(NGEN - 1, -1, -1):
        ry[g] = y
        y += row_h.get(g, 0) + gap
    return gap, ry, need > avail_h


# legenda vlevo nahoře, když je tam volno (typicky nad kratší otcovskou větví), jinak dole
LEG_ITEM_H = 10.5 * S
LEG_W = 88 * S
GAP, row_y, too_tall = layout(12 * S)
leg_h = 9 * S + LEG_ITEM_H * len(items)
leg_y0 = row_y[NGEN - 1]
blocking = [xs[k] - cards[k]["w"] / 2 for k in anc
            if row_y[anc[k]] < leg_y0 + leg_h + 3 * S and row_y[anc[k]] + row_h[anc[k]] > leg_y0]
LEGEND_LEFT = bool(items) and min(blocking, default=W) - X0 >= LEG_W + 6 * S
if not LEGEND_LEFT:
    GAP, row_y, too_tall = layout(30 * S)
if too_tall:
    print("Pozor: strom je vyšší než papír – zvol větší papír (--papir A1).", file=sys.stderr)


def card_box(k):
    """Všechny karty v řadě mají stejnou výšku (text je svisle uprostřed)."""
    g = cards[k]["g"]
    return xs[k] - cards[k]["w"] / 2, row_y[g], cards[k]["w"], row_h[g]


# ---------------------------------------------------------------- kreslení
E = html.escape
FONT = "Georgia, 'Times New Roman', serif"
SYM = "'Segoe UI Symbol', 'DejaVu Sans', 'Noto Sans Symbols', sans-serif"
LINE = "#8C7660"
out = []
a = out.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}" '
  f'font-family="{FONT}">')
a('<defs><filter id="sh" x="-10%" y="-10%" width="120%" height="130%">'
  f'<feDropShadow dx="0" dy="{0.35 * S:.2f}" stdDeviation="{0.45 * S:.2f}" flood-color="#5B4636" flood-opacity="0.18"/>'
  '</filter>'
  '<radialGradient id="paper" cx="50%" cy="45%" r="75%"><stop offset="0" stop-color="#FDFAF3"/>'
  '<stop offset="1" stop-color="#F3EBDC"/></radialGradient></defs>')
a(f'<rect width="{W}" height="{H}" fill="url(#paper)"/>')
# rámeček
a(f'<rect x="{FRAME}" y="{FRAME}" width="{W - 2 * FRAME}" height="{H - 2 * FRAME}" fill="none" '
  f'stroke="#A88B6A" stroke-width="{0.6 * S}"/>')
a(f'<rect x="{FRAME + 1.6 * S}" y="{FRAME + 1.6 * S}" width="{W - 2 * FRAME - 3.2 * S}" '
  f'height="{H - 2 * FRAME - 3.2 * S}" fill="none" stroke="#A88B6A" stroke-width="{0.25 * S}"/>')
for cx, cy in ((FRAME, FRAME), (W - FRAME, FRAME), (FRAME, H - FRAME), (W - FRAME, H - FRAME)):
    a(f'<rect x="{cx - 2 * S}" y="{cy - 2 * S}" width="{4 * S}" height="{4 * S}" fill="#F7F1E5" '
      f'stroke="#A88B6A" stroke-width="{0.4 * S}" transform="rotate(45 {cx} {cy})"/>')

# hlavička
root = P[ROOTK]
rd = person(ROOTK)
ty = FRAME + 17 * S
a(f'<text x="{W / 2}" y="{ty}" text-anchor="middle" font-size="{4.2 * S}" letter-spacing="{1.6 * S}" '
  f'fill="#8C6E4F">RODOKMEN</text>')
a(f'<text x="{W / 2}" y="{ty + 13 * S}" text-anchor="middle" font-size="{13 * S}" fill="#2E241C">'
  f'{E(rd["name"])}</text>')
n_anc = len(anc) - 1
max_g = NGEN - 1
GEN_WORD = {1: "jedné generaci", 2: "dvou generacích", 3: "třech generacích", 4: "čtyřech generacích",
            5: "pěti generacích", 6: "šesti generacích", 7: "sedmi generacích", 8: "osmi generacích",
            9: "devíti generacích", 10: "deseti generacích"}


def predku(n):
    return "předek" if n == 1 else "předkové" if 2 <= n <= 4 else "předků"


sub = (f'roz. {rd["roz"]}  ·  ' if rd["roz"] else "") + f'{n_anc} {predku(n_anc)} v {GEN_WORD.get(max_g, str(max_g) + " generacích")}'
a(f'<text x="{W / 2}" y="{ty + 22 * S}" text-anchor="middle" font-size="{4.6 * S}" font-style="italic" '
  f'fill="#5A4A3E">{E(sub)}</text>')
# ornament pod nadpisem
oy = ty + 27.5 * S
a(f'<g stroke="#A88B6A" stroke-width="{0.3 * S}" fill="none">'
  f'<line x1="{W / 2 - 40 * S}" y1="{oy}" x2="{W / 2 - 4 * S}" y2="{oy}"/>'
  f'<line x1="{W / 2 + 4 * S}" y1="{oy}" x2="{W / 2 + 40 * S}" y2="{oy}"/>'
  f'<rect x="{W / 2 - 1.6 * S}" y="{oy - 1.6 * S}" width="{3.2 * S}" height="{3.2 * S}" fill="#A88B6A" '
  f'transform="rotate(45 {W / 2} {oy})"/></g>')
if VENOVANI:
    a(f'<text x="{W / 2}" y="{oy + 8 * S}" text-anchor="middle" font-size="{4.4 * S}" font-style="italic" '
      f'fill="#8C6E4F">{E(VENOVANI)}</text>')

# popisky generací (vlevo)
GEN_NAME = {0: "", 1: "rodiče", 2: "prarodiče", 3: "praprarodiče", 4: "prapraprarodiče"}
for g in range(1, NGEN):
    cy = row_y[g] + row_h[g] / 2
    lx = FRAME + 6 * S
    a(f'<text x="{lx}" y="{cy - 1 * S}" font-size="{8 * S}" fill="#C9B79F" font-style="italic">{g}.</text>')
    a(f'<text x="{lx}" y="{cy + 4.2 * S}" font-size="{2.5 * S}" letter-spacing="{0.35 * S}" fill="#8C6E4F">'
      f'{E((GEN_NAME.get(g) or "generace").upper())}</text>')
    if g >= 5:
        a(f'<text x="{lx}" y="{cy + 7.6 * S}" font-size="{2.5 * S}" letter-spacing="{0.35 * S}" fill="#8C6E4F">'
          f'PŘEDKŮ</text>')

# spojnice
labels = []
lw = 0.42 * S
for k in sorted(anc):
    ps = parents(k)
    if not ps:
        continue
    cx, cy, cw, ch = card_box(k)
    ctop = cy
    if len(ps) == 2:
        fx, fy, fw, fh = card_box(ps[0])
        mx, my, mw, mh = card_box(ps[1])
        bar_y = row_y[anc[ps[0]]] + row_h[anc[ps[0]]] / 2
        a(f'<line x1="{fx + fw}" y1="{bar_y}" x2="{mx}" y2="{bar_y}" stroke="{LINE}" stroke-width="{lw}"/>')
        midx = (xs[ps[0]] + xs[ps[1]]) / 2
        a(f'<path d="M{midx},{bar_y} V{ctop}" stroke="{LINE}" stroke-width="{lw}" fill="none"/>')
        a(f'<circle cx="{midx}" cy="{bar_y}" r="{0.9 * S}" fill="#F7F1E5" stroke="{LINE}" stroke-width="{lw}"/>')
        m = marriage(ps[0], ps[1])
        if m:
            g = anc[ps[0]]
            labels.append((midx, row_y[g] + row_h[g] + min(GAP * 0.45, 5.5 * S), m, body_size(g) * 0.98))
    else:
        px, py, pw, ph = card_box(ps[0])
        a(f'<line x1="{xs[ps[0]]}" y1="{py + ph}" x2="{xs[ps[0]]}" y2="{ctop}" stroke="{LINE}" stroke-width="{lw}"/>')

for x, y, t, sz in labels:
    sym, rest = t[:1], t[2:]
    tw = text_w(rest, sz, "i") + sz * 1.3
    a(f'<rect x="{x - tw / 2 - 1.4 * S}" y="{y - sz * 0.95}" width="{tw + 2.8 * S}" height="{sz * 1.45}" '
      f'rx="{sz * 0.7}" fill="#F8F2E6" stroke="#D8C7AE" stroke-width="{0.2 * S}"/>')
    a(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{sz}" fill="#6B5644" font-style="italic">'
      f'<tspan font-family="{SYM}" font-style="normal">{sym}</tspan> {E(rest)}</text>')

# karty
for k in sorted(anc, key=lambda k: anc[k]):
    x, y, w, h = card_box(k)
    c = cards[k]
    col = color(k)
    g = c["g"]
    is_root = k == ROOTK
    r = 1.6 * S
    fill = "#FFFDF8" if not is_root else "#5B4636"
    a(f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" '
      f'stroke="{col if not is_root else "#3F2F23"}" stroke-opacity="0.55" stroke-width="{0.3 * S}"/></g>')
    if not is_root:
        a(f'<path d="M{x},{y + r} a{r},{r} 0 0 1 {r},{-r} h{w - 2 * r} a{r},{r} 0 0 1 {r},{r} v{0.6 * S} h{-w} z" '
          f'fill="{col}"/>')
    pad = 2.4 * S if g >= 4 else 3.2 * S
    ty_ = y + pad + 1.6 * S + (h - c["h"]) / 2
    for t, sz, st, fc, gap in c["lines"]:
        ty_ += gap + sz * 0.95
        attrs = ' font-weight="bold"' if st == "b" else ' font-style="italic"' if st == "i" else ""
        if is_root:
            fc = "#FFF8EC" if st != "i" else "#E9D9C2"
        a(f'<text x="{xs[k]}" y="{ty_:.2f}" text-anchor="middle" font-size="{sz:.2f}"{attrs} fill="{fc}">{E(t)}</text>')
        ty_ += sz * 0.27

# panely po stranách výchozí osoby (č. ROOTK)
rx, ry, rw, rh = card_box(ROOTK)

# 1. QR kód a odkaz na rodinný web (vpravo od kořene)
if QR_URL:
    qw = 92 * S
    qh = rh
    qx = min(W - MARGIN - qw - 2 * S, xs[ROOTK] + rw / 2 + 16 * S)
    qy = ry
    qr_sz = 17.5 * S
    qrx = qx + 4.0 * S
    qry = qy + (qh - qr_sz) / 2
    clean_url = re.sub(r"^https?://", "", QR_URL).rstrip("/")

    a(f'<a href="{E(QR_URL)}" target="_blank" style="text-decoration:none;">')
    a(f'<g filter="url(#sh)"><rect x="{qx}" y="{qy}" width="{qw}" height="{qh}" rx="{1.6 * S}" '
      f'fill="#FFFDF8" stroke="#A88B6A" stroke-opacity="0.65" stroke-width="{0.35 * S}"/></g>')
    # bílý podklad pod QR kódem
    a(f'<rect x="{qrx - 1.2 * S}" y="{qry - 1.2 * S}" width="{qr_sz + 2.4 * S}" height="{qr_sz + 2.4 * S}" '
      f'rx="{1.0 * S}" fill="#FFFFFF" stroke="#D8C7AE" stroke-width="{0.25 * S}"/>')
    # vektorový QR kód
    a(qr_svg(QR_URL, qrx, qry, qr_sz, fill="#2E241C"))
    # texty a odkaz
    tx = qx + qr_sz + 7.8 * S
    a(f'<text x="{tx}" y="{qy + 7.2 * S}" font-size="{2.6 * S}" letter-spacing="{0.4 * S}" '
      f'fill="#8C6E4F">RODINNÝ WEB</text>')
    a(f'<text x="{tx}" y="{qy + 13.5 * S}" font-size="{3.5 * S}" font-weight="bold" '
      f'fill="#2E241C">{E(clean_url)}</text>')
    a(f'<text x="{tx}" y="{qy + 19.2 * S}" font-size="{2.45 * S}" font-style="italic" '
      f'fill="#5A4A3E">Příběhy rodu · fotografie · matriky</text>')
    a('</a>')

# 2. Informační panel o předcích (vlevo od kořene pro symetrii)
bw = 92 * S
bh = rh
bx = max(MARGIN + LABELW + 2 * S, xs[ROOTK] - rw / 2 - 16 * S - bw)
by = ry
btx = bx + bw / 2 + 1.2 * S

a(f'<g filter="url(#sh)"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="{1.6 * S}" '
  f'fill="#FFFDF8" stroke="#A88B6A" stroke-opacity="0.65" stroke-width="{0.35 * S}"/></g>')
a(f'<path d="M{bx},{by + 1.6 * S} a{1.6 * S},{1.6 * S} 0 0 1 {1.6 * S},{-1.6 * S} h{2.0 * S} v{bh} h{-2.0 * S} '
  f'a{1.6 * S},{1.6 * S} 0 0 1 {-1.6 * S},{-1.6 * S} z" fill="#8C6E4F"/>')
a(f'<text x="{btx}" y="{by + 7.2 * S}" text-anchor="middle" font-size="{2.6 * S}" letter-spacing="{0.4 * S}" '
  f'fill="#8C6E4F">PŘÍMÁ LINIE PŘEDKŮ</text>')
a(f'<text x="{btx}" y="{by + 13.5 * S}" text-anchor="middle" font-size="{3.5 * S}" font-weight="bold" '
  f'fill="#2E241C">{n_anc} předků v {max_g} generacích</text>')
a(f'<text x="{btx}" y="{by + 19.2 * S}" text-anchor="middle" font-size="{2.45 * S}" font-style="italic" '
  f'fill="#5A4A3E">Čechy a Morava · 18. až 20. století</text>')

# legenda větví
if LEGEND_LEFT:
    lx, ly = X0 + 2 * S, leg_y0 + 3 * S
    a(f'<text x="{lx}" y="{ly}" font-size="{2.8 * S}" letter-spacing="{0.5 * S}" fill="#8C6E4F">RODY A VĚTVE</text>')
    a(f'<line x1="{lx}" y1="{ly + 2 * S}" x2="{lx + 40 * S}" y2="{ly + 2 * S}" stroke="#C9B79F" '
      f'stroke-width="{0.25 * S}"/>')
    for i, (col, title, desc) in enumerate(items):
        iy = ly + 9 * S + i * LEG_ITEM_H
        a(f'<rect x="{lx}" y="{iy - 3.2 * S}" width="{4 * S}" height="{4 * S}" rx="{0.7 * S}" fill="{col}"/>')
        a(f'<text x="{lx + 6.5 * S}" y="{iy}" font-size="{3.8 * S}" font-weight="bold" fill="#2E241C">{E(title)}</text>')
        a(f'<text x="{lx + 6.5 * S}" y="{iy + 4.2 * S}" font-size="{2.9 * S}" font-style="italic" fill="#5A4A3E">'
          f'{E(wrap(desc, 2.9 * S, LEG_W - 8 * S, "i", 1)[0])}</text>')
else:
    ly = H - FRAME - 26 * S + 7 * S
    cell = (W - 2 * MARGIN) / max(1, len(items))
    for i, (col, title, desc) in enumerate(items):
        cx = MARGIN + cell * i + cell / 2
        a(f'<rect x="{cx - text_w(title, 3.6 * S, "b") / 2 - 6 * S}" y="{ly - 3 * S}" width="{3.6 * S}" '
          f'height="{3.6 * S}" rx="{0.6 * S}" fill="{col}"/>')
        a(f'<text x="{cx}" y="{ly}" text-anchor="middle" font-size="{3.6 * S}" font-weight="bold" fill="#2E241C">'
          f'{E(title)}</text>')
        for j, t in enumerate(wrap(desc, 2.7 * S, cell - 8 * S, "i", 2)):
            a(f'<text x="{cx}" y="{ly + 4.4 * S + j * 3.4 * S}" text-anchor="middle" font-size="{2.7 * S}" '
              f'font-style="italic" fill="#5A4A3E">{E(t)}</text>')
today = datetime.date.today()
foot = (CUSTOM.get("zapati") or "Sestaveno z matričních zápisů státních oblastních archivů a rodinných vzpomínek") + \
    f"  ·  stav k {today.day}. {today.month}. {today.year}"
a(f'<text x="{W / 2}" y="{H - FRAME - 4.2 * S}" text-anchor="middle" font-size="{2.6 * S}" fill="#8C6E4F" '
  f'letter-spacing="{0.15 * S}">{E(foot)}</text>')
a("</svg>")
svg = "\n".join(out)

import unicodedata  # noqa: E402
plain = unicodedata.normalize("NFKD", re.sub(r"\b\w+\.\s*", "", rd["name"])).encode("ascii", "ignore").decode().lower()
slug = re.sub(r"[^a-z0-9]+", "_", plain).strip("_")
base = os.path.join(OUT, f"predkove_{slug}_{PAPIR.lower()}")
open(base + ".svg", "w", encoding="utf-8").write(svg)
page = (f'<!doctype html><html><head><meta charset="utf-8"><style>@page{{size:{W}mm {H}mm;margin:0}}'
        f'html,body{{margin:0;padding:0;width:{W}mm;height:{H}mm;overflow:hidden}}svg{{display:block}}</style>'
        f'</head><body>{svg}</body></html>')
open(base + ".html", "w", encoding="utf-8").write(page)
print("SVG:", base + ".svg")

CHROME = next((c for c in ("C:/Program Files/Google/Chrome/Application/chrome.exe",
                           "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
                           "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
                           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                           "google-chrome", "chromium", "chromium-browser")
               if os.path.exists(c) or shutil.which(c)), None)
if CHROME:
    url = "file:///" + (base + ".html").replace("\\", "/").lstrip("/")
    with tempfile.TemporaryDirectory() as prof:
        common = [CHROME, "--headless=new", "--disable-gpu", f"--user-data-dir={prof}", "--hide-scrollbars"]
        subprocess.run(common + ["--no-pdf-header-footer", f"--print-to-pdf={base}.pdf", url],
                       capture_output=True, timeout=120)
        px_w = 2400
        px_h = round(px_w * H / W)
        scale = px_w / (W / 25.4 * 96)
        subprocess.run(common + [f"--window-size={round(W / 25.4 * 96)},{round(H / 25.4 * 96)}",
                                 f"--force-device-scale-factor={scale:.4f}", f"--screenshot={base}.png", url],
                       capture_output=True, timeout=120)
    for ext in ("pdf", "png"):
        if os.path.exists(f"{base}.{ext}"):
            print(ext.upper() + ":", f"{base}.{ext}")
else:
    print("Chrome/Edge nenalezen – PDF vytiskni z HTML souboru v prohlížeči (bez okrajů).")
