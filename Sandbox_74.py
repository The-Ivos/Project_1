prvni_radek = "První řádek v souboru,\n"
druhy_radek = "druhý řádek v souboru,\n"
treti_radek = "třetí řádek v souboru."

open("txt_soubor.txt","w").close()
with open("txt_soubor.txt","r+",encoding="utf-8") as file:
    file.write(prvni_radek)
    file.write(druhy_radek)
    file.write(treti_radek)

    file.seek(0)

    content = file.read()

print(content)