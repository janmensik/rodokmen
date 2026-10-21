# Stav rodokmenu a pravidla práce

Tento soubor je vstupní bod. Po každém restartu (nová konverzace, zkrácený kontext) ho Gemini čte jako první,
pak konec `research_log.md` a sekci „Rozpracováno“.

## Pro koho
- Výchozí osoba: **Jan Menšík** (* 7. 1. 1980)
- Kdo s Gemini pracuje a jak chce komunikovat: Jan Menšík (česky, stručně, srozumitelně)

## Kde co je
| Soubor | Obsah |
|---|---|
| `data/osoby.py` | Přímí předci podle Kekulého čísla + rody, boční příbuzní, otevřené otázky, hypotézy. |
| `data/zaznamy.json` | Každý použitý zápis z matriky (klíč = název obrázku). |
| `data/svazky.json` | Matriční svazky (archiv, signatura, odkaz). |
| `data/prepisy.json` | Přepis originálu a český překlad každého zápisu. |
| `data/zvyrazneni.json` | Rámečky – které místo výřezu čteme. |
| `data/research_log.md` | Deník VŠECH hledání, i neúspěšných. |
| `data/udaje_od_rodiny.md` | Co řekla rodina, rodinné dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Co by šlo zjistit jen v archivu. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Mapa, rodinné fotky a dokumenty, nastavení webu. |
| `vyrezy/`, `zdroje/` | Výřezy zápisů pro web (1800 px) a v plném rozlišení. |
| `dokumenty/` | Rodinné dokumenty a fotky od uživatele (originály). |
| `pracovni/` | Pracovní soubory (stažené stránky, kontrolní obrázky) – nejdou na web. |
| `web/` | Rodinný web. `cd web && npm run data && npm run build`, náhled `npm run preview`. |

## Pravidla
1. Než něco ohlásím jako nové, prohledám `osoby.py`, `zaznamy.json` a `research_log.md` (jméno, místo, rok).
2. Údaj je „doloženo“ (doc) jen tehdy, když jsem ho přečetl přímo na snímku. Čtení od pomocníků ověřím sám.
3. Každé hledání (i neúspěšné) zapíšu do `research_log.md`.
4. Nejistá čtení označím (?) – nic nedomýšlím.
5. Ke každému novému zápisu: výřez (`tools/vyrez.py`), rámeček (`tools/ramecek.py`) a přepis s překladem.
6. Po změně dat spustím `python -I -X utf8 tools/kontrola.py` a otestuji `python -I -X utf8 tools/export_web.py`.
7. **Git a živý web (GitHub Pages):** Repozitář je na GitHubu (`https://github.com/janmensik/rodokmen.git`) a web na `https://janmensik.github.io/rodokmen/`. Po každé úpravě (noví předci, matriky, texty, úpravy kódu) proveď Git commit a push do větve `main` (`git push origin main`). GitHub Actions workflow automaticky zaktualizuje web.

## Rozpracováno (aktualizovat průběžně)
- 21. 10. 2026: Doplněno od uživatele pro větev Julie Menšík Čákiové:
  - Otec Miloslava Čákiho: **Juraj (Jiří) Čáki** (* asi 1921, č. 12).
  - Matka Miloslava Čákiho: **Marie Čákiová roz. Bubancová** (č. 13).
  - Otec Evy Čákiové: **Miroslav Krejzek** (1914–1978, č. 14).
  - Matka Evy Čákiové: **Věra Krejzková roz. Černá** (1917–2005, č. 15); její otec **Josef Černý** (č. 30) a 1 bratr.
  - Založeny rody Čákiových a Krejzkových/Černých v `LINES`. Kompletní 3. generace (všech 8 praprarodičů dětí č. 8–15).
- 21. 10. 2026: V matrikách Žlebů (SOA Praha – eBadatelna) ověřeno a doloženo:
  - Úmrtí Jana Jarolíma 1903 (Žleby 35, pag. 666, sn. 337, tuberkulóza, obuvník čp. 37, potvrzuje narození i sňatek v Dolní Krupé).
  - Narození a křest Jana Jarolíma 1863 (Žleby 10, pag. 285, sn. 290, nemanželský syn Barbory Jarolímové; nově odhaleni její rodiče obuvník Josef Jarolím a Kateřina roz. Táborská, otec Kateřiny Josef Táborský).
  - Narození a křest Emilie Jarolímové 1899 (Žleby 32, pag. 25, sn. 29, Žleby čp. 37; nově odhalen pradědeček Ignác Jeřábek, učitel v Čachotíně čp. 15).
  - Do rodokmenu přidáni 4 noví předci (Josef Jarolím č. 170, Kateřina Táborská č. 171, Ignác Jeřábek č. 174 a Josef Táborský č. 342).
- Další krok:
  1. Pokračovat v ověřování matčiny větve:
     - Sňatek Jana Jarolíma a Antonie Havlové (29. 5. 1888 v Dolní Krupé – SOA Zámrsk / ARON).
     - Narození Antonie Havlové (13. 1. 1857 v Dolní Krupé čp. 42 – SOA Zámrsk / ARON).
     - Větev Holánků a Šímů ve Starém Ransku (narození Julia Holánka 1889, Františka Holánka 1854, Julie Šímové 1854 – Krucemburk / ARON).
     - Větev Henzlů a Pospíchalů v Hluboké a Chlumu (Franz Henzl 1872, Aloisie Pospíchalová 1875 – Krucemburk / ARON).
  2. Doplnit od uživatele podrobnosti k otcovské větvi:
     - Dívčí příjmení a rodiče babičky MUDr. Ludmily Menšíkové (č. 9).
     - Farnost v Praze nebo křestní zápis doc. RNDr. Miroslava Menšíka (* 3. 8. 1906 Praha, č. 8).
