# Rodokmen Menšíkových

Interaktivní rodinný rodokmen a genealogický archiv rodu Menšíkových, Jarolímových, Holánkových, Henzlových, Čákiových a spřízněných větví.

🌐 **Živý web:** [https://janmensik.github.io/rodokmen/](https://janmensik.github.io/rodokmen/)

---

## 📌 O projektu

Rodokmen vychází od dětí Kryštofa Adama (* 2010), Tey Apoleny (* 2013), Hynka Alberta (* 2015) a Jonáše Alexe (* 2017) a spojuje větev otce Jana Menšíka (* 1980) a matky Julie Menšík Čákiové (* 1979). 

Sleduje předky od pražských akademiků a lékařů přes obuvníky ze Žlebů, železáře, zámečníky a hamerníky ze Starého Ranska až po truhláře a hostinské z Hluboké na pomezí Vysočiny a Železných hor.

### Současný stav výzkumu
- **56** známých osob
- **31** rodin
- **9** generací předků
- **5** hlavních rodových větví
- Matriční zápisy se snímky, výřezy a přepisy originálního kurentu/švabachu

---

## 📁 Struktura projektu

- `data/` – strukturovaná genealogická data (`osoby.py`, `zaznamy.json`, `mista.json`, `svazky.json`, `zajimavosti.md`, `research_log.md`)
- `vyrezy/` – výřezy matričních zápisů se zvýrazněním čtených pasáží a portréty předků
- `zdroje/` – plná rozlišení archivních snímků a rodinných fotografií
- `vystupy/` – tiskové plakáty (vějíř předků 360°, kompletní strom rodiny v SVG/HTML/PNG)
- `tools/` – nástroje v Pythonu (`export_web.py`, `fan_chart.py`, `tree_chart.py`)
- `web/` – moderní statický web postavený na frameworku [Astro](https://astro.build) s vyhledáváním přes [Pagefind](https://pagefind.app) a interaktivní mapou [Leaflet](https://leafletjs.com)

---

## 🚀 Spuštění a správa webu

### Požadavky
- Python 3.9+
- Node.js 18+

### Lokální spuštění
1. Přejděte do složky `web`:
   ```bash
   cd web
   npm install
   ```
2. Generování dat a spuštění vývojového serveru:
   ```bash
   npm run data
   npm run dev
   ```
   Web poběží na adrese `http://localhost:4321/rodokmen/`.

### Sestavení (build)
```bash
npm run build
```
Výsledné statické soubory jsou vygenerovány do `web/dist/`.

---

## ⚙️ Automatické nasazení (GitHub Actions)

Tento repozitář má nakonfigurovaný GitHub Actions workflow (`.github/workflows/deploy.yml`), který při každém `git push` do větve `main`:
1. Zpracuje všechna genealogická data skriptem `tools/export_web.py`.
2. Vygeneruje interaktivní SVG vějíř a strom rodiny.
3. Sestaví web v Astru a indexuje vyhledávání v Pagefindu.
4. Automaticky publikuje výsledný web na **GitHub Pages**.
