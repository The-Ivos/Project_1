def filtruj_adresy_s_cisly(a:set):

    vysledek = []

    for i in a:        
        for j in i:
            if j.isnumeric():
                vysledek.append(i)
                break
    
    return print(vysledek)

adresy = [
   "matous@holinka.com",
   "danek11@seznam.cz",
   "rennud15@gmail.com",
   "pepa@centrum.cz"
]

filtruj_adresy_s_cisly(adresy)