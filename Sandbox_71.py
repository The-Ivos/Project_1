muj_string = "Nazdar blbecku"
muj_druhej_string = "To cumis, co? "

animals = ("kocka","kun","pes","prase","krokodyl",muj_string,muj_druhej_string,"chlobot")

stringlines = []

for i in animals:
    stringlines.append(i+"\n")

stringlines[-1] = stringlines[-1].rstrip("\n")

open("muj_novej_file.txt",mode="w",encoding="UTF-8").close()
muj_soubor = open("muj_novej_file.txt",mode="r+",encoding="UTF-8")

# muj_soubor.write(muj_string)
# muj_soubor.write(muj_druhej_string)

muj_soubor.writelines(stringlines)

print(muj_soubor.tell())

muj_soubor.seek(muj_soubor.seek(0,1)/3)

print(muj_soubor.tell())

# obsah_fileu = muj_soubor.read()
print(muj_soubor.read())

print(muj_soubor.tell())


muj_soubor.close()

# print(obsah_fileu)




