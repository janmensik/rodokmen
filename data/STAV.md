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

  - V zápisu zjištěno datum sňatku rodičů (1885 u Týna).

  - Do rodokmenu nově doplněni a doloženi další 3 předci v 6. generaci: **František Jirkovský** (č. 68), **Aloisie Franzová** (č. 69) a **Anna Svobodová** (č. 71).

- 22. 10. 2026: Kniha oddaných Týnského chrámu (AHMP, TÝN O10 – 1878–1889):

  - **Sňatek Aloise Jirkovského a Aloisie Marie Tiché** (19. 1. 1885 v Týnském chrámu; sn. 140, fol. 130, 2. zápis). Ženich Alois Jirkovský (25 let, * 7. 4. 1859, křtěn u sv. Haštala v Praze), kamnářský dělník v čp. 12-I, syn Františka Jirkovského, hrnčíře v Praze (z Kutné Hory) a Aloisie roz. Franzové z Prahy; nevěsta Aloisie Marie Tichá (26 let, * 12. 7. 1858, křtěna u sv. Apolináře v Praze), dcera Františka Tichého, mistra krejčího v Praze na Novém Městě čp. 501-II (rodilého z Březnice) a Anny roz. Svobodové z Prahy. Svědkové Eduard Zoliwetz a Jan Jirkovský.

  - V rodokmenu evidováno celkem **125 osob** (z toho **13 doložených primárních zápisů** ze snímků matrik ve 13 svazcích).

- 22. 10. 2026: Doplnění od uživatele pro rodinu Julie: babička **MUDr. Věra Krejzková roz. Černá** (č. 15, 1917–2005) byla lékařka (MUDr.) a žila v Žamberku. V Žamberku tak působili jako lékaři oba manželé MUDr. Miroslav Krejzek i MUDr. Věra Krejzková a později i jejich dcera MUDr. Iva Gajdošová.

- 22. 10. 2026: Matrika farnosti Nejsv. Trojice v Podskalí (AHMP, TRP N15 – 1905–1914):

  - **Křest doc. RNDr. Miroslava Menšíka** (* 3. 8. 1906, pokřtěn 9. 8. 1906 v Praze čp. 1717-II jako **Miroslav Vladimír**; sn. 56, pag. 49, zápis č. 89). Otec František Menšík (* 8. 7. 1873 Jistebnice čp. 56), c. k. civilní strážník, syn pekaře Josefa Menšíka a Marie roz. Šmedlové; matka Pavlína roz. Jirkovská (* 2. 11. 1882 Praha čp. 12-I), dcera kamnáře Aloise Jirkovského a Aloisie roz. Tiché. Kmotrem byl dědeček Alois Jirkovský (v zastoupení Františkem Bůžkem).

  - V policejní konskripci doloženi sourozenci doc. Miroslava Menšíka: bratr **František Pavel Menšík** (* 1901 Praha, † v dětství) a sestra **Vlastimila Menšíková** (* 1902 Praha).

  - V rodokmenu evidováno celkem **125 osob** (z toho **14 doložených primárních zápisů** ze snímků matrik ve 14 svazcích, 29 řádků deníku).

- 22. 10. 2026: Matrika farnosti sv. Haštala v Praze (AHMP, HŠ N15 – 1853–1863):

  - **Křest Aloise Jirkovského** (* 7. 4. 1859, pokřtěn 10. 4. 1859 v Praze I čp. 783; sn. 332, pag. 330, zápis č. 1). Otec František Jirkovský, tovaryš hrnčířský z Kutné Hory, manželský syn Václava Jirkovského, patentního invalidy (vysloužilého vojáka) v Čáslavi a Anny roz. Pilzové z Kutné Hory; matka Aloisie, manželská dcera Barbory Franzové, pradleny v Praze.

  - V zápisu odhalen sňatek rodičů 15. 2. 1852 u sv. Františka v Praze.

  - Do rodokmenu nově doloženi a zařazeni 3 předci v 7. generaci: **Václav Jirkovský** (č. 136), **Anna Jirkovská roz. Pilzová** (č. 137) a **Barbora Franzová** (č. 139).

  - V rodokmenu evidováno celkem **128 osob** (z toho **15 doložených primárních zápisů** ze snímků matrik v 15 svazcích, 30 řádků deníku).

- 22. 10. 2026: Matrika farnosti sv. Apolináře v Praze (AHMP, AP N30 – 1858–1859):

  - **Křest Aloisie Marie Tiché** (* 12. 7. 1858, pokřtěna 18. 7. 1858 v Praze II čp. 501; sn. 119, list 116, zápis č. 4, roční č. 1884, přijímací č. 2388). Otec František Tichý, mistr krejčovský v Praze čp. 501/2, rodilý z Březnice, manželský syn Josefa Tichého, vrchnostenského poddaného v Březnici a Anny roz. Satrové (Šatrové) z Koupě u Březnice; matka Anna, manželská dcera Václava Svobody, komisionáře od policie v Praze čp. 501/2 a Anny roz. Schneiderové z N. N.

  - Do rodokmenu nově doloženi a zařazeni 4 předci v 7. generaci: **Josef Tichý** (č. 140), **Anna Tichá roz. Satrová** (č. 141), **Václav Svoboda** (č. 142) a **Anna Svobodová roz. Schneiderová** (č. 143).

  - V rodokmenu evidováno celkem **132 osob** (z toho **16 doložených primárních zápisů** ze snímků matrik v 16 svazcích, 31 řádků deníku).

- 22. 10. 2026: Matrika oddaných farnosti Jistebnice (SOA Třeboň, Jistebnice 20 • 4517 – 1809–1831):

  - **Sňatek Josefa Menšíka st. a Barbory Horychové** (12. 2. 1828 v Jistebnici; sn. 20, fol. 19, zápis č. 8). Ženich Jozef Menssjk (26 let, svobodný, * cca 1801/1806), zdejší měšťan a pekař, bydliště čp. 165 (písařský přesmyk za rodné čp. 156 Menšíků); nevěsta Barbora (26 let, svobodná, * 3. 9. 1801 čp. 136), dcera Františka Horycha, mistra zednického a zdejšího měšťana v čp. 86 a Barbory roz. Dědové. Oddal kurát P. Jan Pavel Kaffka, svědky byli soused Vojtěch Matoušek a mlynář Václav Slavba.

  - V indexech Jistebnice (SOA Třeboň) dohledána další data:

    - Narození nevěsty Barbory Horychové: 3. 9. 1801 v Jistebnici čp. 136 (kniha 4534 sn. 23).

    - Narození ženicha Josefa Menšíka: 13. 7. 1806 v Jistebnici čp. 156 (kniha 4534 sn. 39).

    - Sňatek rodičů nevěsty Františka Horycha a Barbory Dědové: 18. 1. 1791 v Jistebnici čp. 136 (kniha 4537 sn. 11).

    - Sňatek bratra nevěsty Václava Horycha (* 1795) s Marianou Šmedlovou dne 18. 2. 1828 v Jistebnici (čp. 86) – Václav byl později v roce 1865 svědkem na svatbě synovce Josefa Menšíka ml. s Marií Šmedlovou.

  - V rodokmenu evidováno celkem **133 osob** (z toho **17 doložených primárních zápisů** ze snímků matrik v 17 svazcích, 32 řádků deníku).

- 22. 10. 2026: Rodina babičky MUDr. Ludmily Menšíkové roz. Pivničkové (* 1909 Praha – † 2007 Praha):
  - Zjištěn křestní výtah u sv. Apolináře (22. 8. 1909), promoce na LF UK v Praze (1934).
  - V policejních přihláškách a matrikách AHMP nalezen sňatek rodičů 27. 4. 1908 u sv. Jindřicha: **Jan Emanuel Pivnička** (* 1872 Praha), měšťanský učitel na Hradčanech (Pod baštami 277/4) a **Emma Marie Tomíčková** (* 1886 Warta / Stráž nad Ohří), dcera c. k. přednosty stanice Antonína Tomíčka a Anny roz. Halíkové z Lobče.
  - Odhalena rodinná vzpomínka na laskavou „paní Pivničkovou“ z Hradčan a rodinný hrob na Olšanských hřbitovech (006, 7a, 134).
  - Nalezen křest Jana Emanuela Pivničky u sv. Štěpána (1872) a sňatek prarodičů u sv. Jiljí (1869): krejčovský pomocník **Josef Pivnička** (* 1844 Čechtice) a **Antonie roz. Grubnerová** (* 1843 Dobříš).
  - Rozluštěna rodinná tradice o popraveném příbuzném Linhartovi: bratři **Bedřich Linhart** (* 1886, vrchní kriminální inspektor pražské policie, odbojář sítí ÚVOD a Sparta, popraven 20. 10. 1944 na Pankráci) a **Otto Linhart** (* 1895, hlavní radista vysílačky Sparta I) byli vlastní bratranci prababičky Pavlíny Menšíkové roz. Jirkovské (přes tetu Pavlínu Bertu Linhartovou roz. Jirkovskou, provdanou 1883 u Týna za mlynáře Jana Linharta).

- 22. 10. 2026: Průzkum rodiny manželky Julie Menšík Čákiové (dosud nejméně prozkoumaná větev):
  - **Větev MUDr. Miroslava Krejzka (1914–1978, č. 14):**
    - V matrice doktorů Karlovy univerzity (inv. č. 10, pag. 4844, sn. 448) nalezena doktorská promoce MUDr. Miroslava Krejzka dne 23. 6. 1939. Narozen 3. 9. 1914 v Bystřici nad Pernštejnem, maturoval 1933 na reálném gymnáziu v Tišnově.
    - Zjištěni a doloženi rodiče (č. 28 a 29): **Otakar Krejzek**, soukromník v Bystřici nad Pernštejnem, a **Františka Krejzková**.
    - Zrekonstruován profesní a životní příběh: chirurgie prof. Jana Bedrny v Hradci Králové, nemocnice v Nymburce (seznámení s budoucí chotí Věrou Černou z Poděbrad), nákaza TBC v dubnu 1945 od vězňů z transportů smrti z koncentračních táborů, od března 1946 primář a hrudní chirurg v léčebně Albertinum v Žamberku.
  - **Větev MUDr. Věry Krejzkové roz. Černé (1917–2005, č. 15):**
    - V matrice Poděbrady 70 (SOA Praha, sn. 140, fol. 136) nalezen a přepsán sňatek rodičů (14. 6. 1911): **Josef Černý** (25 let, * 16. 2. 1886 Poděbrady č. 15/II, mistr kovářský) a **Marie Měšťánková** (25 let, * 16. 12. 1885 Končice č. 14), dcera Josefa Měšťánka, obchodníka v Poděbradech č. 13/II a Kateřiny roz. Oucké z Končic.
    - V matrice Žiželice 17 (SOA Praha, sn. 237, fol. 246) nalezen a přepsán křest **Marie Měšťánkové** (* 13. 12. 1885 Končice čp. 14). Rodiče: rolník **Josef Měšťánek** (* 1859, syn tkalce Václava Měšťánka a Barbory roz. Kosové z Bojiště) a **Kateřina** (* 1857, dcera Kateřiny Ouzké z Končic).
    - Zápis nese unikátní přípis potvrzující úmrtí **25. 10. 1972 v léčebně TBC v Žamberku (Albertinum)**, kde působila její dcera i zeť!
    - V matrice Poděbrady 64 (SOA Praha, sn. 133, fol. 149) nalezen sňatek prarodičů (20. 7. 1885): mistr kovářský **Jan Černý** (25 let, * 13. 12. 1860 Dobšice č. 27 / Malé Zboží čp. 15, syn kováře Františka Černého a Kateřiny roz. Michlové) a **Anna Hromadová** (21 let, * 29. 6. 1864 Chvalovice č. 4, dcera rolníka Václava Hromady a Anny roz. Kovaříkové).
    - Odhalena nepřetržitá kovářská tradice rodu Černých (Josef Černý * 1886, Jan Černý * 1860, František Černý i Josef Michl z Vlkova).
  - **Prohloubení větví Měšťánek, Ouzký, Hromada a Kovářík (generace 6, 7 a 8):**
    - V matrice Žiželice 19 (SOA Praha, sn. 131, fol. 144) nalezen a přepsán sňatek (3. 4. 1883 Končice čp. 71): **Josef Měšťánek** (* cca 1859, mistr tesařský z Končic čp. 14, syn tesaře a tkalce Václava Měšťánka a Barbory roz. Kosa z Bojiště čp. 10) a **Kateřina Ouzká** (* cca 1857, nemanželská dcera Kateřiny Ouzké, dcery domkaře Jiřího Ouzkého z Končic čp. 14 a Barbory roz. Daníčkové z Končic čp. 12).
    - V matrice Kovanice 10 (SOA Praha, sn. 161, pag. 159) nalezen a přepsán křest **Anny Hromadové** (* 29. 6. 1864 Chvalovice čp. 21). Rodiče: rolník **Václav Hromada** (syn † Václava Hromady st., rolníka z Vyšehořovic čp. 22 na Českobrodsku a Alžběty roz. Jirkovské z čp. 25) a **Anna** (dcera Josefa Kováříka, výminkáře v Chvalovicích čp. 21 a Anny roz. Homolové z Chrástu na Českobrodsku).
    - Do rodokmenu nově doloženo a doplněno 16 předků Julie v 6., 7. a 8. generaci:
      - 6. generace: František Černý (č. 120), Kateřina Michlová (č. 121), Václav Hromada (č. 122), Anna Kováříková (č. 123), Václav Měšťánek (č. 124), Barbora Kosová (č. 125), Kateřina Ouzká st. (č. 127).
      - 7. generace: kovář Josef Michl (č. 242), Václav Hromada st. (č. 244), Alžběta Jirkovská (č. 245), Josef Kovářík (č. 246), Anna Homolová (č. 247), Václav Kos (č. 250), Jiří Ouzký (č. 254), Barbora Daníčková (č. 255).
      - 8. generace: Jiří Daníček (č. 510).
  - V rodokmenu celkem evidováno **165 osob** (z toho **27 doložených primárních zápisů** ze snímků matrik ve 26 svazcích, 44 řádků deníku).

- 24. 10. 2026: Zavedení lokálního modelu Ollama (qwen2.5:7b) a sepsání kroniky rodu:
  - Zprovozněno lokální generování textů přes Ollama (qwen2.5:7b při rychlosti cca 24–27 tokenů/s).
  - Vytvořen a na web zapracován soubor data/pribeh.md (5 rozsáhlých kapitol mapujících všechny hlavní rodové linie):
    1. Pekaři Menšíkovi z Jistebnice a cesta do Prahy
    2. Pražský odboj, vysílačka Sparta a hrdinové Linhartovi
    3. Tři generace mistrů kovářských z Dobšic a Poděbrad
    4. Lékařská sága v podorlickém Albertinu v Žamberku
    5. Železářská huť ve Starém Ransku a mlynáři z Čáslavska
  - Do data/zajimavosti.md přidány 3 nové kapitoly (kovářská svatba 211 dní před narozením syna, legitimace Pavlíny Jirkovské 809 dní po narození, dlouhověkost v Albertinu).
  - Do data/archivni_dotazy.md vypracovány detailní badatelské plány pro slovenskou větev (farnost Dúbrava) a moravský původ Otakara Krejzka (sčítání lidu 1921).

- 26. 10. 2026: Nálezy a ověření v matrikách SOA Praha (Kovanice a Nebovidy):
  - **Sňatek Václava Hromady a Anny Kováříkové (12. 4. 1853):** Matrika Kovanice 08 (sn. 102, pag. 100, 2. zápis). Gruntovník Václav Hromada (20 1/2 let, * 31. 8. 1832) z Chvalovic čp. 21, syn † Václava Hromady z Vyšehořovic čp. 22 a Alžběty roz. Jirkovské z čp. 25; nevěsta Anna Kováříková (21 1/2 let, * 1831), dcera Josefa Kováříka, výminkáře v Chvalovicích čp. 21 a Anny roz. Homolové z Chrástu. Povolení c. k. okresního soudu v Českém Brodě z 30. 3. 1853 č. 1967.
  - **Křest Josefa Měšťánka (16. 1. 1859):** Matrika Nebovidy 11 (sn. 32, pag. 59, 1. zápis). Narozen v Bojišti čp. 10 jako syn tovaryše tesařského Václava Měšťánka a Barbory roz. Kosové. Odhaleni noví předci v 7. generaci: † Antonín Měšťánek, nádeník ze Dvorů čp. 2, Barbora roz. Šafáříková z Peček, a Marie Kosová roz. Kollářová z Peček čp. 55.
  - **Sňatek Václava Měšťánka a Barbory Kosové (4. 10. 1858):** Matrika Nebovidy 18 (sn. 10, pag. 15, 2. zápis). Ženich Václav Měšťánek (28 let, * cca 1830), záložník c. k. 6. pluku polního dělostřelectva, nevěsta Barbora Kosová (23 let, * cca 1835) z Bojiště čp. 10. Vojenské povolení z Pešti č. 3724 po ohláškách v Uhrách v Karos-Keresztúr. Syn Josef se narodil pouhých 104 dní po svatbě.
  - Do rodokmenu nově doloženi 3 noví předci v 7. generaci: **Antonín Měšťánek** (č. 248), **Barbora Šafáříková** (č. 249), **Marie Kollářová** (č. 251).
  - V rodokmenu celkem evidováno **168 osob** (z toho **30 doložených primárních zápisů** ze snímků matrik ve 29 svazcích, 47 řádků deníku).
  - Do `data/zajimavosti.md` přidány 2 nové příběhy vytvořené a zrevidované za pomoci lokálního modelu Ollama (dělostřelecký záložník a svatba 104 dní před porodem, dvacetiletý hospodář Hromada).

- 26. 10. 2026: Nálezy a ověření kovářské dynastie Černých (Žehuň / ARON Lužec nad Cidlinou):
  - **Křest mistra kovářského Jana Nepomuka Černého (12. 3. 1860):** Matrika Žehuň 04 (SOA Praha, sn. 257, pag. 288, 2. zápis r. 1860 pro Dobšice). Narozen i pokřtěn 12. 3. 1860 v Dobšicích čp. 27 jako syn kováře Františka Černého a Kateřiny roz. Michlové. Vyřešena záhada data narození: v poděbradské oddací matrice z roku 1885 bylo chybně uvedeno 13. 12. 1860, ale v žehuňské křestní matrice je autentický přípis *„List křestní k ženění 18 3/7 85“* dokazující vydání křestního listu 3. 7. 1885 pro svatbu v Poděbradech (písař zaměnil 3. a 12. měsíc).
  - **Sňatek kováře Františka Černého a Kateřiny Michlové (21. 1. 1856):** Matrika Lužec nad Cidlinou sign. 95-10 (SOA Zámrsk / ARON, APU `334cfeb8-253f-4a93-9b98-77035ed3a3c6`, sn. 83, pag. 161–162, 1. zápis r. 1856 pro Vlkov). Oddáni 21. 1. 1856 ve Vlkově čp. 13; šestadvacetiletý kovář František Černý (* cca 1829 Dobšice čp. 27) a sedmnáctiletá Kateřina Michlová (* cca 1838 Vlkov čp. 13), dcera † mistra kovářského Josefa Michla z Vlkova čp. 13 a Anny roz. Fialové z Lužan čp. 19. Svatba doložena vrchnoporučenským povolením č. 25 ze 4. 1. 1856.
  - **Odhalena pětigenerační kovářská dynastie po meči i po přeslici:** Kovářské řemeslo provozovali Václav Černý (Dobšice čp. 27), František Černý (Dobšice čp. 27 / Malé Zboží čp. 15), Jan Černý (Malé Zboží / Poděbrady) a Josef Černý (Poděbrady na Zámostí čp. 15/II, kování lázeňských fiakrů a kočárů), podpořené kovářskými předky z mateřských linií: Jan Šiška (kovář v Žiželicích čp. 119) a Josef Michl (kovář ve Vlkově čp. 13).
  - Do rodokmenu nově doloženi 3 noví předci v 7. generaci: **Václav Černý** (č. 240), **Anna Šišková** (č. 241), **Anna Fialová** (č. 243).
  - **Křest a oprava data narození Kateřiny Ouzké ml. (11. 4. 1862):** Matrika Žiželice 07 (SOA Praha, sn. 131, pag. 161, 3. zápis r. 1862 pro Končice). Narozena 11. 4. 1862 v Končicích čp. 14 (pokřtěna 13. 4. 1862) jako nemanželská dcera svobodné matky Kateřiny Ouzké (dcery † Jiřího Ouzkého, baráčníka z Končic čp. 14 a Barbory roz. Daníčkové z čp. 12). V oddacím zápise z 3. 4. 1883 byl její věk chybně zapsán jako 26 let (* cca 1857), ve skutečnosti se však vdávala ve věku nedožitých 21 let (proto potřebovala vrchnoporučenské svolení soudu v Chlumci n. C.). Křestní matrika obsahuje nezvratný okrajový přípis: *„List křestní k oddavkám vydán dne 29. března 1883 čj. 2868“* přesně 5 dní před svatbou!
  - V rodokmenu celkem evidováno **171 osob** (z toho **33 doložených primárních zápisů** ze snímků matrik ve 32 svazcích, 50 řádků deníku).
  - Do `data/zajimavosti.md` přidány 2 nové kapitoly (Kovářská dynastie pěti generací, Záhada březnového data narození kováře Jana Černého) vytvořené a zrevidované s využitím modelu Ollama qwen2.5:7b.

- Další kroky k prozkoumání:
  1. Křest Kateřiny Ouzké ml. (* cca 1857, nemanželská dcera Kateřiny Ouzké st. z Končic čp. 14).
  2. Slovenská řeckokatolická větev Čáki a Bubanec (farnost Dúbrava, okres Snina na Zemplíně – matriky na FamilySearch).
  3. Sňatek Otakara Krejzka a Františky (kolem 1905–1913 na Moravě mimo Bystřici n. P.).
  4. Starší generace kovářů Černých v Dobšicích a Malém Zboží (farnost Žehuň).
