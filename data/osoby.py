# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…

P = {
    # 0. generace – výchozí osoba
    1: dict(n="Jan Menšík", y="* 1980", st="fam", sex="M",
            f=["* 1980"], r=[], note="Žijící – údaje jen základní."),

    # 1. generace – rodiče
    2: dict(n="Radim Menšík", y="* 1946", st="fam",
            f=["* 1946"], r=[], note="Žijící – údaje jen základní."),
    3: dict(n="Zdeňka Jarolímová", y="* 1949", st="fam",
            f=["* 1949"], r=[], note="Žijící – údaje jen základní."),

    # 2. generace – prarodiče (z matčiny strany 6–7; z otcovy strany 4–5 zatím k doplnění)
    6: dict(n="Richard Jarolím", y="1927–2012", st="fam",
            f=["* 26. 3. 1927 Žleby čp. 17", "× 30. 10. 1948 Rumburk Zdenka Holánková", "† 24. 3. 2012 Hradec Králové"],
            r=[], note="Údaje z rodinného stromu PDF."),
    7: dict(n="Zdenka Holánková", y="* 1928", st="fam",
            f=["* 20. 11. 1928 Hluboká čp. 36", "× 30. 10. 1948 Rumburk Richard Jarolím"],
            r=[], note="Údaje z rodinného stromu PDF."),

    # 3. generace – pradědečci a prababičky z matčiny strany (12–15)
    12: dict(n="Fridrich Hůlek", y="", st="fam",
             f=["lesní inženýr"], r=[],
             note="Údaje z rodinného stromu PDF (datum a místo narození zatím neuvedeny; syn Richard nesl příjmení matky Jarolím)."),
    13: dict(n="Emilie Jarolímová", y="* 1899", st="fam",
             f=["* 15. 4. 1899 Žleby čp. 37", "dělnice"], r=[],
             note="Údaje z rodinného stromu PDF."),
    14: dict(n="Julius Holánek", y="1889–1952", st="fam",
             f=["* 20. 7. 1889 Staré Ransko čp. 55", "zámečník", "× 20. 5. 1926 Sofia Henzlová", "† 1952"], r=[],
             note="Údaje z rodinného stromu PDF."),
    15: dict(n="Sofia Henzlová", y="1904–1985", st="fam",
             f=["* 8. 5. 1904 Hluboká čp. 38", "× 20. 5. 1926 Julius Holánek", "† 1985"], r=[],
             note="Údaje z rodinného stromu PDF (psána též Sofia Henzl)."),

    # 4. generace – praprarodiče (26–31)
    26: dict(n="Jan Jarolím", y="1863–1903", st="fam",
             f=["* 4. 6. 1863 Žleby čp. 126", "obuvník", "× 29. 5. 1888 Dolní Krupá Antonie Havlová", "† 31. 7. 1903 Žleby čp. 37"], r=[],
             note="Údaje z rodinného stromu PDF."),
    27: dict(n="Antonie Havlová", y="1857 – po 1914", st="fam",
             f=["* 13. 1. 1857 Dolní Krupá čp. 42", "× 29. 5. 1888 Dolní Krupá Jan Jarolím", "† po 1914"], r=[],
             note="Údaje z rodinného stromu PDF."),
    28: dict(n="František Holánek", y="* 1854", st="fam",
             f=["* 4. 10. 1854 Staré Ransko čp. 53", "zámečník", "× Julie Šímová"], r=[],
             note="Údaje z rodinného stromu PDF."),
    29: dict(n="Julie Šímová", y="* 1854", st="fam",
             f=["* 16. 3. 1854 Staré Ransko čp. 46", "× František Holánek"], r=[],
             note="Údaje z rodinného stromu PDF."),
    30: dict(n="Franz Henzl", y="1872–1954", st="fam",
             f=["* 12. 7. 1872 Hluboká čp. 15", "truhlář a hostinský", "× Aloisie Pospíchalová", "† 15. 2. 1954 Havlíčkův Brod čp. 539"], r=[],
             note="Údaje z rodinného stromu PDF."),
    31: dict(n="Aloisie Pospíchalová", y="1875–1957", st="fam",
             f=["* 6. 1. 1875 Chlum čp. 35", "× Franz Henzl", "† 1957"], r=[],
             note="Údaje z rodinného stromu PDF."),

    # 5. generace (52–61)
    52: dict(n="otec neuveden", y="", st="unk",
             f=[], r=[], note="Jan Jarolím (* 1863) byl nemanželským synem Barbory Jarolímové; otec v rodinném stromu neuveden."),
    53: dict(n="Barbora Jarolímová", y="", st="fam",
             f=["Žleby čp. 126"], r=[], note="Údaje z rodinného stromu PDF."),
    54: dict(n="Jan Havel", y="", st="fam",
             f=["krejčí v Dolní Krupé", "× Anna Jeřábková"], r=[], note="Údaje z rodinného stromu PDF."),
    55: dict(n="Anna Jeřábková", y="", st="fam",
             f=["Čachotín čp. 15", "× Jan Havel"], r=[], note="Údaje z rodinného stromu PDF (v PDF psáno Čachitín čp. 15)."),
    56: dict(n="Jan Holánek", y="* 1820", st="fam",
             f=["* 18. 6. 1820 Staré Ransko čp. 45", "domkař", "× Johanna Hlaváčková"], r=[],
             note="Údaje z rodinného stromu PDF."),
    57: dict(n="Johanna Hlaváčková", y="", st="fam",
             f=["Staré Ransko čp. 49", "× Jan Holánek"], r=[], note="Údaje z rodinného stromu PDF."),
    58: dict(n="Matěj Šíma", y="", st="fam",
             f=["Staré Ransko čp. 2", "horník / horolezec", "× Františka Benová"], r=[],
             note="Údaje z rodinného stromu PDF (v PDF uvedeno 'horolezec' – ověřit v matrice, zda nešlo o horníka / havíře v železárnách v Ransku)."),
    59: dict(n="Františka Benová", y="", st="fam",
             f=["Staré Ransko čp. 41", "× Matěj Šíma"], r=[], note="Údaje z rodinného stromu PDF."),
    60: dict(n="Václav Henzl", y="* 1844", st="fam",
             f=["* 6. 8. 1844 Hluboká čp. 15", "čtvrtláník", "× Marie Procházková"], r=[],
             note="Údaje z rodinného stromu PDF."),
    61: dict(n="Marie Procházková", y="", st="fam",
             f=["Hluboká čp. 7", "× Václav Henzl"], r=[], note="Údaje z rodinného stromu PDF."),

    # 6. generace (112–121)
    112: dict(n="Josef Holánek", y="", st="fam",
              f=["kovář a zámečník v Křižanově", "× Filipina Slámová"], r=[], note="Údaje z rodinného stromu PDF."),
    113: dict(n="Filipina Slámová", y="", st="fam",
              f=["Staré Ransko čp. 33", "× Josef Holánek"], r=[], note="Údaje z rodinného stromu PDF."),
    114: dict(n="Vojtěch Hlaváček", y="", st="fam",
              f=["uhlíř ve Starém Ransku čp. 49", "× Barbora Haislerová"], r=[], note="Údaje z rodinného stromu PDF."),
    115: dict(n="Barbora Haislerová", y="", st="fam",
              f=["Františkodol (Fraunsthal)", "× Vojtěch Hlaváček"], r=[], note="Údaje z rodinného stromu PDF."),
    116: dict(n="Tomáš Šíma", y="", st="fam",
              f=["dráb ve Starém Ransku čp. 2", "× Marie Halíková"], r=[], note="Údaje z rodinného stromu PDF."),
    117: dict(n="Marie Halíková", y="", st="fam",
              f=["Olešná (Volešná)", "× Tomáš Šíma"], r=[], note="Údaje z rodinného stromu PDF."),
    118: dict(n="František Ben", y="", st="fam",
              f=["hamernický mistr ve Starém Ransku čp. 41", "× Karolina Králíčková"], r=[], note="Údaje z rodinného stromu PDF."),
    119: dict(n="Karolina Králíčková", y="", st="fam",
              f=["Česká Kamenice", "× František Ben"], r=[], note="Údaje z rodinného stromu PDF."),
    120: dict(n="Jan Henzl", y="† před 1872", st="fam",
              f=["kovář a zámečník v Hluboké čp. 15", "× Anna Nováková", "† před 1872"], r=[], note="Údaje z rodinného stromu PDF."),
    121: dict(n="Anna Nováková", y="", st="fam",
              f=["Chlumětín", "× Jan Henzl"], r=[], note="Údaje z rodinného stromu PDF (psána Anna Nowak)."),

    # 7. generace (224–235)
    224: dict(n="František Holánek", y="", st="fam",
              f=["Křižanov"], r=[], note="Údaje z rodinného stromu PDF."),
    226: dict(n="Jan Sláma", y="", st="fam",
              f=["tesař ve Starém Ransku čp. 33", "× Alžběta Dymáčková"], r=[], note="Údaje z rodinného stromu PDF."),
    227: dict(n="Alžběta Dymáčková", y="", st="fam",
              f=["× Jan Sláma"], r=[], note="Údaje z rodinného stromu PDF."),
    230: dict(n="Josef Haisler", y="", st="fam",
              f=["Františkodol (Fraunsthal)"], r=[], note="Údaje z rodinného stromu PDF."),
    232: dict(n="Vojtěch Šíma", y="", st="fam",
              f=["Staré Ransko"], r=[], note="Údaje z rodinného stromu PDF."),
    234: dict(n="Ondřej Halík", y="", st="fam",
              f=["× Kateřina Dušková"], r=[], note="Údaje z rodinného stromu PDF."),
    235: dict(n="Kateřina Dušková", y="", st="fam",
              f=["× Ondřej Halík"], r=[], note="Údaje z rodinného stromu PDF."),
}

LINES = {
    12: ("Hůlkovi", "Lesní inženýr Fridrich Hůlek – větev otce dědečka Richarda Jarolíma."),
    13: ("Jarolímovi", "Obuvníci ze Žlebů a krejčí Havlovi z Dolní Krupé."),
    14: ("Holánkovi", "Zámečníci, kováři, uhlíři a hamerníci ze Starého Ranska a Křižanova."),
    15: ("Henzlovi", "Truhláři, hostinští a kováři z Hluboké, Chlumu a Chlumětína."),
}

SIDE = [
    dict(k=1, n="Julie Menšík Čákiová (* 1979)", t="Manželka Jana.", r=[]),
    dict(k=1, n="Jakub Menšík (* 1977)", t="Bratr Jana.", r=[]),
    dict(k=3, n="Lenka Hájková roz. Jarolímová (* 1962)", t="Sestra Zdeňky (manžel Martin Hájek * 1960, syn Václav Hájek * 1983).", r=[]),
    dict(k=13, n="Josefa Haňavcová roz. Jarolímová", t="Sestra Emilie, Žleby čp. 37. Manžel Rudolf Haňavec (* 22. 10. 1896 Žleby čp. 190), dcera Hana Haňavcová (Žleby / Rumburk).", r=[]),
    dict(k=13, n="Rudolf Jarolím (* 1. 10. 1903 Žleby čp. 37)", t="Bratr Emilie. Syn Jaroslav Jarolím (* 10. 6. 1927 Žleby – † 10. 5. 2012 New York).", r=[]),
    dict(k=14, n="Helena Měřínská roz. Holánková (1896–1982)", t="Sestra Julia, * 1896 Staré Ransko čp. 55. Manžel František Měřínský (* 4. 6. 1890 Staré Ransko – † 1951), syn Miloš Měřínský (1924–1998), vnučka Jitka Měřínská (* 1979).", r=[]),
    dict(k=27, n="Otilie Havlová (* 12. 12. 1876 Slatina nad Úpou)", t="Sestra Antonie Havlové, v domácnosti.", r=[]),
]

ISSUES = [
    ("Otcovská větev Menšíkových (č. 4–5 a 8–11)", "Otevřené: v dodaném PDF je zpracována matčiny větev (Jarolímovi, Holánkovi, Henzlovi) a větev strýce Martina Hájka; prarodiče a pradědečci z otcovy strany (Radim Menšík * 1946) zatím chybí."),
    ("Původ pradědečka Fridricha Hůlka (č. 12)", "Otevřené: v PDF je uveden jako lesní inženýr s fotografií, ale bez data a místa narození; dědeček Richard (* 1927 Žleby čp. 17) nesl příjmení matky Jarolím."),
    ("Povolání Matěje Šímy (č. 58) ze Starého Ranska čp. 2", "Otevřené: v PDF je uvedeno 'horolezec' – v matrice Starého Ranska ověřit, zda nešlo o čtení slova 'horník' / 'havíř' u železáren."),
]

HYPOTEZY = [
]

SAME = {}
