# Přímí předci podle Kekulého čísel: 1 = výchozí osoby (děti Kryštof a Tea Menšíkovi),

# otec osoby n má číslo 2n (2 = Jan Menšík), matka 2n+1 (3 = Julie Menšík Čákiová),

# 4–7 prarodiče dětí (rodiče Jana a Julie), 8–15 praprarodiče dětí (prarodiče Jana a Julie)…

#

# JEDNOTNÁ STRUKTURA OSOBY (stejná u předků v P i u bočních příbuzných ve SIDE → "vetev"; popis v tools/fakta.py):

#   n      jméno (tituly patří sem, ne do faktů)

#   y      jen roky: "* 1895", "1890–1944", "asi 1720–1785", "1857 – po 1914", "† před 1888"; plná data patří do f

#   f      události v pořadí  "* datum místo"  →  "× datum místo manžel/ka"  →  "† datum místo",

#          pak ostatní volné údaje (čí syn/dcera, poznámky)

#   roz    rodné příjmení      zam    povolání / postavení      bydl   bydliště

#   puvod  odkud pochází       pohreb místo pohřbu              vztah  (boční příbuzní) vztah k linii

#   st, r, note  stav, klíče zápisů, poznámka



P = {

    # 0. generace – děti Jana a Julie

    1: dict(n="Kryštof, Tea, Hynek a Jonáš Menšíkovi", y="* 2010, * 2013, * 2015, * 2017", st="fam", sex="M",

            f=[], bydl="Libčice nad Vltavou",

            deti=[dict(n="Kryštof Adam Menšík", y="* 2010", f=["* 20. 3. 2010 Praha"], bydl="Libčice nad Vltavou"),

                  dict(n="Tea Apolena Menšíková", y="* 2013", f=["* 14. 2. 2013 Praha"], bydl="Libčice nad Vltavou"),

                  dict(n="Hynek Albert Menšík", y="* 2015", f=["* 10. 7. 2015 Praha"], bydl="Libčice nad Vltavou"),

                  dict(n="Jonáš Alex Menšík", y="* 2017", f=["* 5. 12. 2017 Praha"], bydl="Libčice nad Vltavou")],

            r=[], note="Čtyři děti Jana a Julie, narozené v Praze, žijící v Libčicích nad Vltavou."),



    # 1. generace – rodiče (Jan a manželka Julie)

    2: dict(n="Mgr. Jan Menšík", y="* 1980", st="fam",

            f=["* 7. 1. 1980 Praha", "× 12. 9. 2009 Zvíkov Mgr. Julie Menšík Čákiová"],

            zam="právník", bydl="Libčice nad Vltavou (od roku 2009)", r=[],

            note="Výchozí osoba rodokmenu, manžel Mgr. Julie Menšík Čákiové (sňatek 12. 9. 2009 Zvíkov). Vystudoval Právnickou fakultu Univerzity Karlovy v Praze (Mgr.), dříve Gymnázium Buďánka a SŠ Nad Štolou. Od roku 2009 žije v Libčicích nad Vltavou."),

    3: dict(n="Mgr. Julie Menšík Čákiová", y="* 1979", st="fam",

            f=["* 22. 5. 1979 Praha", "× 12. 9. 2009 Zvíkov Mgr. Jan Menšík"],

            roz="Čákiová", bydl="Libčice nad Vltavou (od roku 2009)", r=[],

            note="Mgr., roz. Čákiová, manželka Mgr. Jana Menšíka (sňatek 12. 9. 2009 Zvíkov). Narozena v Praze, od roku 2009 žije v Libčicích nad Vltavou."),



    # 2. generace – prarodiče dětí (rodiče Jana a rodiče Julie)

    4: dict(n="Ing. Radim Jaroslav Menšík", y="1946–2021", st="fam",

            f=["* 13. 9. 1946 Praha", "× asi 1972 Praha Ing. Zdeňka Jarolímová", "† 15. 1. 2021 Praha", "pohřben 27. 1. 2021 Praha"],

            zam="inženýr", r=[], note="Ing. Radim Jaroslav Menšík, otec Jana a Jakuba Menšíkových. Syn doc. RNDr. Miroslava Menšíka a MUDr. Ludmily Menšíkové. Narozen v Praze, sňatek s Ing. Zdeňkou Jarolímovou kolem roku 1972 v Praze."),

    5: dict(n="Ing. Zdeňka Menšíková", y="* 1949", st="fam",

            f=["* 6. 5. 1949", "× asi 1972 Praha Ing. Radim Jaroslav Menšík"],

            roz="Jarolímová", zam="inženýrka dopravy (GŘ ČD, MDČR)", bydl="Praha 6 (Pod Beránkou)", r=[],

            note="Ing., roz. Jarolímová, matka Jana a Jakuba Menšíkových. Dcera Richarda Jarolíma (1927–2012) a Zdenky roz. Holánkové (* 1928). Působila na Ministerstvu dopravy a na Českých drahách. Žijící v Praze 6."),

    6: dict(n="JUDr. Miloslav Čáki", y="* 1947", st="fam",

            f=["* 1. 6. 1947 Vlčice (u Trutnova)", "× PhDr. Eva Krejzková"],

            zam="právník (JUDr., Ministerstvo financí ČR)", bydl="Praha 4 - Háje (Hviezdoslavova); v dětství Červeněves čp. 88", r=[],

            note="Právník (JUDr.), působil na Ministerstvu financí ČR, manžel PhDr. Evy Čákiové. Narozen ve Vlčicích u Trutnova, dětství prožil v Červeněvsi čp. 88 (syn Juraje Čákiho a Marie roz. Bubancové ze Slovenska)."),

    7: dict(n="PhDr. Eva Čákiová", y="* 1946", st="fam",

            f=["* 1. 11. 1946 Rychnov nad Kněžnou", "× JUDr. Miloslav Čáki"],

            roz="Krejzková", bydl="Praha 4 - Háje (Hviezdoslavova), Vrabsko; v dětství Žamberk", r=[],

            note="PhDr., roz. Krejzková, manželka JUDr. Miloslava Čákiho, dcera MUDr. Miroslava Krejzka a MUDr. Věry roz. Černé. Narozena v Rychnově nad Kněžnou, dětství prožila v Žamberku."),



    # 3. generace – praprarodiče dětí / prarodiče Jana a Julie (8–13)

    8: dict(n="doc. RNDr. Miroslav Vladimír Menšík", y="1906–1968", st="doc",

            f=["* 3. 8. 1906 Praha (křest u Nejsv. Trojice v Podskalí)", "× MUDr. Ludmila Menšíková", "† 12. 1. 1968 Praha"],

            zam="docent deskriptivní geometrie a fotogrammetrie na Stavební fakultě ČVUT; vedoucí redaktor Rozhledů matematicko-fyzikálních (1956–1968)",

            r=["podskali_krest_miroslav_mensik_1906"], note="Matematik, vysokoškolský docent deskriptivní geometrie a fotogrammetrie na Stavební fakultě ČVUT, autor učebnic a vědeckých prací. Narozen 3. 8. 1906 v Praze na Novém Městě čp. 1717 (pokřtěn 9. 8. 1906 u Nejsv. Trojice v Podskalí jako Miroslav Vladimír). Syn Františka Menšíka (* 1873 Jistebnice) a Pavlíny roz. Jirkovské (* 1882 Praha). Z matčiny strany byli jeho bratranci z druhého kolena slavní bratři Linhartové – hrdinové protinacistického odboje v čele s Bedřichem Linhartem (popraveným 1944 na Pankráci) a radiotelegrafistou vysílačky Sparta I Otto Linhartem."),

    9: dict(n="MUDr. Ludmila Menšíková", y="1909–2007", st="doc",
            f=["* 22. 8. 1909 Praha (křest u sv. Apolináře)",
               "× 1. asi 1935 MUDr. Pech",
               "× 2. 1940–1942 doc. RNDr. Miroslav Menšík",
               "† 2007 Praha", "pohřbena Olšanské hřbitovy (část 006, odd. 7a, hrob 134)"],
            roz="Pivničková", zam="dětská lékařka (pediatr)",
            bydl="Praha 6 - Hradčany (Pod baštami 277/4), dříve Dejvice (Vítězné nám. 1)",
            r=["jindrich_oddani_jan_pivnicka_1908"],
            note="MUDr. Ludmila Menšíková, roz. Pivničková, poprvé provdaná Pechová. Dětská lékařka v Praze, manželka doc. RNDr. Miroslava Menšíka, matka Radima a Ivana Menšíkových. Narozena 22. 8. 1909 v Praze (dle křestního výtahu u sv. Apolináře), dcera učitele měšťanské školy na Hradčanech Jana Emanuela Pivničky a Emmy Marie roz. Tomíčkové. V roce 1928 maturovala na reálném gymnáziu v Bubenči, v roce 1934 promovala na Lékařské fakultě UK v Praze (MUDr.). Působila v Krči, Nemocnici Německý Brod, Plzni a v Dejvicích. Zemřela v roce 2007 a je pohřbena v rodinném hrobě na Olšanech spolu se svou matkou Emmou Pivničkovou. V rodinné paměti se uchoval tragický odkaz příbuzného jménem Linhart, popraveného za války v Praze – jednalo se o Bedřicha Linharta (* 1886, popraven 20. 10. 1944 na Pankráci), bratrance její tchyně Pavlíny Menšíkové roz. Jirkovské."),

    10: dict(n="Richard Jarolím", y="1927–2012", st="fam",

             f=["* 26. 3. 1927 Žleby čp. 17", "× 30. 10. 1948 Rumburk Zdenka Holánková", "† 24. 3. 2012 Hradec Králové"],

             bydl="Hradec Králové",

             r=[], note="Dědeček Jana z matčiny strany. S manželkou Zdenkou žili v Hradci Králové. Narozen ve Žlebech čp. 17, zemřel v Hradci Králové."),

    11: dict(n="Zdenka Jarolímová", y="* 1928", st="fam",

             f=["* 20. 11. 1928 Hluboká čp. 36", "× 30. 10. 1948 Rumburk Richard Jarolím"],

             roz="Holánková", bydl="Hradec Králové",

             r=[], note="Babička Jana z matčiny strany, rozená Holánková. S manželem Richardem Jarolímem žili v Hradci Králové. Narozena v Hluboké čp. 36."),

    12: dict(n="Juraj (Jiří) Čáki", y="* asi 1921", st="fam",

             f=["* asi 1921 Slovensko (Dúbrava / Šmigovec, okres Snina)", "× Marie Bubancová",

                "příjmení v matrikách: Čáki / Čaky / Csáky"],

             puvod="Zemplín (Dúbrava / Šmigovec)", bydl="Červeněves čp. 88", r=[],

             note="Otec JUDr. Miloslava Čákiho (uváděn též jako Jiří Čáki / Čaky). Pocházel z východního Slovenska (Dúbrava nebo Šmigovec, okres Snina, Zemplín), žil v Červeněvsi čp. 88. Měl bratra Miroslava Čákyho."),

    13: dict(n="Marie Čákiová", y="", st="fam",

             f=["× Juraj (Jiří) Čáki"],

             roz="Bubancová", puvod="Zemplín (Šmigovec / Dúbrava, okres Snina)", r=[],

             note="Matka JUDr. Miloslava Čákiho. Rozená Bubancová, původem z východního Slovenska (Šmigovec nebo Dúbrava, okres Snina, Zemplín)."),

    14: dict(n="MUDr. Miroslav Krejzek", y="1914–1978", st="fam",

             f=["* 3. 9. 1914 Bystřice nad Pernštejnem", "× Věra Černá", "† 27. 5. 1978 Žamberk",

                "vystudoval medicínu v Brně", "měl 5 bratrů"],

             zam="lékař (MUDr.)", bydl="Žamberk", r=[],

             note="Lékař (MUDr.), manžel MUDr. Věry roz. Černé, otec PhDr. Evy Čákiové a MUDr. Ivy Gajdošové (dědeček Julie). Narozen v Bystřici nad Pernštejnem, vystudoval medicínu v Brně, měl 5 bratrů, působil a zemřel v Žamberku."),

    15: dict(n="MUDr. Věra Krejzková", y="1917–2005", st="fam",

             f=["* 8. 2. 1917 Poděbrady", "× Miroslav Krejzek", "† 7. 11. 2005 Žamberk"],

             zam="lékařka (MUDr.)", bydl="Žamberk",

             roz="Černá", r=[],

             note="Lékařka (MUDr.) v Žamberku, manželka MUDr. Miroslava Krejzka, matka PhDr. Evy Čákiové a MUDr. Ivy Gajdošové (babička Julie), dcera Josefa Černého."),



    # 4. generace – pradědečci a prababičky (16–23, 30)

    16: dict(n="František Xaver Menšík", y="* 1873", st="doc",

             f=["* 8. 7. 1873 Jistebnice čp. 56", "× 8. 5. 1902 Praha (Týnský chrám) Pavlína Rosalie Jirkovská"],

             zam="c. k. policejní strážník v Praze, poštovní úředník / kancista",

             bydl="Praha I čp. 12 (1902), Staré Město čp. 78, Nové Město čp. 355",

             puvod="Jistebnice č. 56",

             r=["tyn_oddani_frantisek_mensik_1902", "jistebnice_krest_frantisek_mensik_1873"],

             note="Narozen 8. 7. 1873 v Jistebnici čp. 56 jako manželský syn pekaře Josefa Menšíka a Marie roz. Šmedlové. Dne 8. 5. 1902 oddán u Týna s Pavlínou Jirkovskou."),

    17: dict(n="Pavlína Rosalie Menšíková", y="* 1882", st="doc",

             f=["* 2. 11. 1882 Praha I čp. 12", "× 8. 5. 1902 Praha (Týnský chrám) František Menšík"],

             roz="Jirkovská", bydl="Praha I čp. 12", puvod="Praha",

             r=["tyn_krest_pavlina_jirkovska_1882", "tyn_oddani_frantisek_mensik_1902"],

             note="Narozena 2. 11. 1882 v Praze I čp. 12 (pokřtěna 12. 11. 1882 v Týnském chrámu). Dcera kamnáře Aloise Jirkovského a Aloisie roz. Tiché. Dne 8. 5. 1902 oddána u Týna s Františkem Menšíkem. Její kmotrou při křtu byla teta Pavlína Berta Linhartová roz. Jirkovská (* 1854), jejíž synové (vlastní bratranci Pavlíny) Bedřich, Zdeněk, Václav a Otto Linhartovi vytvořili jednu z nejstatečnějších rodin protinacistického odboje (vysílačka Sparta I, Obrana národa, Tři králové); Bedřich Linhart byl v říjnu 1944 popraven v pražské sekyrárně na Pankráci."),
    18: dict(n="Jan Emanuel Pivnička", y="1872 – po 1921", st="doc",
             f=["* 14. 1. 1872 Praha Nové Město čp. 1356 (křest u sv. Štěpána)",
                "× 27. 4. 1908 Praha (kostel sv. Jindřicha) Emma Marie Tomíčková",
                "vystoupil z církve 15. 2. 1921 (Magistrát čj. 3738 C)"],
             zam="definitivní učitel měšťanské chlapecké školy na Hradčanech (dříve u Panny Marie Sněžné)",
             bydl="Praha IV - Hradčany čp. 277 (Pod baštami 4), dříve Malá Strana čp. 196 a 623",
             puvod="Praha Nové Město",
             r=["stepan_krest_jan_pivnicka_1872", "jindrich_oddani_jan_pivnicka_1908"],
             note="Definitivní učitel měšťanské chlapecké školy na Hradčanech. Narozen 14. 1. 1872 v Praze na Novém Městě čp. 1356 (pokřtěn 21. 1. 1872 u sv. Štěpána). Syn mistra krejčovského Josefa Pivničky (rodem z Čechtic) a Antonie roz. Grubnerové z Dobříše. Dne 27. 4. 1908 oddán u sv. Jindřicha s Emmou Marií Tomíčkovou. V roce 1921 vystoupil z církve římskokatolické."),
    19: dict(n="Emma Marie Pivničková", y="1886–?", st="doc",
             f=["* 7. 4. 1886 Warta čp. 59 (Stráž nad Ohří)",
                "× 27. 4. 1908 Praha (kostel sv. Jindřicha) Jan Emanuel Pivnička",
                "pohřbena Olšanské hřbitovy (část 006, odd. 7a, hrob 134)"],
             roz="Tomíčková", bydl="Praha IV - Hradčany čp. 277, dříve Kamenné Žehrovice čp. 164",
             puvod="Warta (Stráž nad Ohří u Hauenštejnu, okres Kadaň)",
             r=["jindrich_oddani_jan_pivnicka_1908"],
             note="Manželka Jana Emanuela Pivničky a matka MUDr. Ludmily Menšíkové. Narozena 7. 4. 1886 ve Wartě čp. 59 (dnes Stráž nad Ohří u hradu Hauenštejn, okres Kadaň). Dcera c. k. železničního přednosty stanice Hauenstein-Warta Antonína Tomíčka a Anny roz. Halíkové z Lobče čp. 63. Pohřbena v rodinném hrobě na Olšanech spolu s dcerou Ludmilou. V rodině Jana Menšíka je pamatována jako „paní Pivničková“ (babička otce Ing. Radima Menšíka), u níž rodina na Hradčanech (Pod baštami 277/4) pobývala."),



    # Pokračování 4. generace (20–23, 30)

    20: dict(n="Fridrich Hůlek", y="", st="fam",

             f=[], zam="lesní inženýr", r=[],

             note="Údaje z rodinného stromu PDF (datum a místo narození zatím neuvedeny; syn Richard nesl příjmení matky Jarolím)."),

    21: dict(n="Emilie Jarolímová", y="1899 – po 1927", st="doc",

             f=["* 15. 4. 1899 Žleby čp. 37", "† po 1927"],

             zam="dělnice",

             r=["zleby_krest_emilie_jarolimova_1899"],

             note="Křest doložen v matrice Žleby 32 (pag. 25, sn. 29). Na okraji poznámka o sňatku 20. 3. 1937 s Rudolfem Kaňourem (?)"),

    22: dict(n="Julius Holánek", y="1889–1952", st="fam",

             f=["* 20. 7. 1889 Staré Ransko čp. 55", "× 20. 5. 1926 Sofia Henzlová", "† 1952"],

             zam="zámečník", r=[],

             note="Údaje z rodinného stromu PDF a MyHeritage CSV."),

    23: dict(n="Sofia Henzlová", y="1904–1985", st="fam",

             f=["* 8. 5. 1904 Hluboká čp. 38", "× 20. 5. 1926 Julius Holánek", "† 1985"], r=[],

             note="Údaje z rodinného stromu PDF a MyHeritage CSV (psána též Sofia Henzl)."),

    30: dict(n="Josef Černý", y="", st="fam",

             f=[], r=[],

             note="Otec Věry Krejzkové roz. Černé (pradědeček Julie). Měl syna (bratra Věry). Údaj od rodiny."),



    # 5. generace – praprarodiče (32–35, 42–47)

    32: dict(n="Josef Menšík", y="* 1832", st="doc",

             f=["* 18. 3. 1832 Jistebnice čp. 156", "× 31. 1. 1865 Jistebnice Marie Šmedlová"],

             zam="pekař v Jistebnici čp. 156 a 56", puvod="Jistebnice",

             r=["jistebnice_krest_josef_mensik_1832", "jistebnice_krest_frantisek_mensik_1873", "jistebnice_oddani_josef_mensik_1865"],

             note="Mistr pekařský v Jistebnici čp. 156 a 56. Narozen 18. 3. 1832 v Jistebnici čp. 156 (pokřtěn 20. 3. 1832 kaplanem P. Fabriciem Dvořákem). Syn pekaře Josefa Menšíka a Barbory roz. Horychové. Oddán 31. 1. 1865 v Jistebnici s Marií Šmedlovou."),

    33: dict(n="Marie Menšíková", y="* 1835", st="doc",

             f=["* 18. 6. 1835 Jistebnice čp. 48", "× 31. 1. 1865 Jistebnice Josef Menšík"],

             roz="Šmedlová", puvod="Jistebnice",

             r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_krest_frantisek_mensik_1873", "jistebnice_oddani_josef_mensik_1865"],

             note="Narozena i pokřtěna 18. 6. 1835 v Jistebnici čp. 48. Dcera Antonína Šmedly, punčocháře a pozdějšího kostelníka v Jistebnici čp. 48, a Františky roz. Šebelové z Vlasenic."),

    34: dict(n="Alois Jirkovský", y="* 1859", st="doc",

             f=["* 7. 4. 1859 Praha (křest u sv. Haštala)", "× 19. 1. 1885 Praha (Týnský chrám) Aloisie Marie Tichá"],

             zam="kamnář v Praze", bydl="Praha I čp. 12",

             r=["hastal_krest_alois_jirkovsky_1859", "tyn_oddani_alois_jirkovsky_1885", "tyn_krest_pavlina_jirkovska_1882", "tyn_oddani_frantisek_mensik_1902"],

             note="Kamnářský dělník a kamnář v Praze na Starém Městě čp. 12. Narozen 7. 4. 1859 v Praze (pokřtěn ve farnosti sv. Haštala). Syn Františka Jirkovského, hrnčířského tovaryše v Praze (rodilého z Kutné Hory) a Aloisie roz. Franzové z Prahy. Oddán 19. 1. 1885 u Týna s Aloisií Marií Tichou. Jeho sestra Pavlína Berta Jirkovská (* 1854) se v roce 1883 provdala za mlynářského Jana Linharta a stala se matkou odbojářů bratří Linhartových."),

    35: dict(n="Aloisie Marie Jirkovská", y="* 1858", st="doc",

             f=["* 12. 7. 1858 Praha Nové Město čp. 501 (křest u sv. Apolináře)", "× 19. 1. 1885 Praha (Týnský chrám) Alois Jirkovský"],

             roz="Tichá", bydl="Praha I čp. 12", puvod="Březnice",

             r=["apolinar_krest_aloisie_ticha_1858", "tyn_oddani_alois_jirkovsky_1885", "tyn_krest_pavlina_jirkovska_1882", "tyn_oddani_frantisek_mensik_1902"],

             note="Narozena 12. 7. 1858 v Praze na Novém Městě čp. 501, pokřtěna 18. 7. 1858 u sv. Apolináře, příslušná do Březnice. Dcera mistra krejčího Františka Tichého v Praze (rodilého z Březnice) a Anny roz. Svobodové z Prahy. Manželka kamnáře Aloise Jirkovského a matka Pavlíny Rosalie Menšíkové."),
    36: dict(n="Josef Pivnička", y="* 1844", st="doc",
             f=["* 10. 3. 1844 Čechtice",
                "× 3. 10. 1869 Praha (kostel sv. Jiljí) Antonie Grubnerová"],
             zam="mistr krejčovský v Praze na Novém Městě čp. 1356-II",
             bydl="Praha Nové Město čp. 1356, dříve Staré Město čp. 326",
             puvod="Čechtice (okres Dolní Kralovice / Ledeč nad Sázavou)",
             r=["jilji_oddani_josef_pivnicka_1869", "stepan_krest_jan_pivnicka_1872"],
             note="Mistr krejčí v Praze. Narozen 10. 3. 1844 v Čechticích. Syn souseda a provazníka v Čechticích Josefa Pivničky a Josefy roz. Boháčkové. Dne 3. 10. 1869 oddán u sv. Jiljí na Starém Městě s Antonií Grubnerovou z Dobříše."),
    37: dict(n="Antonie Pivničková", y="* 1843", st="doc",
             f=["* 6. 2. 1843 Dobříš",
                "× 3. 10. 1869 Praha (kostel sv. Jiljí) Josef Pivnička"],
             roz="Grubnerová", bydl="Praha Nové Město čp. 1356", puvod="Dobříš (okres Příbram)",
             r=["jilji_oddani_josef_pivnicka_1869", "stepan_krest_jan_pivnicka_1872"],
             note="Manželka mistra krejčího Josefa Pivničky. Narozena 6. 2. 1843 v Dobříši. Dcera dobříšského mistra krejčovského Antonína Grubnera a Barbory roz. Filoridové."),
    38: dict(n="Antonín Tomíček", y="† před 1908", st="doc",
             f=["× Anna Halíková", "† před 1908"],
             zam="c. k. železniční přednosta stanice Hauenstein-Warta (Buštěhradská dráha)",
             bydl="Warta čp. 59 (Stráž nad Ohří)", puvod="Čechy",
             r=["jindrich_oddani_jan_pivnicka_1908"],
             note="C. k. železniční přednosta nádraží Hauenstein-Warta (dnes Stráž nad Ohří na trati Chomutov–Cheb bývalé Buštěhradské dráhy) ve Wartě čp. 59. Manžel Anny roz. Halíkové a otec Emmy Marie Pivničkové."),
    39: dict(n="Anna Tomíčková", y="† před 1908", st="doc",
             f=["* Lobeč čp. 63", "× Antonín Tomíček", "† před 1908"],
             roz="Halíková", bydl="Warta čp. 59", puvod="Lobeč čp. 63 (okres Slaný / Mšeno)",
             r=["jindrich_oddani_jan_pivnicka_1908"],
             note="Manželka c. k. přednosty stanice Antonína Tomíčka a matka Emmy Marie Pivničkové. Pocházela z Lobče čp. 63."),

    42: dict(n="Jan Jarolím", y="1863–1903", st="doc",

             f=["* 4. 6. 1863 Žleby čp. 126", "× 29. 5. 1888 Dolní Krupá Antonie Havlová", "† 31. 7. 1903 Žleby čp. 37"],

             zam="obuvník", bydl="Žleby čp. 37",

             r=["krupa_oddani_jan_jarolim_1888", "zleby_umrti_jan_jarolim_1903", "zleby_krest_jan_jarolim_1863", "zleby_krest_emilie_jarolimova_1899"],

             note="Křest (Žleby 10, pag. 285, sn. 290), sňatek (Dolní Krupá 5946, sn. 102) i úmrtí na tuberkulózu (Žleby 35, pag. 666, sn. 337) doloženy přímo ze snímků matrik."),

    43: dict(n="Antonie Havlová", y="1857 – po 1914", st="doc",

             f=["* 13. 1. 1857 Dolní Krupá čp. 42", "× 29. 5. 1888 Dolní Krupá Jan Jarolím", "† po 1914"],

             r=["krupa_krest_antonie_havlova_1857", "krupa_oddani_jan_jarolim_1888", "zleby_krest_emilie_jarolimova_1899", "zleby_umrti_jan_jarolim_1903"],

             note="Narození v Dolní Krupé čp. 42 (sign. 2840, sn. 206) i sňatek 29. 5. 1888 (sign. 5946, sn. 102) doloženy ze snímků matrik SOA Zámrsk. Dcera mistra krejčovského Jana Havla a Anny roz. Jeřábkové."),

    44: dict(n="František Holánek", y="1854 – po 1896", st="doc",

             f=["* 4. 8. 1854 Staré Ransko čp. 53", "× Julie Šímová", "† po 1896"],

             zam="zámečník",

             r=["ransko_krest_frantisek_holanek_1854"],

             note="Narození ve Starém Ransku čp. 53 doloženo přímo z matriky SOA Zámrsk / ARON (sign. 711, sn. 188, pag. 185). Pokřtěn 4. 8. 1854. Zámečník ve Starém Ransku."),

    45: dict(n="Julie Šímová", y="1854 – po 1896", st="fam",

             f=["* 16. 3. 1854 Staré Ransko čp. 46", "× František Holánek", "† po 1896"], r=[],

             note="Údaje z rodinného stromu PDF a MyHeritage CSV."),

    46: dict(n="Franz Henzl", y="1872–1954", st="fam",

             f=["* 12. 7. 1872 Hluboká čp. 15", "× Aloisie Pospíchalová", "† 15. 2. 1954 Havlíčkův Brod čp. 539"],

             zam="truhlář a hostinský", r=[],

             note="Údaje z rodinného stromu PDF."),

    47: dict(n="Aloisie Pospíchalová", y="1875–1957", st="fam",

             f=["* 6. 1. 1875 Chlum čp. 35", "× Franz Henzl", "† 1957"], r=[],

             note="Údaje z rodinného stromu PDF."),



    # 6. generace (64–70, 84–93)

    64: dict(n="Josef Menšík st.", y="* cca 1801/1806", st="doc",

             f=["* 13. 7. 1806 Jistebnice čp. 156", "× 12. 2. 1828 Jistebnice Barbora Horychová"],

             zam="měšťan a pekař v Jistebnici čp. 156", puvod="Jistebnice",

             r=["jistebnice_krest_josef_mensik_1832", "jistebnice_oddani_josef_mensik_1828", "jistebnice_oddani_josef_mensik_1865"],

             note="Měšťan a mistr pekařský v Jistebnici čp. 156, syn řezníka Františka Menšíka (v matrice 1832 zapsán Faustin) a Anny roz. Dvořákové. Narozen 13. 7. 1806 v čp. 156. Oddán 12. 2. 1828 v Jistebnici s Barborou Horychovou (v oddací matrice zapsán ve věku 26 let, bydliště čp. 165)."),

    65: dict(n="Barbora Menšíková", y="* 1801", st="doc",

             f=["* 3. 9. 1801 Jistebnice čp. 136", "× 12. 2. 1828 Jistebnice Josef Menšík"],

             roz="Horychová", puvod="Jistebnice",

             r=["jistebnice_krest_josef_mensik_1832", "jistebnice_oddani_josef_mensik_1828", "jistebnice_oddani_josef_mensik_1865"],

             note="Narozena 3. 9. 1801 v Jistebnici čp. 136. Dcera Františka Horycha, mistra zednického a měšťana v Jistebnici (čp. 136 a 86), a Barbory roz. Dědové. Oddána 12. 2. 1828 v Jistebnici (z čp. 86, věk 26 let) s pekařem Josefem Menšíkem."),

    66: dict(n="Antonín Šmedla", y="", st="doc",

             f=["× Františka Šebelová"],

             zam="punčochář, později kostelník v Jistebnici čp. 48 / 73", puvod="Jistebnice",

             r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_oddani_josef_mensik_1865"],

             note="Punčochář a později kostelník v Jistebnici, syn Antonína Šmedly, punčocháře z Jistebnice, a Anny roz. Kostkové."),

    67: dict(n="Františka Šmedlová", y="", st="doc",

             f=["× Antonín Šmedla"],

             roz="Šebelová", puvod="Vlasenice",

             r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_oddani_josef_mensik_1865"],

             note="Dcera Václava Šebeleho, správčího ve Vlasenicích, a jeho choti Apolonie."),

    68: dict(n="František Jirkovský", y="† před 1882", st="doc",

             f=["× 15. 2. 1852 Praha (sv. František) Aloisie Franzová", "† před 2. 11. 1882"],

             zam="hrnčířský tovaryš a kamnář v Praze", puvod="Kutná Hora", bydl="Praha I čp. 783",

             r=["hastal_krest_alois_jirkovsky_1859", "tyn_oddani_alois_jirkovsky_1885", "tyn_krest_pavlina_jirkovska_1882"],

             note="Hrnčířský tovaryš v Praze, rodilý z Kutné Hory. Syn Václava Jirkovského, patentního invalidy v Čáslavi, a Anny roz. Pilzové z Kutné Hory. Oddán 15. 2. 1852 u sv. Františka v Praze s Aloisií Franzovou. K listopadu 1882 již zemřelý."),

    69: dict(n="Aloisie Jirkovská", y="", st="doc",

             f=["× 15. 2. 1852 Praha (sv. František) František Jirkovský"],

             roz="Franzová", puvod="Praha", bydl="Praha I čp. 783",

             r=["hastal_krest_alois_jirkovsky_1859", "tyn_oddani_alois_jirkovsky_1885", "tyn_krest_pavlina_jirkovska_1882"],

             note="Manželka hrnčířského tovaryše Františka Jirkovského v Praze, rozená Franzová z Prahy (dcera Barbory Franzové, pradleny v Praze). Oddána 15. 2. 1852 u sv. Františka. Matka kamnáře Aloise Jirkovského."),

    70: dict(n="František Tichý", y="† před 1882", st="doc",

             f=["× Anna Svobodová", "† před 2. 11. 1882"],

             zam="mistr krejčovský v Praze čp. 501-II", puvod="Březnice", bydl="Praha Nové Město čp. 501-II",

             r=["apolinar_krest_aloisie_ticha_1858", "tyn_oddani_alois_jirkovsky_1885", "tyn_krest_pavlina_jirkovska_1882", "tyn_oddani_frantisek_mensik_1902"],

             note="Mistr krejčovský v Praze na Novém Městě čp. 501-II, rodilý z Březnice. Syn Josefa Tichého, vrchnostenského poddaného v Březnici, a Anny roz. Satrové (Šatrové) z Koupě. Manžel Anny roz. Svobodové a otec Aloisie Marie Jirkovské roz. Tiché. K listopadu 1882 již zemřelý."),

    71: dict(n="Anna Tichá", y="† před 1882", st="doc",

             f=["× František Tichý", "† před 2. 11. 1882"],

             roz="Svobodová", puvod="Praha", bydl="Praha Nové Město čp. 501-II / Březnice",

             r=["apolinar_krest_aloisie_ticha_1858", "tyn_oddani_alois_jirkovsky_1885", "tyn_krest_pavlina_jirkovska_1882"],

             note="Manželka mistra krejčího Františka Tichého v Praze, rozená Svobodová z Prahy. Dcera Václava Svobody, policejního komisionáře v Praze čp. 501-II, a Anny roz. Schneiderové. K listopadu 1882 již zemřelá."),
    72: dict(n="Josef Pivnička", y="", st="doc",
             f=["× Josefa (Barbora) Boháčková", "† před 1872"],
             zam="soused a provazník v Čechticích", puvod="Čechtice",
             r=["stepan_krest_jan_pivnicka_1872", "jilji_oddani_josef_pivnicka_1869"],
             note="Soused a mistr provaznický v Čechticích (okres Dolní Kralovice / Ledeč nad Sázavou). Otec mistra krejčovského Josefa Pivničky (* 1844)."),
    73: dict(n="Josefa Pivničková", y="", st="doc",
             f=["× Josef Pivnička"],
             roz="Boháčková", puvod="Čechtice",
             r=["stepan_krest_jan_pivnicka_1872", "jilji_oddani_josef_pivnicka_1869"],
             note="Manželka čechtického souseda a provazníka Josefa Pivničky a matka Josefa Pivničky (* 1844). V matrice oddaných z r. 1869 psána Josefa roz. Boháčková, v matrice narozených z r. 1872 Barbora roz. Boháčková."),
    74: dict(n="Antonín Grubner", y="", st="doc",
             f=["× Barbora Filoridová"],
             zam="mistr krejčovský v Dobříši", puvod="Dobříš",
             r=["jilji_oddani_josef_pivnicka_1869", "stepan_krest_jan_pivnicka_1872"],
             note="Mistr krejčovský v Dobříši (okres Příbram). Otec Antonie Pivničkové roz. Grubnerové (* 1843)."),
    75: dict(n="Barbora Grubnerová", y="", st="doc",
             f=["× Antonín Grubner"],
             roz="Filoridová", puvod="Dobříš",
             r=["jilji_oddani_josef_pivnicka_1869", "stepan_krest_jan_pivnicka_1872"],
             note="Manželka dobříšského mistra krejčovského Antonína Grubnera a matka Antonie Pivničkové roz. Grubnerové (* 1843). Příjmení psáno též Filoridy / Tilorády."),

    84: dict(n="otec neuveden", y="", st="unk",

             f=[], r=["zleby_krest_jan_jarolim_1863"], note="Jan Jarolím (* 1863) byl nemanželským synem Barbory Jarolímové; otec v křestní matrice Žlebů neuveden (kolonka otce prázdná)."),

    85: dict(n="Barbora Jarolímová", y="† před 1888", st="doc",

             f=["† před 29. 5. 1888", "dcera obuvníka Josefa Jarolíma a Kateřiny Táborské"],

             bydl="Žleby čp. 126",

             r=["krupa_oddani_jan_jarolim_1888", "zleby_krest_jan_jarolim_1863", "zleby_krest_emilie_jarolimova_1899"],

             note="Doložena v křestních zápisech syna Jana i vnučky Emilie ve Žlebech; v oddacím zápise syna Jana (1888) uvedena jako již zesnulá."),

    86: dict(n="Jan Havel", y="† před 1888", st="doc",

             f=["× Anna Jeřábková", "† před 29. 5. 1888", "syn Martina Havla a Magdaleny Dolanské"],

             zam="mistr krejčovský", bydl="Dolní Krupá čp. 42",

             r=["krupa_krest_antonie_havlova_1857", "krupa_oddani_jan_jarolim_1888", "zleby_krest_emilie_jarolimova_1899"],

             note="Mistr krejčovský v Dolní Krupé čp. 42. Syn domkaře Martina Havla z Dolní Krupé čp. 42 a Magdaleny roz. Dolanské z čp. 22. Doložen v křtu dcery Antonie (1857) i vnučky Emilie (1899); k 1888 již zesnulý."),

    87: dict(n="Anna Jeřábková", y="† před 1888", st="doc",

             f=["× Jan Havel", "† před 29. 5. 1888", "dcera učitele Ignáce Jeřábka a Josefy Hoffmannové"],

             bydl="Čachotín čp. 15",

             r=["krupa_krest_antonie_havlova_1857", "krupa_oddani_jan_jarolim_1888", "zleby_krest_emilie_jarolimova_1899"],

             note="Dcera učitele Ignáce Jeřábka a Josefy roz. Hoffmannové z Frauenthalu (Pohledu) čp. 5. Doložena v křtu dcery Antonie (1857), oddavkách (1888) i křtu vnučky Emilie (1899)."),

    88: dict(n="Jan Holánek", y="* 1820", st="doc",

             f=["* 18. 6. 1820 Staré Ransko čp. 45", "× Johanna Hlaváčková",

                "syn mistra kovářského Josefa Holánka a Barbory Slámové"],

             zam="domkař", bydl="Staré Ransko čp. 53",

             r=["ransko_krest_frantisek_holanek_1854"],

             note="Domkař ve Starém Ransku čp. 53. Doložen v křestní matrice syna Františka (* 1854, sign. 711, sn. 188), kde je uveden jako manželský syn již zesnulého kovářského mistra Josefa Holánka ze Starého Ranska čp. 53 a Barbory roz. Slámové ze Starého Ranska čp. 33."),

    89: dict(n="Johanna Hlaváčková", y="", st="doc",

             f=["× Jan Holánek", "dcera mistra zámečnického Vojtěcha Hlaváčka a Barbory Haislerové"],

             bydl="Staré Ransko čp. 49",

             r=["ransko_krest_frantisek_holanek_1854"],

             note="Doložena v křestní matrice syna Františka (* 1854, sign. 711, sn. 188). Manželská dcera zámečnického mistra Vojtěcha Hlaváčka ze Starého Ranska čp. 49 a Barbory roz. Haislerové z Hamrů čp. 9 (u Hlinska)."),

    90: dict(n="Matěj Šíma", y="", st="fam",

             f=["× Františka Benová"],

             zam="horník / horolezec", bydl="Staré Ransko čp. 2", r=[],

             note="Údaje z rodinného stromu PDF (v PDF uvedeno 'horolezec' – ověřit v matrice, zda nešlo o horníka / havíře v železárnách v Ransku)."),

    91: dict(n="Františka Benová", y="", st="fam",

             f=["× Matěj Šíma"], bydl="Staré Ransko čp. 41", r=[], note="Údaje z rodinného stromu PDF."),

    92: dict(n="Václav Henzl", y="* 1844", st="fam",

             f=["* 6. 8. 1844 Hluboká čp. 15", "× Marie Procházková"],

             zam="čtvrtláník", r=[],

             note="Údaje z rodinného stromu PDF."),

    93: dict(n="Marie Procházková", y="", st="fam",

             f=["× Václav Henzl"], bydl="Hluboká čp. 7", r=[], note="Údaje z rodinného stromu PDF."),



    # 7. generace (128–135, 170–185)

    128: dict(n="František Menšík", y="", st="doc",

              f=["× Anna Dvořáková"],

              zam="řezník v Jistebnici", puvod="Jistebnice",

              r=["jistebnice_krest_josef_mensik_1832", "jistebnice_oddani_josef_mensik_1865"],

              note="Řezník v Jistebnici, otec pekaře Josefa Menšíka z čp. 156. V křtu syna Josefa 1832 zapsán Faustin Menšík, v oddací matrice 1865 František."),

    129: dict(n="Anna Menšíková", y="", st="doc",

              f=["× František Menšík"],

              roz="Dvořáková", puvod="Jistebnice",

              r=["jistebnice_krest_josef_mensik_1832", "jistebnice_oddani_josef_mensik_1865"],

              note="Manželka řezníka Františka Menšíka z Jistebnice."),

    130: dict(n="František Horych", y="", st="doc",

              f=["× 18. 1. 1791 Jistebnice Barbora Dědová"],

              zam="mistr zednický a měšťan v Jistebnici", puvod="Jistebnice",

              r=["jistebnice_krest_josef_mensik_1832", "jistebnice_oddani_josef_mensik_1828", "jistebnice_oddani_josef_mensik_1865"],

              note="Mistr zednický a měšťan v Jistebnici (čp. 136 a 86), otec Barbory Menšíkové roz. Horychové. Oddán 18. 1. 1791 v Jistebnici s Barborou Dědovou."),

    131: dict(n="Barbora Horychová", y="", st="doc",

              f=["× 18. 1. 1791 Jistebnice František Horych"],

              roz="Dědová", puvod="Jistebnice",

              r=["jistebnice_krest_josef_mensik_1832", "jistebnice_oddani_josef_mensik_1828", "jistebnice_oddani_josef_mensik_1865"],

              note="Manželka zednického mistra Františka Horycha z Jistebnice, rozená Dědová. Oddána 18. 1. 1791 v Jistebnici."),

    132: dict(n="Antonín Šmedla st.", y="", st="doc",

              f=["× Anna Kostková"],

              zam="punčochář v Jistebnici", puvod="Jistebnice",

              r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_oddani_josef_mensik_1865"],

              note="Punčochář v Jistebnici, otec kostelníka Antonína Šmedly."),

    133: dict(n="Anna Šmedlová", y="", st="doc",

              f=["× Antonín Šmedla"],

              roz="Kostková", puvod="Jistebnice",

              r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_oddani_josef_mensik_1865"],

              note="Manželka punčocháře Antonína Šmedly z Jistebnice, rozená Kostková."),

    134: dict(n="Václav Šebele", y="", st="doc",

              f=["× Apolonie Šebelová"],

              zam="správčí ve Vlasenicích", puvod="Vlasenice",

              r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_oddani_josef_mensik_1865"],

              note="Správčí ve Vlasenicích, otec Františky Šmedlové roz. Šebelové."),

    135: dict(n="Apolonie Šebelová", y="", st="doc",

              f=["× Václav Šebele"],

              puvod="Vlasenice",

              r=["jistebnice_krest_marie_smedlova_1835", "jistebnice_oddani_josef_mensik_1865"],

              note="Manželka správčího Václava Šebeleho ve Vlasenicích."),

    136: dict(n="Václav Jirkovský", y="", st="doc",

              f=["× Anna Pilzová"],

              zam="patentinvalida (vysloužilý voják) v Čáslavi", puvod="Kutná Hora", bydl="Čáslav",

              r=["hastal_krest_alois_jirkovsky_1859"],

              note="Patentinvalida v Čáslavi, původem z Kutné Hory. Otec hrnčířského tovaryše Františka Jirkovského v Praze."),

    137: dict(n="Anna Jirkovská", y="", st="doc",

              f=["× Václav Jirkovský"],

              roz="Pilzová", puvod="Kutná Hora",

              r=["hastal_krest_alois_jirkovsky_1859"],

              note="Manželka Václava Jirkovského, rozená Pilzová (Pílcová) z Kutné Hory. Matka Františka Jirkovského."),

    139: dict(n="Barbora Franzová", y="", st="doc",

              f=[], zam="pradlena v Praze", puvod="Praha", bydl="Praha",

              r=["hastal_krest_alois_jirkovsky_1859"],

              note="Pradlena v Praze, matka Aloisie Jirkovské roz. Franzové."),

    140: dict(n="Josef Tichý", y="", st="doc",

              f=["× Anna Satrová"],

              zam="vrchnostenský poddaný v Březnici", puvod="Březnice", bydl="Březnice",

              r=["apolinar_krest_aloisie_ticha_1858"],

              note="Vrchnostenský poddaný v Březnici, otec pražského mistra krejčovského Františka Tichého."),

    141: dict(n="Anna Tichá", y="", st="doc",

              f=["× Josef Tichý"],

              roz="Satrová", puvod="Koupě", bydl="Březnice / Koupě",

              r=["apolinar_krest_aloisie_ticha_1858"],

              note="Manželka Josefa Tichého, rozená Satrová (Šatrová) z Koupě u Březnice. Matka Františka Tichého."),

    142: dict(n="Václav Svoboda", y="", st="doc",

              f=["× Anna Schneiderová"],

              zam="komisionář od policie v Praze", puvod="Praha", bydl="Praha Nové Město čp. 501-II",

              r=["apolinar_krest_aloisie_ticha_1858"],

              note="Komisionář od policie v Praze na Novém Městě čp. 501-II. Otec Anny Tiché roz. Svobodové."),

    143: dict(n="Anna Svobodová", y="", st="doc",

              f=["× Václav Svoboda"],

              roz="Schneiderová", puvod="Praha", bydl="Praha Nové Město čp. 501-II",

              r=["apolinar_krest_aloisie_ticha_1858"],

              note="Manželka pražského policejního komisionáře Václava Svobody, rozená Schneiderová. Matka Anny Tiché roz. Svobodové."),

    170: dict(n="Josef Jarolím", y="", st="doc",

              f=["× Kateřina Táborská"],

              zam="obuvník", bydl="Žleby čp. 126",

              r=["zleby_krest_jan_jarolim_1863", "zleby_krest_emilie_jarolimova_1899"],

              note="Otec Barbory Jarolímové, obuvník ve Žlebech čp. 126; doložen v křestních zápisech dcery, vnuka Jana i pravnučky Emilie."),

    171: dict(n="Kateřina Táborská", y="", st="doc",

              f=["× Josef Jarolím", "dcera Josefa Táborského"],

              bydl="Žleby čp. 7 / čp. 126",

              r=["zleby_krest_jan_jarolim_1863", "zleby_krest_emilie_jarolimova_1899"],

              note="Matka Barbory Jarolímové, dcera Josefa Táborského ze Žlebů."),

    172: dict(n="Martin Havel", y="† před 1857", st="doc",

              f=["× Magdalena Dolanská", "† před 13. 1. 1857"],

              zam="domkař", bydl="Dolní Krupá čp. 42",

              r=["krupa_krest_antonie_havlova_1857", "krupa_oddani_jan_jarolim_1888"],

              note="Domkař v Dolní Krupé čp. 42, otec mistra krejčovského Jana Havla. Doložen v křestní matrice vnučky Antonie."),

    173: dict(n="Magdalena Dolanská", y="† před 1857", st="doc",

              f=["× Martin Havel", "† před 13. 1. 1857"],

              bydl="Dolní Krupá čp. 22",

              r=["krupa_krest_antonie_havlova_1857", "krupa_oddani_jan_jarolim_1888"],

              note="Matka krejčího Jana Havla, rodem z Dolní Krupé čp. 22. Doložena v křestní matrice vnučky Antonie."),

    174: dict(n="Ignác Jeřábek", y="† po 1864", st="doc",

              f=["× Josefa Hoffmannová", "† po 1864"],

              zam="učitel", bydl="Čachotín čp. 15, Jiříkov čp. 4 a Dolní Krupá čp. 42",

              r=["krupa_krest_antonie_havlova_1857", "krupa_oddani_jan_jarolim_1888", "zleby_krest_emilie_jarolimova_1899"],

              note="Učitel v Čachotíně čp. 15, k roku 1857 žil v Jiříkově čp. 4, k roku 1864 na odpočinku v Dolní Krupé čp. 42. Otec Anny Jeřábkové. Doložen v křestních matrikách dcery i vnuček."),

    175: dict(n="Josefa Hoffmannová", y="† před 1864", st="doc",

              f=["× Ignác Jeřábek", "† před 9. 7. 1864"],

              bydl="Frauenthal (Pohled) čp. 5",

              r=["krupa_krest_antonie_havlova_1857"],

              note="Manželka učitele Ignáce Jeřábka, rodem z Frauenthalu (Pohledu) čp. 5. Matka Anny Jeřábkové. Doložena v křestní matrice dcery Antonie."),

    176: dict(n="Josef Holánek", y="† před 1854", st="doc",

              f=["× Barbora Slámová", "† před 4. 8. 1854"],

              zam="mistr kovářský", bydl="Staré Ransko čp. 53",

              r=["ransko_krest_frantisek_holanek_1854"],

              note="Mistr kovářský ve Starém Ransku čp. 53. Doložen v křestní matrice vnuka Františka (* 1854), kde je uveden jako již zesnulý mistr kovářský. Manželka Barbora roz. Slámová z čp. 33."),

    177: dict(n="Barbora Slámová", y="", st="doc",

              f=["× Josef Holánek"],

              bydl="Staré Ransko čp. 33",

              r=["ransko_krest_frantisek_holanek_1854"],

              note="V rodinném stromu PDF byla uvedena s křestním jménem Filipina; v křestní matrice vnuka Františka (* 1854) je však jednoznačně doložena jako Barbora rozená Sláma ze Starého Ranska čp. 33."),

    178: dict(n="Vojtěch Hlaváček", y="", st="doc",

              f=["× Barbora Haislerová"],

              zam="mistr zámečnický", bydl="Staré Ransko čp. 49",

              r=["ransko_krest_frantisek_holanek_1854"],

              note="Mistr zámečnický ve Starém Ransku čp. 49 (v rodinném stromu PDF byl chybně označen za uhlíře). Doložen v křestní matrice vnuka Františka Holánka (* 1854)."),

    179: dict(n="Barbora Haislerová", y="", st="doc",

              f=["× Vojtěch Hlaváček"],

              bydl="Hamry čp. 9 (panství Hlinecké)",

              r=["ransko_krest_frantisek_holanek_1854"],

              note="Pocházela z Hamrů čp. 9 na hlineckém panství (panství Hlinsko, Chrudimský kraj). Doložena v křestním zápise vnuka Františka Holánka (* 1854)."),

    180: dict(n="Tomáš Šíma", y="", st="fam",

              f=["× Marie Halíková"], zam="dráb", bydl="Staré Ransko čp. 2", r=[], note="Údaje z rodinného stromu PDF."),

    181: dict(n="Marie Halíková", y="", st="fam",

              f=["× Tomáš Šíma"], bydl="Olešná (Volešná)", r=[], note="Údaje z rodinného stromu PDF."),

    182: dict(n="František Ben", y="", st="fam",

              f=["× Karolina Králíčková"], zam="hamernický mistr", bydl="Staré Ransko čp. 41", r=[], note="Údaje z rodinného stromu PDF."),

    183: dict(n="Karolina Králíčková", y="", st="fam",

              f=["× František Ben"], bydl="Česká Kamenice", r=[], note="Údaje z rodinného stromu PDF."),

    184: dict(n="Jan Henzl", y="† před 1872", st="fam",

              f=["× Anna Nováková", "† před 1872"], zam="kovář a zámečník", bydl="Hluboká čp. 15", r=[], note="Údaje z rodinného stromu PDF."),

    185: dict(n="Anna Nováková", y="", st="fam",

              f=["× Jan Henzl"], bydl="Chlumětín", r=[], note="Údaje z rodinného stromu PDF (psána Anna Nowak)."),



    # 8. generace (342–363)

    342: dict(n="Josef Táborský", y="", st="doc",

              f=[], bydl="Žleby čp. 7 / čp. 126",

              r=["zleby_krest_jan_jarolim_1863", "zleby_krest_emilie_jarolimova_1899"],

              note="Otec Kateřiny Táborské ze Žlebů; doložen v křestních zápisech vnuka Jana a pravnučky Emilie Jarolímových."),

    352: dict(n="František Holánek", y="", st="fam",

              f=[], bydl="Křižanov", r=[], note="Údaje z rodinného stromu PDF."),

    354: dict(n="Jan Sláma", y="", st="fam",

              f=["× Alžběta Dymáčková"], zam="tesař", bydl="Staré Ransko čp. 33", r=[], note="Údaje z rodinného stromu PDF."),

    355: dict(n="Alžběta Dymáčková", y="", st="fam",

              f=["× Jan Sláma"], r=[], note="Údaje z rodinného stromu PDF."),

    358: dict(n="Josef Haisler", y="", st="fam",

              f=[], bydl="Františkodol (Fraunsthal)", r=[], note="Údaje z rodinného stromu PDF."),

    360: dict(n="Vojtěch Šíma", y="", st="fam",

              f=[], bydl="Staré Ransko", r=[], note="Údaje z rodinného stromu PDF."),

    362: dict(n="Ondřej Halík", y="", st="fam",

              f=["× Kateřina Dušková"], r=[], note="Údaje z rodinného stromu PDF."),

    363: dict(n="Kateřina Dušková", y="", st="fam",

              f=["× Ondřej Halík"], r=[], note="Údaje z rodinného stromu PDF."),

    # 8. generace – doplněno z GEDCOM (353)

    353: dict(n='Mariana Žundálková', y='1764–1802', st='mh',

             f=['* 13. 8. 1764 Kundratice', '× 1. 2. 1791 Křižanov 37 František Holánek', '† 19. 10. 1802 Křižanov 37'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),



    # 9. generace (704–711)

    704: dict(n='Václav Holánek', y='1726–1787', st='mh',

             f=['* 23. 9. 1726 Křižanov', '× 10. 11. 1754 Křižanov Judita Holánková', '† 23. 11. 1787 Křižanov 37'],

             zam='kovář', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    705: dict(n='Judita Holánková', y='1734–1809', st='mh',

             f=['* 19. 10. 1734 Jívoví', '× 10. 11. 1754 Křižanov Václav Holánek', '† 18. 3. 1809 Křižanov 37'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    706: dict(n='Matěj Žundálek', y='1735–1800', st='mh',

             f=['* 2. 2. 1735', '× asi 1755 Alžběta Žundálková', '† 2. 4. 1800'],

             zam='sedlák', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    707: dict(n='Alžběta Žundálková', y='1738–1806', st='mh',

             f=['* 1738', '× asi 1755 Matěj Žundálek', '† 13. 5. 1806 Kundratice 24'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    708: dict(n='Jan Sláma', y='1715–1772', st='mh',

             f=['* 30. 3. 1715', '× 2. 2. 1744 Sopoty Rozálie Pokorná', '† 19. 6. 1772 Sopoty 12'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    709: dict(n='Rozálie Pokorná', y='1722–1773', st='mh',

             f=['* 1722', '× 2. 2. 1744 Sopoty Jan Sláma', '† 8. 4. 1773 Sopoty 12'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    710: dict(n='Karel Dymáček', y='1718–1772', st='mh',

             f=['* 11. 7. 1718 Ransko', '× 17. 9. 1752 Ransko Anna Dobrovolná', '† 6. 5. 1772 Ransko 9'],

             zam='slévač', pohreb='Krucemburk, sv. Mikuláš', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    711: dict(n='Anna Dobrovolná', y='1728–1780', st='mh',

             f=['* 1. 7. 1728', '× 17. 9. 1752 Ransko Karel Dymáček', '† 1780'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),



    # 10. generace (1408–1423)

    1408: dict(n='Vít Holánek', y='1680–1756', st='mh',

             f=['* asi 1680', '× 22. 7. 1720 Mariana Vodičková Škodová', '† 24. 5. 1756'],

             zam='kovář', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1409: dict(n='Mariana Vodičková Škodová', y='1681–1742', st='mh',

             f=['* 19. 5. 1681', '× 22. 7. 1720 Vít Holánek', '† 9. 7. 1742'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1410: dict(n='Josef Holánek', y='1701–1789', st='mh',

             f=['* 13. 3. 1701', '× 10. 2. 1726 Jívoví a Kundratice Barbora Havelková', '† 30. 7. 1789 Jívoví 1'],

             zam='sedlák', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1411: dict(n='Barbora Havelková', y='1704–1783', st='mh',

             f=['* 4. 12. 1704', '× 10. 2. 1726 Jívoví a Kundratice Josef Holánek', '† 19. 2. 1783 Jívoví 1'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1412: dict(n='Antonín Žundálek', y='1710–1750', st='mh',

             f=['* asi 1710', '× 24. 2. 1734 Margareta Cziczálková', '† asi 1750'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1413: dict(n='Margareta Cziczálková', y='1711–1741', st='mh',

             f=['* 15. 6. 1711', '× 24. 2. 1734 Antonín Žundálek', '† 30. 10. 1741'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1416: dict(n='Josef Sláma', y='1672–1732', st='mh',

             f=['* 1672', '× 18. 12. 1703 Alžběta Dymáčková', '† 4. 10. 1732 Sopoty'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1417: dict(n='Alžběta Dymáčková', y='1683–1751', st='mh',

             f=['* 1683', '× 18. 12. 1703 Josef Sláma', '† 14. 9. 1751 Sopoty'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1418: dict(n='František Pokorný', y='1700–1744', st='mh',

             f=['* asi 1700', '† asi 1744'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1420: dict(n='Tobiáš Dymáček', y='1686–1762', st='mh',

             f=['* 13. 6. 1686 Sobiňovská huť', '× 8. 11. 1711 Mariana Chlebečková', '† 2. 6. 1762 Ransko'],

             pohreb='Krucemburk, sv. Mikuláš', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1421: dict(n='Mariana Chlebečková', y='1694–1748', st='mh',

             f=['* 25. 8. 1694 Sobíňov', '× 8. 11. 1711 Tobiáš Dymáček', '† 26. 1. 1748 Ransko'],

             pohreb='Krucemburk, sv. Mikuláš', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1422: dict(n='Martin Dobrovolný', y='1697–1773', st='mh',

             f=['* 11. 11. 1697', '× 28. 1. 1725 Apolena Zrzavá', '† 5. 1. 1773 Krucemburk 102'],

             zam='sedlák', pohreb='Krucemburk, sv. Mikuláš', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    1423: dict(n='Apolena Zrzavá', y='1704–1763', st='mh',

             f=['* 11. 3. 1704', '× 28. 1. 1725 Martin Dobrovolný', '† 30. 11. 1763 Krucemburk'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),



    # 11. generace (2816–2847)

    2816: dict(n='Jiří Holánek', y='1630–1706', st='mh',

             f=['* asi 1630', '× asi 1655 Dorota Holánková', '† 13. 10. 1706'],

             pohreb='Křižanov, sv. Václav', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2817: dict(n='Dorota Holánková', y='1635–1704', st='mh',

             f=['* asi 1635', '× asi 1655 Jiří Holánek', '† 6. 2. 1704'],

             pohreb='Křižanov, sv. Václav', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2818: dict(n='Řehoř Škoda', y='1643–1726', st='mh',

             f=['* asi 1643 Dolní Bory', '× 13. 2. 1678 Sklené Salomena Šebková', '† 1. 7. 1726 Dolní Bory'],

             zam='mlynář', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2819: dict(n='Salomena Šebková', y='1650–1715', st='mh',

             f=['* asi 1650', '× 13. 2. 1678 Sklené Řehoř Škoda', '† 5. 3. 1715'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2820: dict(n='Šebestian Holánek', y='1666–1747', st='mh',

             f=['* asi 1666', '× 3. 2. 1686 Mariana Skřípalová', '† 6. 8. 1747'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2821: dict(n='Mariana Skřípalová', y='1666–1748', st='mh',

             f=['* asi 1666 Sviny', '× 3. 2. 1686 Šebestian Holánek', '† 22. 8. 1748'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2822: dict(n='Jan Havelka', y='1672–1727', st='mh',

             f=['* 19. 5. 1672', '× 28. 1. 1703 Margita Pávková', '† 28. 8. 1727'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2823: dict(n='Margita Pávková', y='1680–1730', st='mh',

             f=['* 14. 3. 1680', '× 28. 1. 1703 Jan Havelka', '† asi 1730'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2824: dict(n='Jan Žundálek', y='1677–1727', st='mh',

             f=['* asi 1677', '× 13. 7. 1704 Jívoví a pernštejnské panství Mariana Karásková', '† 25. 1. 1727'],

             zam='šafář', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2825: dict(n='Mariana Karásková', y='1685–1733', st='mh',

             f=['* 2. 8. 1685', '× 13. 7. 1704 Jívoví a pernštejnské panství Jan Žundálek', '† 14. 9. 1733'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2826: dict(n='Jakub Cziczálek', y='1669–1737', st='mh',

             f=['* 7. 6. 1669', '× asi 1690 Magdalena Cziczálková', '† 25. 12. 1737'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2827: dict(n='Magdalena Cziczálková', y='1670–1736', st='mh',

             f=['* asi 1670', '× asi 1690 Jakub Cziczálek', '† 11. 5. 1736'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2834: dict(n='Jan Dymáček', y='1660–1705', st='mh',

             f=['* asi 1660 Sobíňov', '† asi 1705'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2840: dict(n='Tomáš Dymáček', y='1664–1710', st='mh',

             f=['* asi 1664', '× 11. 6. 1684 Sobíňov a Horní Studenec Dorota Jeigerová', '† asi 1710'],

             zam='slévač, správce v huti', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2841: dict(n='Dorota Jeigerová', y='1664–1710', st='mh',

             f=['* asi 1664 Horní Studenec', '× 11. 6. 1684 Sobíňov a Horní Studenec Tomáš Dymáček', '† asi 1710 Sobíňov'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2842: dict(n='Matěj Chlebeček', y='1662–1706', st='mh',

             f=['* 24. 2. 1662', '× 1. 10. 1685 Sopoty a pila pod Bílkem Alžběta Ambrožová', '† 7. 12. 1706 Sobíňov'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2843: dict(n='Alžběta Ambrožová', y='1665–1710', st='mh',

             f=['* asi 1665', '× 1. 10. 1685 Sopoty a pila pod Bílkem Matěj Chlebeček', '† asi 1710'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2844: dict(n='Jan Dobrovolný', y='1665–1725', st='mh',

             f=['* 1665 Benátky', '× 21. 10. 1685 Kateřina Pátková', '† 25. 11. 1725'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2845: dict(n='Kateřina Pátková', y='1665–1737', st='mh',

             f=['* 1665', '× 21. 10. 1685 Jan Dobrovolný', '† 27. 12. 1737'],

             pohreb='Krucemburk, sv. Mikuláš', r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2846: dict(n='Martin Zrzavý', y='1668–1720', st='mh',

             f=['* 5. 12. 1668', '× 19. 1. 1698 Alžběta Fejtková', '† asi 1720'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),

    2847: dict(n='Alžběta Fejtková', y='1678–1720', st='mh',

             f=['* asi 1678', '× 19. 1. 1698 Martin Zrzavý', '† asi 1720'], r=[],

             note='Údaj z exportu Geni / MyHeritage (export-Forest.ged).'),



}



LINES = {

        9: ("Pivničkovi a Menšíkovi", "Pražská větev – babička MUDr. Ludmila Menšíková roz. Pivničková (1909–2007), učitel Jan Pivnička a přednosta stanice Antonín Tomíček."),

    10: ("Jarolímovi a Hůlkovi", "Obuvníci ze Žlebů, krejčí z Dolní Krupé a lesníci; dědeček Richard Jarolím (1927–2012)."),

    11: ("Holánkovi a Henzlovi", "Zámečníci a hamerníci ze Starého Ranska a truhláři z Hluboké; babička Zdenka Jarolímová roz. Holánková (* 1928)."),

    12: ("Čákiovi", "Slovenská větev rodiny Julie Menšík Čákiové – pradědeček Juraj (Jiří) Čáki (* asi 1921) a prababička Marie rozená Bubancová z východního Slovenska (obce Dúbrava a Šmigovec, okres Snina)."),

    14: ("Krejzkovi a Černí", "Větev pradědečka MUDr. Miroslava Krejzka (1914–1978, Bystřice nad Pernštejnem / Žamberk) a prababičky Věry roz. Černé (1917–2005, Poděbrady / Žamberk)."),

}



# Boční příbuzní: n = „Jméno (roky)“, t = text na stránce předka (plná data sem), vetev = karta ve stromu

# se stejnými poli jako osoba v P (n, y, f, roz, zam, bydl, puvod, pohreb, vztah) + manzel a deti.

SIDE = [

    dict(k=2, n="Jakub Menšík (* 1977)", t="Bratr Jana, * 8. 2. / 10. 2. 1977 Praha, bytem Praha 6 - Dejvice.", r=[],

         vetev=dict(n="Jakub Menšík", y="* 1977", f=["* 8. 2. 1977 Praha (v rodinném stromu též 10. 2. 1977)"], bydl="Praha 6 - Dejvice (Mozambická)", vztah="bratr Jana")),

    dict(k=3, n="Mgr. Lucie Černíková roz. Čákiová", t="Sestra Julie, Mgr., roz. Čákiová (manžel Aleš Černík, CIO v C.S.CARGO; děti David Černík * asi 2004 a Lenka Černíková * asi 2008).", r=[],

         vetev=dict(n="Mgr. Lucie Černíková", y="", roz="Čákiová", bydl="Praha (Stodůlky)", vztah="sestra Julie",

                    manzel=dict(n="Aleš Černík", y="", zam="ředitel IT (CIO)", bydl="Praha"),

                    deti=[dict(n="David Černík", y="* asi 2004", f=["* asi 2004 Praha"], bydl="Praha"),

                          dict(n="Lenka Černíková", y="* asi 2008", f=["* asi 2008 Praha"], bydl="Praha")])),

    dict(k=4, n="Ivan Menšík (asi 1942–2012)", t="Starší bratr Radima Menšíka (strýc Jana), syn Miroslava a Ludmily, * asi 1942 Praha, † 2012 Praha, pohřben v Čtyřkolech.", r=[],

         vetev=dict(n="Ivan Menšík", y="asi 1942–2012", f=["* asi 1942 Praha", "† 2012 Praha"], bydl="Praha",

                    pohreb="Čtyřkoly", vztah="bratr Radima")),

    dict(k=5, n="Lenka Hájková roz. Jarolímová (* 1962)", t="Mladší sestra Zdeňky (teta Jana), * 21. / 24. 4. 1962 Hradec Králové; manžel Ing. arch. Martin Hájek (* 1960 Smiřice, architekt), syn Ing. arch. Václav Hájek (* 17. 1. / 20. 2. 1983 Hradec Králové, architekt).", r=[],

         vetev=dict(n="Lenka Hájková", y="* 1962", f=["* 24. 4. 1962 Hradec Králové (v rodinném stromu též 21. 4. 1962)"], roz="Jarolímová", bydl="Hradec Králové (Františka Žaloudka 422)", vztah="sestra Zdeňky",

                    manzel=dict(n="Ing. arch. Martin Hájek", y="* 1960", zam="architekt", bydl="Smiřice"),

                    deti=[dict(n="Ing. arch. Václav Hájek", y="* 1983", f=["* 20. 2. 1983 Hradec Králové (v rodinném stromu též 17. 1. 1983)"], zam="architekt", bydl="Hradec Králové (Horova 1184)")])),

    dict(k=7, n="MUDr. Iva Gajdošová († 2013)", t="Lékařka (MUDr.), sestra Evy Čákiové (teta Julie), roz. Krejzková, † 2013 Hradec Králové; dcera Barbora Gajdošová (partner René Štefec, dcera Evelína Štefcová * 2013) a syn Marek Gajdoš.", r=[],

         vetev=dict(n="MUDr. Iva Gajdošová", y="† 2013", f=["† 2013 Hradec Králové"], roz="Krejzková", zam="lékařka", pohreb="Hradec Králové",

                    bydl="Hradec Králové", vztah="sestra Evy",

                    manzel=dict(n="MUDr. Gajdoš", y="", zam="lékař", bydl="Hradec Králové"),

                    deti=[dict(n="Barbora Gajdošová", y="", bydl="Hradec Králové / Praha",

                               manzel=dict(n="René Štefec", y="", zam="kominík", bydl="Praha"),

                               deti=[dict(n="Evelína Štefcová", y="* 2013", bydl="Praha", vztah="dcera")]),

                          dict(n="Marek Gajdoš", y="", bydl="Hradec Králové / Praha", manzel=dict(n="Valadez", y="", puvod="Mexiko", bydl="Praha"))])),

    dict(k=8, n="František Pavel Menšík (* 1901)", t="Starší bratr doc. Miroslava Menšíka (prastrýc Jana), * 1901 Praha, † v dětství Praha. Doložen v policejní konskripci karton 388, obraz 88.", r=[],

         vetev=dict(n="František Pavel Menšík", y="* 1901", f=["* 1901 Praha", "† v dětství Praha"], vztah="bratr Miroslava")),

    dict(k=8, n="Vlastimila Menšíková (* 1902)", t="Sestra doc. Miroslava Menšíka (prateta Jana), * 1902 Praha, dcera Františka a Pavlíny. Doložena v policejní konskripci karton 388, obraz 88.", r=[],

         vetev=dict(n="Vlastimila Menšíková", y="* 1902", f=["* 1902 Praha"], vztah="sestra Miroslava")),

    dict(k=34, n="Pavlína Berta Linhartová roz. Jirkovská (1854–1927)", t="Sestra Aloise Jirkovského, teta Pavlíny Menšíkové roz. Jirkovské a kmotra při jejím křtu. Narozena 24. 8. 1854 v Praze u křižovníků, oddána 20. 5. 1883 u Týna s Janem Linhartem (* 16. 4. 1854 Velké Číčovice, mlynářský chasník a záložník vozatajského pluku). Zemřela 27. 2. 1927 na Král. Vinohradech. Matka slavné odbojové rodiny bratří Linhartových.", r=["tyn_oddani_jan_linhart_1883"],
         vetev=dict(n="Pavlína Berta Linhartová", y="1854–1927", f=["* 24. 8. 1854 Praha (křest u sv. Františka)", "× 20. 5. 1883 Praha (Týnský chrám) Jan Linhart (* 1854 Číčovice)", "† 27. 2. 1927 Praha-Vinohrady"], roz="Jirkovská", vztah="sestra Aloise, teta Pavlíny")),

    dict(k=17, n="Bedřich Linhart (1886–1944)", t="Vlastní bratranec Pavlíny Menšíkové roz. Jirkovské. Narozen 9. 4. 1886 v Michli čp. 14, vrchní kriminální inspektor pražské policie, ruský legionář a klíčový představitel protinacistického odboje (krycí jméno „Polda“; spolupráce s Obranou národa, skupinou Tří králů a sítí ÚVOD). V letech 1939–1941 jako tlumočník v Petschkově paláci varoval ohrožené osoby a vynášel zprávy gestapa; v garáži a autě ukrýval vysílačku Sparta Ic. Zatčen v červenci 1942 a dne 20. 10. 1944 v 16:00 popraven gilotinou v pankrácké sekyrárně.", r=["tyn_oddani_jan_linhart_1883"],
         vetev=dict(n="Bedřich Linhart", y="1886–1944", f=["* 9. 4. 1886 Praha-Michle", "† 20. 10. 1944 Praha-Pankrác (popraven v sekyrárně)"], zam="vrchní kriminální inspektor policie, ruský legionář, protinacistický odbojář (Polda)", vztah="bratranec Pavlíny Menšíkové roz. Jirkovské")),

    dict(k=17, n="Otto Linhart (1895–1980)", t="Vlastní bratranec Pavlíny Menšíkové roz. Jirkovské. Narozen 24. 9. 1895 v Praze u sv. Františka, ruský legionář, poštovní revident na Hlavní poště v Praze a legendární radiotelegrafista ilegální vysílačky Sparta I (ÚVOD). Jako jediný ze čtyř bratří přežil protektorátní pronásledování gestapem v hluboké ilegalitě.", r=[],
         vetev=dict(n="Otto Linhart", y="1895–1980", f=["* 24. 9. 1895 Praha", "† 29. 3. 1980 Praha"], zam="poštovní úředník, ruský legionář, radiotelegrafista vysílačky Sparta I", vztah="bratranec Pavlíny Menšíkové roz. Jirkovské")),

    dict(k=17, n="Václav a Zdeněk Linhartovi", t="Bratři Bedřicha a Otto Linharta, bratranci Pavlíny Menšíkové roz. Jirkovské. Zdeněk Linhart (* 12. 5. 1888 Praha, † 17. 1. 1943 KT Stutthof), řidič tramvaje, poskytoval byt pro vysílání Jindřicha Klečky. Václav Linhart (* 21. 7. 1892 Praha, † 4. 7. 1942 Praha), kamenotiskař a odbojář, při zatýkání gestapem požil cyankáli. Sestry Marie a Ludmila přežily věznění v KT Ravensbrück.", r=[],
         vetev=dict(n="Václav a Zdeněk Linhartovi", y="† 1942, † 1943", f=["Václav: * 21. 7. 1892, † 4. 7. 1942 Praha (cyankáli při zatýkání)", "Zdeněk: * 12. 5. 1888, † 17. 1. 1943 KT Stutthof"], zam="odbojáři (Sparta I)", vztah="bratranci Pavlíny Menšíkové roz. Jirkovské")),

    dict(k=65, n="Václav Horych (* 1795)", t="Bratr Barbory Menšíkové roz. Horychové, měšťan v Jistebnici čp. 86. Narozen 4. 8. 1795 v čp. 136, oddán 18. 2. 1828 v Jistebnici s Marií Šmedlovou (čp. 197). V roce 1865 byl svědkem na svatbě svého synovce Josefa Menšíka ml. a Marie Šmedlové.", r=["jistebnice_oddani_josef_mensik_1828", "jistebnice_oddani_josef_mensik_1865"],

         vetev=dict(n="Václav Horych", y="* 1795", f=["* 4. 8. 1795 Jistebnice čp. 136", "× 18. 2. 1828 Jistebnice Mariana Šmedlová"], zam="měšťan v Jistebnici čp. 86", vztah="bratr Barbory")),

    dict(k=12, n="Miroslav Čáky", t="Bratr Juraje Čákiho, původem ze Slovenska (Zemplín / Snina).", r=[],

         vetev=dict(n="Miroslav Čáky", y="", puvod="Slovensko (Zemplín / Snina)", vztah="bratr Juraje (psán Čáky)")),

    dict(k=14, n="5 bratrů Krejzkových", t="Pět bratrů MUDr. Miroslava Krejzka z Bystřice nad Pernštejnem.", r=[],

         vetev=dict(n="bratři Krejzkovi", y="", puvod="Bystřice nad Pernštejnem", vztah="5 bratrů Miroslava")),

    dict(k=15, n="bratr Věry Černé", t="Bratr Věry Krejzkové roz. Černé, syn Josefa Černého.", r=[],

         vetev=dict(n="bratr Černý", y="", vztah="bratr Věry, syn Josefa")),

    dict(k=21, n="Josefa Haňavcová roz. Jarolímová", t="Sestra Emilie, Žleby čp. 37. Manžel Rudolf Haňavec (* 22. 10. 1896 Žleby čp. 190), dcera Hana Hrachová roz. Haňavcová (Žleby / Rumburk, manžel Jan Hrach, † Rumburk).", r=[],

         vetev=dict(n="Josefa Haňavcová", y="", roz="Jarolímová", bydl="Žleby čp. 37", vztah="sestra Emilie",

                    manzel=dict(n="Rudolf Haňavec", y="* 1896", f=["* 22. 10. 1896 Žleby čp. 190"]),

                    deti=[dict(n="Hana Hrachová", y="", roz="Haňavcová", bydl="Žleby / Rumburk",

                               manzel=dict(n="Jan Hrach", y="", f=["† Rumburk"], bydl="Rumburk"))])),

    dict(k=21, n="Rudolf Jarolím (* 1903)", t="Bratr Emilie, * 1. 10. 1903 Žleby čp. 37. Syn Jaroslav Jarolím (* 10. 6. 1927 Žleby – † 10. 5. 2012 New York).", r=[],

         vetev=dict(n="Rudolf Jarolím", y="* 1903", f=["* 1. 10. 1903 Žleby čp. 37"], vztah="bratr Emilie",

                    deti=[dict(n="Jaroslav Jarolím", y="1927–2012", f=["* 10. 6. 1927 Žleby", "† 10. 5. 2012 New York"],

                               bydl="New York (ze Žlebů)")])),

    dict(k=22, n="Helena Měřínská roz. Holánková (1896–1982)", t="Sestra Julia, * 1896 Staré Ransko čp. 55. Manžel František Měřínský (* 4. 6. 1890 Staré Ransko – † 1951), syn Miloš Měřínský (1924–1998, architekt; manželka Jitka Měřínská * 1942, učitelka), vnučka Jitka Měřínská (* 1979, Brno).", r=[],

         vetev=dict(n="Helena Měřínská", y="1896–1982", f=["* 1896 Staré Ransko čp. 55", "† 1982"], roz="Holánková", vztah="sestra Julia",

                    manzel=dict(n="František Měřínský", y="1890–1951", f=["* 4. 6. 1890 Staré Ransko", "† 1951"]),

                    deti=[dict(n="Miloš Měřínský", y="1924–1998", zam="architekt",

                               manzel=dict(n="Jitka Měřínská", y="* 1942", zam="učitelka"),

                               deti=[dict(n="Jitka Měřínská", y="* 1979", bydl="Brno")])])),

    dict(k=43, n="Ignác Havel (* 1864)", t="Bratr Antonie Havlové, * 9. 7. 1864 Dolní Krupá čp. 42, syn mistra krejčovského Jana Havla a Anny Jeřábkové.", r=[],

         vetev=dict(n="Ignác Havel", y="* 1864", f=["* 9. 7. 1864 Dolní Krupá čp. 42"], vztah="bratr Antonie")),

    dict(k=43, n="Otilie Havlová (* 1876)", t="Sestra Antonie Havlové, * 12. 12. 1876 Slatina nad Úpou, v domácnosti.", r=[],

         vetev=dict(n="Otilie Havlová", y="* 1876", f=["* 12. 12. 1876 Slatina nad Úpou"], zam="v domácnosti", vztah="sestra Antonie")),

]



ISSUES = [

    ("Otcovská větev Menšíků – narození a rodiče doc. RNDr. Miroslava Vladimíra Menšíka (* 3. 8. 1906 Praha, č. 8)", "Vyřešeno z primárních matrik: Miroslav Vladimír Menšík se narodil 3. 8. 1906 v Praze čp. 1717-II a byl pokřtěn 9. 8. 1906 v kostele Nejsv. Trojice v Podskalí (TRP N15, sn. 56). Rodiče František Xaver Menšík (* 8. 7. 1873 Jistebnice) a Pavlína Rosalie roz. Jirkovská (* 2. 11. 1882 Praha) oddáni 8. 5. 1902 u Týna."),

        ("Otcovská větev Menšíků – rodné příjmení a rodiče babičky MUDr. Ludmily Menšíkové (č. 9)", "Vyřešeno z primárních matrik, archiválií a evidence SPH: babička MUDr. Ludmila Menšíková byla rozená Pivničková (1909–2007), dětská lékařka, dcera měšťanského učitele na Hradčanech Jana Emanuela Pivničky (1872–po 1921) a Emmy Marie roz. Tomíčkové (* 1886 Warta). Doloženi i prarodiče Josef Pivnička (* 1844 Čechtice) & Antonie roz. Grubnerová (* 1843 Dobříš) a přednosta stanice Antonín Tomíček & Anna roz. Halíková z Lobče."),

    ("Větev manželky Julie Menšík Čákiové (prarodiče dětí č. 12–15)", "Vyřešeno z rodinných údajů: všichni 4 prarodiče Julie jsou identifikováni – Juraj (Jiří) Čáki (* asi 1921, č. 12) & Marie roz. Bubancová (č. 13) z otcovy strany, Miroslav Krejzek (1914–1978, č. 14) & Věra roz. Černá (1917–2005, č. 15) z matčiny strany."),

    ("Původ pradědečka Fridricha Hůlka (č. 20)", "Otevřené: v PDF je uveden jako lesní inženýr s fotografií, ale bez data a místa narození; jeho syn Richard (* 1927 Žleby čp. 17) nesl příjmení matky Jarolím."),

    ("Povolání Matěje Šímy (č. 90) ze Starého Ranska čp. 2", "Otevřené: v PDF je uvedeno 'horolezec' – v matrice Starého Ranska ověřit, zda nešlo o čtení slova 'horník' / 'havíř' u železáren."),

]



HYPOTEZY = [

]



SAME = {}

