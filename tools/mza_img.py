#!/usr/bin/env python3
"""Stažení snímku matriky z portálu Actapublica (MZA Brno, www.mza.cz/actapublica).

Použití:
  mza_img.py <detail_id> <snimek> [uroven] [vystup.jpg] [x0,y0,x1,y1]
      detail_id: ID knihy v URL (např. 13256 pro https://www.mza.cz/actapublica/matrika/detail/13256)
      snimek: 1-based číslo snímku (1 .. počet snímků)
      uroven: 0 = plné rozlišení (výchozí pro výřezy), 1 = polovina (výchozí pro celou stranu), 2 = čtvrtina, 3 = osmina
      x0,y0,x1,y1: zlomky 0..1 (např. 0.05,0.42,0.95,0.68) – stahují se jen potřebné dlaždice
  mza_img.py <detail_id> info          -> popis svazku, obce, roky a počet snímků
  mza_img.py <detail_id> link <n>      -> trvalý odkaz na snímek n v prohlížeči Actapublica
  mza_img.py <detail_id> svazek        -> zapíše svazek do data/svazky.json (klíč = mza_<detail_id>)

Popis a seznam snímků se ukládá do pracovni/.cache_mza/<detail_id>.json.
"""
import asyncio
import io
import json
import math
import os
import re
import sys
import xml.etree.ElementTree as ET
from PIL import Image
import httpx

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "pracovni", ".cache_mza")
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def get_sync_client():
    return httpx.Client(http2=True, follow_redirects=True, timeout=30.0)


def load_volume(detail_id):
    os.makedirs(CACHE, exist_ok=True)
    cache_path = os.path.join(CACHE, f"{detail_id}.json")
    if os.path.exists(cache_path):
        with open(cache_path, encoding="utf-8") as f:
            return json.load(f)

    url = f"https://www.mza.cz/actapublica/matrika/detail/{detail_id}"
    with get_sync_client() as client:
        r = client.get(url, headers=HEADERS)
        html = r.text

    # Parse table-item-label and table-item-value
    meta_dict = {}
    rows = re.findall(
        r'<tr>\s*<td class="table-item-label">(.*?)</td>\s*<td class="table-item-value">(.*?)</td>\s*</tr>',
        html,
        re.S,
    )
    for lbl, val in rows:
        l = ' '.join(re.sub(r'<[^>]+>', ' ', lbl).split())
        v = ' '.join(re.sub(r'<[^>]+>', ' ', val).split())
        meta_dict[l] = v

    obce_m = re.search(
        r'Obce a jiné lokality.*?</tr>\s*<tr>\s*<td[^>]*class="table-item-value"[^>]*>(.*?)</td>',
        html,
        re.S,
    )
    obce = ' '.join(re.sub(r'<[^>]+>', ' ', obce_m.group(1)).split()) if obce_m else ""

    sign = str(detail_id)
    for k, v in meta_dict.items():
        if "Číslo knihy" in k:
            sign = v.split()[0]
            break

    puvodce = ""
    for k, v in meta_dict.items():
        if "Původce" in k:
            puvodce = v
            break

    obsahy = []
    for k, v in meta_dict.items():
        if "Narození" in k and v and v != "-":
            obsahy.append(f"N: {v}")
        elif "Oddaní" in k and v and v != "-":
            obsahy.append(f"O: {v}")
        elif "Zemřelí" in k and v and v != "-":
            obsahy.append(f"Z: {v}")
    obsah = ", ".join(obsahy)

    dzi_list = []
    jp2_list = []
    sd_m = re.search(r'CreateSeadragon\s*\(\s*(\[[^\]]+\])\s*,\s*(\[[^\]]+\])', html, re.S)
    if sd_m:
        raw_dzi = json.loads(sd_m.group(1))
        raw_jp2 = json.loads(sd_m.group(2))
        dzi_list = [u.replace(r'\/', '/') for u in raw_dzi]
        jp2_list = raw_jp2

    vol_data = {
        "id": str(detail_id),
        "signatura": sign,
        "puvodce": puvodce,
        "obsah": obsah,
        "obce": obce,
        "casovy_rozsah": obsah,
        "dzi_list": dzi_list,
        "jp2_list": jp2_list,
        "snimku": len(dzi_list),
        "url": url,
    }

    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(vol_data, f, ensure_ascii=False, indent=2)

    return vol_data


async def async_fetch_image(dzi_url, level_offset=1, out="page.jpg", crop=None):
    async with httpx.AsyncClient(http2=True, follow_redirects=True, timeout=45.0) as client:
        r = await client.get(dzi_url, headers=HEADERS)
        root = ET.fromstring(r.text)
        size = root.find("{http://schemas.microsoft.com/deepzoom/2008}Size")
        w_orig = int(size.attrib["Width"])
        h_orig = int(size.attrib["Height"])
        tile_size = int(root.attrib.get("TileSize", 256))
        fmt = root.attrib.get("Format", "jpg")
        max_dim = max(w_orig, h_orig)
        max_level = math.ceil(math.log2(max_dim))

        target_level = max(0, max_level - level_offset)
        scale = 1.0 / (2 ** (max_level - target_level))

        w = math.ceil(w_orig * scale)
        h = math.ceil(h_orig * scale)
        cols = math.ceil(w / tile_size)
        rows = math.ceil(h / tile_size)

        if crop:
            x0_f, y0_f, x1_f, y1_f = crop
            px0 = int(x0_f * w)
            py0 = int(y0_f * h)
            px1 = int(x1_f * w)
            py1 = int(y1_f * h)
            c0 = max(0, px0 // tile_size)
            c1 = min(cols - 1, px1 // tile_size)
            r0 = max(0, py0 // tile_size)
            r1 = min(rows - 1, py1 // tile_size)
        else:
            px0, py0, px1, py1 = 0, 0, w, h
            c0, c1 = 0, cols - 1
            r0, r1 = 0, rows - 1

        base_tiles_url = dzi_url.replace(".dzi", f"_files/{target_level}")

        sem = asyncio.Semaphore(8)

        async def fetch_one(col, row):
            url = f"{base_tiles_url}/{col}_{row}.{fmt}"
            for attempt in range(5):
                async with sem:
                    try:
                        resp = await client.get(url, headers=HEADERS)
                        if resp.status_code == 200:
                            return (col, row, resp.content)
                        elif resp.status_code == 429:
                            await asyncio.sleep(1.0 * (attempt + 1))
                            continue
                        else:
                            raise RuntimeError(f"Chyba při stahování dlaždice {col}_{row}: HTTP {resp.status_code}")
                    except Exception as e:
                        if attempt == 4:
                            raise e
                        await asyncio.sleep(0.5 * (attempt + 1))
            raise RuntimeError(f"Chyba při stahování dlaždice {col}_{row}: přesáhnut počet pokusů")

        tasks = []
        for r_idx in range(r0, r1 + 1):
            for c_idx in range(c0, c1 + 1):
                tasks.append(fetch_one(c_idx, r_idx))

        results = await asyncio.gather(*tasks)

        canvas_w = (c1 - c0 + 1) * tile_size
        canvas_h = (r1 - r0 + 1) * tile_size
        canvas = Image.new("RGB", (canvas_w, canvas_h))

        for col, row, content in results:
            tile = Image.open(io.BytesIO(content))
            paste_x = (col - c0) * tile_size
            paste_y = (row - r0) * tile_size
            canvas.paste(tile, (paste_x, paste_y))

        crop_box = (
            px0 - c0 * tile_size,
            py0 - r0 * tile_size,
            px1 - c0 * tile_size,
            py1 - r0 * tile_size,
        )
        final_img = canvas.crop(crop_box)
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        final_img.save(out, "JPEG", quality=88)
        return out, (w_orig, h_orig)


def fetch_image(dzi_url, level_offset=1, out="page.jpg", crop=None):
    return asyncio.run(async_fetch_image(dzi_url, level_offset, out, crop))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    detail_id = sys.argv[1]
    vol = load_volume(detail_id)

    cmd = sys.argv[2]
    if cmd == "info":
        print(f"Svazek: {vol['signatura']} | Původce: {vol['puvodce']}")
        print(f"Obsah: {vol['obsah']} | Obce: {vol['obce']}")
        print(f"Časový rozsah: {vol['casovy_rozsah']} | Snímků: {vol['snimku']}")
        print(f"URL: {vol['url']}")
        sys.exit(0)

    if cmd == "svazek":
        path = os.path.join(ROOT, "data", "svazky.json")
        sv = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
        key = f"mza_{detail_id}"
        sv[key] = {
            "archiv": "MZA Brno",
            "portal": "Actapublica",
            "fond": vol["puvodce"],
            "svazek": f"sign. {vol['signatura']} ({vol['obsah']})",
            "obce": vol["obce"],
            "roky": vol["casovy_rozsah"],
            "snimku": vol["snimku"],
            "url": vol["url"],
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(sv, f, ensure_ascii=False, indent=2)
        print(f"{key} -> {sv[key]['svazek']}")
        sys.exit(0)

    if cmd == "link":
        sn = int(sys.argv[3])
        if 1 <= sn <= len(vol["jp2_list"]):
            jp2_name = vol["jp2_list"][sn - 1]
            print(f"https://www.mza.cz/actapublica/matrika/detail/{detail_id}?image={jp2_name}")
        else:
            print(f"https://www.mza.cz/actapublica/matrika/detail/{detail_id}")
        sys.exit(0)

    # Download command: snimek [uroven] [vystup] [crop]
    sn = int(cmd)
    if sn < 1 or sn > len(vol["dzi_list"]):
        print(f"Chyba: snímek {sn} mimo rozsah (kniha má {len(vol['dzi_list'])} snímků)")
        sys.exit(1)

    dzi_url = vol["dzi_list"][sn - 1]

    crop_str = sys.argv[5] if len(sys.argv) > 5 else None
    crop = tuple(float(v) for v in crop_str.split(",")) if crop_str else None

    if len(sys.argv) > 3 and sys.argv[3] != "":
        lo = int(sys.argv[3])
    else:
        lo = 0 if crop else 1

    out = sys.argv[4] if len(sys.argv) > 4 else f"mza_{detail_id}_{sn:04d}.jpg"

    print(f"Stahuji detail {detail_id}, snímek {sn}/{vol['snimku']} (úroveň {lo})...")
    path, dims = fetch_image(dzi_url, level_offset=lo, out=out, crop=crop)
    print(f"Uloženo: {path} (plná velikost originálu: {dims[0]}x{dims[1]})")


if __name__ == "__main__":
    main()
