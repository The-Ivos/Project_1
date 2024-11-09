def pridej_deset(a):
    return a + 10

def dej_prijmeni(a):
    return a[-1]

def navys_konretne(a,b):
    return print(dej_prijmeni(a),pridej_deset(b))

jmeno = "Ivos Srot"

cislo = 24

navys_konretne(jmeno.split(),cislo)