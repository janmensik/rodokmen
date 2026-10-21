# Projekt rodokmenu

Tohle je projekt rodokmenu vedený skillem **rodokmen** v aplikaci Antigravity / Gemini. Na začátku každé konverzace:
1. Načti skill `rodokmen` (`SKILL.md`, pokud ještě není načtený).
2. Přečti `data/STAV.md` – stav, pravidla a co je rozpracované – a konec `data/research_log.md`.
3. Pokračuj tam, kde se skončilo. Komunikuj česky, stručně a srozumitelně pro člověka bez zkušeností s genealogií a programováním.
4. Co by šlo ve skillu zlepšit (chyby nástrojů, nové archivy, nápady), zapisuj do `poznamky_pro_skill.md` – viz skill, sekce „Poznámky pro správce skillu“.

## Git repozitář a hosting webu (GitHub Pages)
- **Git repozitář:** `https://github.com/janmensik/rodokmen.git`
- **Živý web:** `https://janmensik.github.io/rodokmen/`
- **Pravidlo pro změny:** Po dokončení jakékoliv práce (přidání předků, ověření zápisů z matrik, nové fotky, úpravy textů nebo kódu webu):
  1. Otestuj export a data: `python -I -X utf8 tools/kontrola.py` a `python -I -X utf8 tools/export_web.py`.
  2. Proveď Git commit s výstižným popisem změn.
  3. Pushni změny do větve `main` (`git push origin main`).
  4. GitHub Actions workflow (`.github/workflows/deploy.yml`) automaticky vygeneruje data, sestaví Astro web a nasadí aktuální verzi na GitHub Pages.

## Technická pravidla prostředí (Windows / Antigravity)
- Python skripty spouštěj vždy přes `python -I -X utf8 tools/<nástroj>.py` (ne `python3`).
- ImageMagick je `magick` (nikdy `convert`).
- Skripty `.sh` spouštěj přes Git Bash (`bash tools/…`).
- Datové soubory zapisuj v UTF-8 bez BOM (přes `write_file` / `edit_file`).
