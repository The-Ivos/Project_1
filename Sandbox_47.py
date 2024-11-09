# Vytvor list se zadanymi hodnotami
adresy = [
    "matous@holinka.com",
    "danek11@seznam.cz",
    "rennud15@gmail.com",
    "pepa@centrum.cz"
]

def filtruj_adresy_s_cisly(emaily: list) -> list:
    """
    Ze zadaneho objektu emailu vyber pouze ty, ktere obsahuji ciselne znaky.

    Priklad:
    >>> print(filtruj_adresy_s_cisly(["matous@holinka.com", "danek11@seznam.cz"]))
    ["danek11@seznam.cz"]
    """
    ciselne_hodnoty = []

    for email in emaily:
        for znak in email:
            if not znak.isnumeric():
                continue
            ciselne_hodnoty.append(email)
            break

    return ciselne_hodnoty

# Uloz vystup funkce do promenne
vysledek = filtruj_adresy_s_cisly(adresy)

# Vytiskni obsah promenne vysledek
print(vysledek)