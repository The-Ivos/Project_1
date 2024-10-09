vysledek = list()
start = "6"
stop = 9
delitel = 3

start = input("Zadej start: ")
stop = input("Zadej stop: ")
delitel = input("Zadej delitel: ")
        
if start.isdigit():
    start = int(start)
if stop.isdigit():
    stop = int(stop)
if delitel.isdigit():
    delitel = int(delitel)

if isinstance(start,int) and isinstance(stop,int) and isinstance(delitel,int):
    print("Zadaný rozsah: " + "<" + str(start) + ", " + str(stop) + ">")
    for i in range(start,stop+1):
        if i % delitel == 0:
            vysledek.append(i)
    print("Čísla dělitelná " + str(delitel) + ": " + str(vysledek))
else:
    print("Zadané vstupy musí být čísla.")



    