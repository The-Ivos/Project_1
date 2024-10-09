# Zadané proměnné
# jmena = [
#     'Michal', 'Pepa', 'Honza',
#     'Pavel', 'Lukas', 'Matej',
#     'Iva', 'Klara', 'Jana',
#     'Honza', 'Vasek','Milan',
#     'Michal'
# ]
# kopie_jmen = jmena.copy()

# Iterace k získání indexů v listu "jmena"
for i in range(0):

    # Iterace k získání indexu, který je o 1 vyšší než aktuální hodnota i
    for j in range(i + 1, len(kopie_jmen)):

        # Pokud je hodnota na indexu i větší než hodnota na indexu j aktualizuj
        # ..pořadí hodnot v listu za pomocí indexů
        if kopie_jmen[i] > kopie_jmen[j]:
            kopie_jmen[i], kopie_jmen[j] = kopie_jmen[j], kopie_jmen[i]

# Vypiš výsledek
print(kopie_jmen)