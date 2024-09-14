mesta = ["0", "Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = [0, 150, 200, 120, 120, 100, 100]
cara = "=" * 35
nabidka = """1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""

print("VITEJTE U NASI APLIKACE DESTINATIO!\n" + cara)
print(nabidka)
jmeno = input("Zadejte sve krestni jmeno: ")
prijmeni = input("Zadejte sve prijmeni: ")
destinace = int(input("Zadejte cislo cilove destinace z nabidky: "))
email = input("Zadejte email: ")
rok_narozeni = input("Zadejte svuj rok narozeni: ")

print(cara)
print("CISLO DESTINACE: " + str(destinace))
print("JMENO: " + jmeno)
print("PRIJMENI: " + prijmeni)
print("EMAIL: " + email)
print(cara)

print("DEKUJI, " + jmeno + " ZA OBJEDNAVKU, ")
print("CIL. DESTINACE: " + str(mesta[destinace]) + "," + " CENA JIZDNEHO: " + str(ceny[destinace]) + "," )
print("NA TVUJ MAIL: " + email + " JSME POSLALI LISTEK.")
print(cara)