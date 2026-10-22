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
- 21. 10. 2026: Import předků z GEDCOM (`dokumenty/export-Forest.ged` z Geni.com):
  - Načteno 43 nových předků v 8. až 11. generaci (roky 1630–1780) v liniích Holánek, Sláma, Dymáček, Žundálek, Škoda, Dobrovolný, Chlebeček (stav `mh`).
  - Odhalena nejstarší známá řemesla: mlynář Řehoř Škoda (* 1643), slévač a správce hutě Tomáš Dymáček (* 1664), šafář Jan Žundálek (* 1677), kováři a slévači.
  - V rodokmenu evidováno celkem **100 osob** (z toho 3 doložené zápisy v matrikách).
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
- 21. 10. 2026: V matrikách Dolní Krupé (SOA Zámrsk – ARON) ověřeno a doloženo:
  - Sňatek Jana Jarolíma a Antonie Havlové 29. 5. 1888 v čp. 42 (sign. 5946, pag. 176–177, sn. 102). Jan (24 let, tovaryš obuvnický) a Antonie (31 let, svobodná v čp. 42). Potvrdil zesnulé rodiče: Jana Havla, mistra krejčovského, a Annu roz. Jeřábkovou.
  - Narození a křest Antonie Havlové 13. 1. 1857 v čp. 42 (sign. 2840, pag. 347–348, sn. 206, zápis č. 5). Dcera krejčího Jana Havla a Anny roz. Jeřábkové.
  - Na snímku 245 nalezen též křest bratra Ignáce Havla (* 9. 7. 1864 Dolní Krupá čp. 42).
  - Zápisy nově odhalily a plně doložily další 3 předky v 7. generaci:
    - **Martin Havel** (č. 172, domkař v Dolní Krupé čp. 42, † před 1857).
    - **Magdalena Dolanská** (č. 173, z Dolní Krupé čp. 22, † před 1857).
    - **Josefa Hoffmannová** (č. 175, z Frauenthalu / Pohledu čp. 5, † před 1864), manželka učitele Ignáce Jeřábka (č. 174, který žil v Jiříkově a dožil v Dolní Krupé čp. 42).
  - V rodokmenu evidováno celkem **103 osob** (z toho 5 doložených zápisů ze snímků matrik).
- 22. 10. 2026: Sjednocení datové struktury a zobrazení ve Stromu i profilech:
  - Vytvořen modul `tools/fakta.py` pro jednotné formátování let (`years`), struktury údajů (`structure`), podtitulků karet (`card_subtitle`) a extrakci všech údajů pro vyhledávání a mapu (`all_facts`).
  - Sjednocena data v `data/osoby.py`: životní události v jednotném pořadí (narození `*`, sňatek `×`, úmrtí `†`), povolání (`zam`), bydliště (`bydl`), dívčí příjmení (`roz`), původ (`puvod`) a pohřeb (`pohreb`).
  - Ve stromu (`tree_chart.py` / `tree.svg`) je zobrazení 100% jednotné: na 2. řádku vždy souhrnné roky (bez míchání celých dat narození), na 3. řádku vždy stejné pořadí `Povolání · Místo`.
  - V profilu osoby (`osoba/[slug].astro`) vytvořena přehledná strukturovaná karta životních údajů s jednotným pořadím položek a seznamem dětí.
  - Všechna původní data, místa na mapě i texty zachovány beze ztráty (ověřeno kontrolami a testovacím skriptem).
- 22. 10. 2026: Rozluštěna a plně doložena otcovská linie Menšíků pro doc. RNDr. Miroslava Menšíka (* 3. 8. 1906 Praha):
  - Policejní přihlášky Praha (NAČR, karton 388, sn. 88, Pag. 19n): nalezen originální záznam rodiny c. k. kancisty/poštovního úředníka **Franze Menschika** (* 1873 Jistebnice) a **Pauliny roz. Jirkovské** (* 1882 Praha), s dětmi Franz Paul (* 1901), Wlastimila (* 1902) a **Miroslav (* 1906)**. Uveden sňatek 8. 5. 1902 u Týna a stěhování 15. 8. 1906 do Podskalské (Nové Město čp. 355).
  - V Týnském chrámu v Praze (AHMP, TÝN O12, sn. 60, pag. 56, zápis č. 37) nalezen a přepsán sňatek 8. 5. 1902: **František Menšík** (* 8. 7. 1873 Jistebnice č. 56), c. k. strážník v Praze čp. 12-I, syn Josefa Menšíka, pekaře z Jistebnice č. 56 a Marie roz. Šmedkové; nevěsta **Pavlína Rosalie Jirkovská** (* 2. 11. 1882 Praha I čp. 12), dcera kamnáře Aloise Jirkovského a Aloisie roz. Tiché (dcery mistra krejčího Františka Tichého).
  - V matrice Jistebnice 16 (SOA Třeboň, kniha 4513, sn. 206, pag. 202, zápis č. 74) nalezen a přepsán křest Františka Xavera Menšíka (* 8. 7. 1873 Jistebnice č. 56): syn **Josefa Menšíka**, pekaře v Jistebnici č. 56 (syna Josefa Menšíka, pekaře v Jistebnici č. 156 a Barbory roz. Horychové) a **Marie** (dcery Antonína Šmedly, kostelníka v Jistebnici a Marie roz. Šobelové z Vlasenice).
  - V matrice Jistebnice 22 (SOA Třeboň, kniha 4519, sn. 60, pag. 118–119, zápis č. II) nalezen a přepsán sňatek Josefa Menšíka a Marie Šmedlové (31. 1. 1865): ženich **Josef Menšík** (* 18. 3. 1832 Jistebnice č. 156, pekař), syn pekaře **Josefa Menšíka st.** z čp. 156 (syna řezníka **Františka Menšíka** a **Anny roz. Dvořákové**) a **Barbory roz. Horychové** (dcery zedníka **Františka Horycha** a **Barbory roz. Dědové**); nevěsta **Marie Šmedlová** (* 18. 6. 1835 Jistebnice č. 48), dcera kostelníka **Antonína Šmedly** z čp. 48 (syna punčocháře **Antonína Šmedly st.** a **Anny roz. Kostkové**) a **Františky roz. Šebelové** (dcery správčího **Václava Šebeleho** z Vlasenic a **Apolonie**).
  - Tímto je linie Menšíků doložena o 6 generací zpět až k řezníku Františku Menšíkovi v Jistebnici (konec 18. století).
- 22. 10. 2026: Matrika Jistebnice 12 (SOA Třeboň, kniha 4509 – 1830–1836):
  - **Křest Josefa Menšíka** (* 18. 3. 1832, pokřtěn 20. 3. 1832 v Jistebnici čp. 156; sn. 46, fol. 46, 4. zápis). V oddací matrice 1865 bylo číslo strany chybně opsáno jako 76 namísto fol. 46 (ověřeno v dobovém indexu matriky). Otec Josef Menšík, pekař, syn Faustina [Františka] Menšíka, řezníka v Jistebnici a Anny roz. Dvořákové; matka Barbora, dcera Františka Horycha, zedníka v Jistebnici a Barbory roz. Dědové.
  - **Křest Marie Šmedlové** (* 18. 6. 1835, pokřtěna 18. 6. 1835 v Jistebnici čp. 48; sn. 122, fol. 122, 3. zápis). Přesně odpovídá citaci v oddací matrice. Otec Antonín Šmedla, punčochář v Jistebnici, syn Antonína Šmedly, punčocháře v Jistebnici a Anny roz. Kostkové; matka Františka, dcera Václava Šebeleho, správčího ve Vlasenicích a Apolonie.
- 22. 10. 2026: Matrika Týnského chrámu (AHMP, TÝN N19 – 1878–1893):
  - **Křest Pavlíny Rosalie Jirkovské** (* 2. 11. 1882, pokřtěna 12. 11. 1882 v Praze I čp. 12-I; sn. 77, fol. 67, 2. zápis). Otec Alois Jirkovský, kamnářský dělník v Praze (přiznal se k otcovství před farářem a svědky Janem Jirkovským a Karlem Jelínkem), syn Františka Jirkovského, hrnčíře z Kutné Hory, a Aloisie roz. Franzové z Prahy. Matka Aloisie Tichá, narozená v Praze (u sv. Apolináře), dcera již zemřelého krejčovského mistra v Praze Františka Tichého a zemřelé Anny roz. Svobodové z Prahy.
  - V zápisu zjištěno přesné datum sňatku rodičů: **14. 1. 1883 v Týnském chrámu**.
  - Do rodokmenu nově doplněni a doloženi další 3 předci v 6. generaci: **František Jirkovský** (č. 68), **Aloisie Franzová** (č. 69) a **Anna Svobodová** (č. 71).
  - V rodokmenu evidováno celkem **125 osob** (z toho **12 doložených primárních zápisů** ze snímků matrik ve 12 svazcích).
- Další bezprostřední krok (v malých krocích):
  1. Dohledat sňatek Aloise Jirkovského a Aloisie Tiché (14. 1. 1883) v matrice Týnského chrámu (TÝN O11).
  2. Dohledat sňatek pekaře Josefa Menšíka st. a Barbory Horychové v Jistebnici (kolem 1825–1831).
  3. Zjistit úmrtí Františka Menšíka a Pavlíny Menšíkové v Praze.
