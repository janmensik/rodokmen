#!/usr/bin/env python3
"""Export dat z rodokmenu (site.json) do standalone webové aplikace Strom (ACiDekCZ/strom).

Generuje web/public/strom-app/index.html se všemi daty rodokmenu vloženými do window.STROM_EMBEDDED_DATA.
"""
import base64
import json
import os
import re
import sys
import unicodedata

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
WEB = os.path.join(ROOT, "web")
DATA_DIR = os.path.join(ROOT, "data")
IMG_DIR = os.path.join(WEB, "public", "img")
SITE_JSON_PATH = os.path.join(WEB, "src", "data", "site.json")
OUT_DIR = os.path.join(WEB, "public", "strom-app")
OUT_HTML = os.path.join(OUT_DIR, "index.html")
TEMPLATE_PATH = os.path.join(TOOLS, "strom-template.html")


def place_key(raw):
    """Normalize place string to match Strom's placeKey()."""
    if not raw:
        return ""
    nfkd = unicodedata.normalize("NFKD", raw)
    no_accents = "".join(c for c in nfkd if not unicodedata.combining(c))
    low = no_accents.lower()
    clean = re.sub(r"[.,;]", " ", low)
    return re.sub(r"\s+", " ", clean).strip()


def parse_name(full_name, roz, sex):
    """Rozdělí celé jméno na tituly, křestní jméno, příjmení a vyvdané příjmení."""
    name = full_name.strip()
    title_before = ""
    title_match = re.match(r"^((?:(?:Mgr|Ing|JUDr|PhDr|MUDr|doc|RNDr|Fr)\.?\s*)+)", name, re.IGNORECASE)
    if title_match:
        title_before = title_match.group(1).strip()
        name = name[len(title_match.group(0)):].strip()

    name = re.sub(r"\s*\(?roz\.\s*[^)]+\)?$", "", name, flags=re.IGNORECASE).strip()

    parts = name.split()
    if len(parts) == 1:
        return {
            "titleBefore": title_before or None,
            "firstName": parts[0],
            "lastName": roz or parts[0],
            "marriedSurname": None
        }

    first_name = " ".join(parts[:-1])
    last_name = parts[-1]
    married_surname = None

    if sex == "F" and roz:
        if roz.lower() != last_name.lower():
            married_surname = last_name
            last_name = roz

    return {
        "titleBefore": title_before or None,
        "firstName": first_name,
        "lastName": last_name,
        "marriedSurname": married_surname
    }


def parse_event_str(raw):
    """Parsuje text narození/úmrtí na datum a místo."""
    if not raw:
        return None, None
    raw = raw.strip()
    date_part = ""
    place_part = ""

    comma_idx = raw.find(",")
    if comma_idx != -1:
        date_part = raw[:comma_idx].strip()
        place_part = raw[comma_idx + 1:].strip()
    else:
        if re.match(r"^(?:asi|kolem|cca|před|pred|po)?\s*(?:\d{1,2}\.\s*\d{1,2}\.\s*)?\d{4}$", raw, re.IGNORECASE):
            date_part = raw
        else:
            m = re.match(r"^((?:asi|kolem|cca|před|pred|po)?\s*(?:\d{1,2}\.\s*\d{1,2}\.\s*)?\d{4})\s*(.*)$", raw, re.IGNORECASE)
            if m:
                date_part = m.group(1).strip()
                place_part = m.group(2).strip()
            else:
                place_part = raw

    date_val = None
    if date_part:
        qual = ""
        d_str = date_part
        if re.match(r"^(?:asi|kolem|cca)", d_str, re.IGNORECASE):
            qual = "~"
            d_str = re.sub(r"^(?:asi|kolem|cca)", "", d_str, flags=re.IGNORECASE).strip()
        elif re.match(r"^(?:před|pred)", d_str, re.IGNORECASE):
            qual = "<"
            d_str = re.sub(r"^(?:před|pred)", "", d_str, flags=re.IGNORECASE).strip()
        elif re.match(r"^po", d_str, re.IGNORECASE):
            qual = ">"
            d_str = re.sub(r"^po", "", d_str, flags=re.IGNORECASE).strip()

        full_d = re.match(r"^(\d{1,2})\.\s*(\d{1,2})\.\s*(\d{4})$", d_str)
        month_d = re.match(r"^(\d{1,2})\.\s*(\d{4})$", d_str)
        year_d = re.match(r"^(\d{4})$", d_str)

        if full_d:
            day = full_d.group(1).zfill(2)
            month = full_d.group(2).zfill(2)
            year = full_d.group(3)
            date_val = f"{qual}{year}-{month}-{day}"
        elif month_d:
            month = month_d.group(1).zfill(2)
            year = month_d.group(2)
            date_val = f"{qual}{year}-{month}"
        elif year_d:
            date_val = f"{qual}{year_d.group(1)}"
        else:
            date_val = date_part

    return (date_val or None), (place_part or None)


def build_strom_data():
    with open(SITE_JSON_PATH, "r", encoding="utf-8") as f:
        site = json.load(f)

    # 1. Pre-load portrait photos as base64 data URLs
    photo_cache = {}
    for slug, p in site.get("people", {}).items():
        docs = p.get("docs", [])
        foto_docs = [d for d in docs if d.get("img", "").startswith("foto_")]
        if foto_docs:
            img_key = foto_docs[0]["img"]
            img_path = os.path.join(IMG_DIR, f"{img_key}.jpg")
            if os.path.exists(img_path):
                try:
                    with open(img_path, "rb") as img_f:
                        b64 = base64.b64encode(img_f.read()).decode("ascii")
                        photo_cache[slug] = f"data:image/jpeg;base64,{b64}"
                except Exception as e:
                    print(f"Varování: nepodařilo se načíst foto {img_path}: {e}")

    # 2. Convert people
    persons = {}
    for slug, p in site.get("people", {}).items():
        name_info = parse_name(p.get("name", slug), p.get("roz", ""), p.get("sex", "M"))
        det = p.get("details", {})
        birth_d, birth_p = parse_event_str(det.get("birth", ""))
        death_d, death_p = parse_event_str(det.get("death", ""))

        if not birth_d and p.get("y"):
            # Try to extract year from y (e.g. "* 1873")
            ym = re.search(r"\*\s*(\d{4})", p.get("y", ""))
            if ym:
                birth_d = ym.group(1)

        if not death_d and p.get("y"):
            # Try to extract year from y (e.g. "† 1945")
            ym = re.search(r"†\s*(\d{4})", p.get("y", ""))
            if ym:
                death_d = ym.group(1)

        parent_ids = []
        if p.get("father"):
            parent_ids.append(p["father"])
        if p.get("mother"):
            parent_ids.append(p["mother"])

        child_ids = p.get("children", [])

        events = []
        if det.get("job"):
            events.append({
                "id": f"ev_job_{slug}",
                "type": "occupation",
                "description": det["job"]
            })
        if det.get("burial"):
            b_d, b_p = parse_event_str(det["burial"])
            events.append({
                "id": f"ev_burial_{slug}",
                "type": "burial",
                "date": b_d,
                "place": b_p
            })

        notes_parts = []
        if p.get("note"):
            notes_parts.append(p["note"])
        if det.get("home"):
            notes_parts.append(f"Bydliště: {det['home']}")
        if p.get("rel"):
            notes_parts.append(f"Vztah: {p['rel']}")
        if p.get("status"):
            notes_parts.append(f"Stav bádání: {p['status']}")
        if p.get("side"):
            side_str = ", ".join(s.get("name", "") for s in p["side"])
            notes_parts.append(f"Boční příbuzní: {side_str}")

        person_obj = {
            "id": slug,
            "firstName": name_info["firstName"],
            "lastName": name_info["lastName"],
            "gender": "F" if p.get("sex") == "F" else "M",
            "isPlaceholder": False,
            "partnerships": [],
            "parentIds": parent_ids,
            "childIds": child_ids,
            "refn": str(p.get("k", "")) if p.get("k") else slug,
        }

        if name_info.get("titleBefore"):
            person_obj["titleBefore"] = name_info["titleBefore"]
        if name_info.get("marriedSurname"):
            person_obj["marriedSurname"] = name_info["marriedSurname"]
        if birth_d:
            person_obj["birthDate"] = birth_d
        if birth_p:
            person_obj["birthPlace"] = birth_p
        if death_d:
            person_obj["deathDate"] = death_d
        if death_p:
            person_obj["deathPlace"] = death_p
        if slug in photo_cache:
            person_obj["photo"] = photo_cache[slug]
        if notes_parts:
            person_obj["notes"] = "\n\n".join(notes_parts)
        if events:
            person_obj["events"] = events

        # Attach source IDs citing this person
        if p.get("records"):
            person_obj["sourceIds"] = p["records"]

        persons[slug] = person_obj

    # 3. Convert families / partnerships
    partnerships = {}
    for fam_id, fam in site.get("families", {}).items():
        p1 = fam.get("father") or fam.get("mother")
        p2 = fam.get("mother") or fam.get("father")
        if not p1 or not p2:
            continue

        start_date = None
        start_place = None
        if fam.get("marriage") and len(fam["marriage"]) > 0:
            m_str = fam["marriage"][0]
            # format e.g. "× 12. 9. 2009 Zvíkov Mgr. Julie Menšík Čákiová"
            m_clean = re.sub(r"^[×xX]\s*", "", m_str).strip()
            # extract date
            dm = re.match(r"^(\d{1,2}\.\s*\d{1,2}\.\s*\d{4})\s*(.*)$", m_clean)
            if dm:
                start_date, _ = parse_event_str(dm.group(1))
                rem = dm.group(2).strip()
                # place is before partner name if present
                words = rem.split()
                if words:
                    start_place = words[0]

        partnership_obj = {
            "id": fam_id,
            "person1Id": p1,
            "person2Id": p2,
            "childIds": fam.get("children", []),
            "status": "married"
        }
        if start_date:
            partnership_obj["startDate"] = start_date
        if start_place:
            partnership_obj["startPlace"] = start_place

        partnerships[fam_id] = partnership_obj

        # Link to persons
        if p1 in persons and fam_id not in persons[p1]["partnerships"]:
            persons[p1]["partnerships"].append(fam_id)
        if p2 in persons and fam_id not in persons[p2]["partnerships"]:
            persons[p2]["partnerships"].append(fam_id)

    # 4. Convert places
    places = {}
    for pl in site.get("places", []):
        name = pl.get("name", "")
        key = place_key(name)
        if key and "lat" in pl and "lon" in pl:
            places[key] = {
                "lat": pl["lat"],
                "lon": pl["lon"],
                "label": name
            }

    # 5. Convert sources
    sources = {}
    for rec in site.get("records", []):
        rec_key = rec.get("key")
        if rec_key:
            sources[rec_key] = {
                "id": rec_key,
                "title": rec.get("title", rec_key),
                "date": rec.get("date", ""),
                "repository": rec.get("archive", ""),
                "volume": rec.get("volume", ""),
                "page": rec.get("scan", ""),
                "url": rec.get("url", ""),
                "summary": rec.get("summary", "")
            }

    root_person = site.get("root", "mgr-jan-mensik-1980")
    if root_person not in persons and persons:
        root_person = list(persons.keys())[0]

    tree_name = site.get("config", {}).get("nazev", "Rodokmen Menšíkových")

    strom_data = {
        "version": 13,
        "persons": persons,
        "partnerships": partnerships,
        "sources": sources,
        "places": places,
        "defaultPersonId": root_person,
        "surnameVariants": [
            ["Menšík", "Menšíková"],
            ["Čáki", "Čákiová"],
            ["Jarolím", "Jarolímová"],
            ["Holánek", "Holánková"],
            ["Henzl", "Henzlová"]
        ]
    }

    envelope = {
        "exportId": "rodokmen-mensikovi-auto-export",
        "exportedAt": "2026-10-29T12:00:00.000Z",
        "appVersion": "3.17.1",
        "treeName": tree_name,
        "data": strom_data
    }

    return envelope


def generate_strom_app(template_html_path, out_html_path):
    envelope = build_strom_data()
    print(f"Data připravena: {len(envelope['data']['persons'])} osob, {len(envelope['data']['partnerships'])} rodin, {len(envelope['data']['places'])} míst.")

    with open(template_html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Create embedded data script
    envelope_json = json.dumps(envelope, ensure_ascii=False)
    # Safe embedding into script tag (prevent </script> injection)
    safe_json = envelope_json.replace("</script>", "<\\/script>").replace("<!--", "<\\!--")
    
    # Custom tweaks for embedded webapp:
    # 1. Hide the view-mode banner and standalone chrome
    # 2. Strict read-only mode (hide all edit and add controls)
    # 3. Focus on "Rodina" and "Potomci" (hide redundant timeline, fan, map)
    custom_head = f"""<style>
/* Clean embedding into rodokmen webapp */
#view-mode-banner {{ display: none !important; }}
#other-tab-notice {{ display: none !important; }}

/* Read-only mode: hide all add and edit controls */
.add-btn,
.rel-link-icon,
.btn-add-person,
#toolbar-buttons,
#toolbar-family-btn,
#bottom-bar-fab,
.edit-only,
.toolbar-undo-group,
.modal-footer button[type="submit"],
.btn-delete,
#btn-add-event,
#btn-add-attachment,
#person-sources-cite,
#person-sources-find,
#source-viewer-edit,
.source-viewer-edit-btn,
.source-edit-btn,
[data-action="edit"],
[data-action="add"],
[data-action="delete"],
[data-action="merge"],
[data-action="toggle-lock"] {{
  display: none !important;
}}

/* Hide standalone app branding and file indicators */
.toolbar-tree-icon,
.app-wordmark,
.tree-switcher,
#offline-indicator,
#file-link-indicator,
#unsaved-copy-indicator,
#research-sync-pill,
.desktop-actions {{
  display: none !important;
}}

/* In view-mode-segment: keep only Rodina and Potomci; hide redundant Timeline, Fan, Map */
#view-mode-timeline,
#view-mode-fan,
#view-mode-map {{
  display: none !important;
}}

/* Mobile bottom bar cleanup */
#bottom-bar-fab,
#bb-view-timeline,
#bb-view-fan,
#bb-view-map {{
  display: none !important;
}}

/* Clean toolbar styling */
.toolbar {{
  padding-left: 0.75rem;
  padding-right: 0.75rem;
  background: var(--surface, #faf7f2);
  border-bottom: 1px solid var(--border, #e8dfd1);
}}
</style>
<script>
window.STROM_EMBEDDED_DATA = {safe_json};
</script>
"""
    if "</head>" in html:
        output_html = html.replace("</head>", f"{custom_head}</head>", 1)
    else:
        output_html = f"<head>{custom_head}</head>" + html

    os.makedirs(os.path.dirname(out_html_path), exist_ok=True)
    with open(out_html_path, "w", encoding="utf-8") as f:
        f.write(output_html)

    size_kb = round(len(output_html.encode('utf-8')) / 1024)
    print(f"Vygenerovano: {out_html_path} ({size_kb} KB)")


if __name__ == "__main__":
    template = TEMPLATE_PATH
    if len(sys.argv) > 1:
        template = sys.argv[1]
    out = OUT_HTML
    if len(sys.argv) > 2:
        out = sys.argv[2]
    generate_strom_app(template, out)
