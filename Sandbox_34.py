heslo = input("Zadej heslo")
while True:
    if heslo % 2 == 0:
        continue
    elif heslo > 100:
        break
    else:
        print("Done")