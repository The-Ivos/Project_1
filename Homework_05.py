pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]

print("Zacatek :",pismena)

while pismena:
    pismeno = input("Ktere pismeno chces vyhodit? ")
    if pismeno in pismena:
        pismena.remove(pismeno)
    elif pismeno not in pismena:
        print(pismeno,"neni soucasti pismen!")
        continue
    print("zbyvaji pismena:",pismena)
else:
    print("Seznam je prazdny!")