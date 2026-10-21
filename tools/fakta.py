#!/usr/bin/env python3
"""Jednotná struktura údajů o osobě – společná pro web (export_web.py), strom (tree_chart.py) i kontroly.

Osoba v data/osoby.py (P[k]) i člen boční větve (SIDE[...]["vetev"], jeho "manzel" a "deti") mají stejná pole:
  n      jméno
  y      roky pro přehledy: "* 1895", "1890–1944", "asi 1720–1785", "1857 – po 1914", "† před 1888", nic → ""
  f      životní události v tomto pořadí:  "* <datum> <místo>"   narození
                                           "× <datum> <místo> <manžel/ka>"   sňatek (i víc)
                                           "† <datum> <místo>"   úmrtí
         a za nimi ostatní volné údaje (původ rodičů, poznámky), např. "syn Martina Havla a Magdaleny Dolanské"
  roz    rodné příjmení ženy (jen když se liší od příjmení ve jméně)
  zam    povolání / postavení ("zámečník", "mistr krejčovský", "lékařka")
  bydl   bydliště ("Staré Ransko čp. 53", "Libčice nad Vltavou (od roku 2009)")
  puvod  odkud pochází, když se liší od místa narození ("Zemplín (Dúbrava / Šmigovec)")
  pohreb místo pohřbu
  vztah  (jen boční příbuzní) vztah k přímé linii ("bratr Jana")
  deti   (jen osoba 1, když jde o víc sourozenců) seznam dětí se stejnými poli

Starší zápisy (povolání nebo bydliště jako volný text ve "f", "† (pohřeb) …") se čtou dál – jen se zobrazí
mezi „Další údaje“.
"""
import re

DATE_RX = re.compile(r"^((?:asi|kolem|cca|před|po|mezi)\s+)?(\d{1,2}\.\s*\d{1,2}\.\s*)?\d{4}(?:\s*[–-]\s*\d{4})?")
TITLE_ONLY = re.compile(r"^(?:(?:Mgr|Ing|Bc|JUDr|MUDr|PhDr|RNDr|doc|prof|arch|MVDr|PaedDr|Ph\.D)\.?\s*)+$")


def years(y):
    """Roky pro přehledy (chip na stránce osoby, strom, vějíř): „1854–?“, „* 1980“, „† 1888“…"""
    y = (y or "").strip()
    ys = re.findall(r"\d{4}", y)
    if not ys:
        return ""
    approx = "≈" if re.match(r"^(asi|≈|cca)", y) else ""

    def qual(t):   # „před 1888“ / „po 1914“ / „≈1720“
        return "před " if re.search(r"\bpřed\b", t) else "po " if re.search(r"\bpo\b", t) else \
            "≈" if re.search(r"(asi|≈|cca)", t) else ""
    if y.startswith(("?", "†")):   # neznámé narození: ukázat jen úmrtí („? – před 1743“ → „† před 1743“)
        return "† " + qual(y) + ys[-1]
    if y.startswith("*"):
        segs = [s for s in y.split(",") if re.search(r"\d{4}", s)] if "–" not in y else [y.split("–")[0]]
        return ", ".join("* " + qual(s) + re.search(r"\d{4}", s).group() for s in segs)
    if len(ys) == 1:
        return approx + ys[0] + ("–?" if "–" in y else "")
    tail = y.split("–")[-1]
    q = qual(tail)
    if q in ("před ", "po "):
        return f"{approx}{ys[0]} – {q}{ys[-1]}"
    return f"{approx}{ys[0]}–{q}{ys[-1]}"


def split_event(text):
    """„7. 1. 1980 Praha“ → („7. 1. 1980“, „Praha“); „před 29. 5. 1888“ → („před 29. 5. 1888“, „“); „Rumburk“ → („“, „Rumburk“)."""
    text = text.strip()
    m = DATE_RX.match(text)
    if not m:
        return "", text
    return m.group(0).strip(), text[m.end():].strip(" ,")


def event_text(text):
    """Událost pro zobrazení: datum a místo oddělené čárkou („7. 1. 1980, Praha“)."""
    date, place = split_event(text)
    return ", ".join(x for x in (date, place) if x)


def structure(p):
    """Rozloží osobu do pevné struktury pro zobrazení (stejné pořadí a stejná pole u všech osob)."""
    s = dict(birth="", marriages=[], death="", burial=p.get("pohreb", ""), roz=p.get("roz", ""),
             job=p.get("zam", ""), home=p.get("bydl", ""), origin=p.get("puvod", ""), rel=p.get("vztah", ""),
             other=[], kids=[])
    for f in p.get("f", []):
        f = f.strip()
        if f.startswith("† (pohřeb)"):
            s["burial"] = s["burial"] or f[len("† (pohřeb)"):].strip()
        elif f.startswith("*") and not s["birth"]:
            s["birth"] = event_text(f[1:])
        elif f.startswith("×"):
            s["marriages"].append(f[1:].strip())
        elif f.startswith("†") and not s["death"]:
            s["death"] = event_text(f[1:])
        elif f.startswith("roz. ") and not s["roz"]:
            s["roz"] = f[5:].strip()
        elif f and not TITLE_ONLY.match(f) and not f.startswith("TÁŽ OSOBA"):
            s["other"].append(f)
    for d in p.get("deti", []):
        ds = structure(d)
        s["kids"].append(dict(name=d["n"], birth=ds["birth"], y=d.get("y") or birth_years(d), home=ds["home"]))
    return s


def birth_years(p):
    for f in p.get("f", []):
        if f.strip().startswith("*"):
            m = re.search(r"\d{4}", f)
            if m:
                return "* " + m.group()
    return ""


def birth_place(p):
    for f in p.get("f", []):
        if f.strip().startswith("*"):
            return split_event(f.strip()[1:])[1]
    return ""


def all_facts(p):
    """Všechny údaje jako seznam textů (pro mapu míst, hledání a kontroly) – nic se nezahodí."""
    out = list(p.get("f", []))
    for key, label in (("roz", "roz. "), ("zam", ""), ("bydl", ""), ("puvod", "původem "), ("pohreb", "pohřeb ")):
        if p.get(key):
            out.append(label + p[key])
    for d in p.get("deti", []):
        out.append(d["n"] + " (" + "; ".join(all_facts(d)) + ")")
    return out


def card(p):
    """Tři řádky pod jménem na kartě ve stromu – vždy ve stejném pořadí:
    roky · povolání · místo (bydliště, jinak místo narození, jinak původ)."""
    place = p.get("bydl") or birth_place(p) or p.get("puvod", "")
    return years(p.get("y") or birth_years(p)), p.get("zam", ""), place
