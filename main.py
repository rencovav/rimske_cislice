def prevodNaRimske(cislo):
    pravidla = (
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("XXX", 30),
        ("XX", 20),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    )

    vysledek = ""
    for pismeno, hodnota in pravidla:
        while cislo >= hodnota:
            cislo -= hodnota
            vysledek += pismeno

    return print(vysledek)

zadani = int(input("Zadej číslo, které bude převedeno na římské: "))
prevodNaRimske(zadani)


def prevodNaArabske(rimskaCislice):
    pravidla = (
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("XXX", 30),
        ("XX", 20),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    )

    vysledek = 0
    for cislice in rimskaCislice:
        for pismeno, hodnota in pravidla:
            while cislice == pismeno:
                vysledek += hodnota

    return print(vysledek)


zadani2 = (input("Zadej číslo, které bude převedeno na arabske: "))
prevodNaArabske(zadani2)