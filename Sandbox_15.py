def zdar():
    vec = input("Zadej co chces: ")
    if vec == ""  :
        zdar()
    else:
        print(vec)

zdar()
