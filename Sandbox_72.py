import os

def zapis_zpravu_do_txt_souboru(jmeno_souboru,zprava):
    if jmeno_souboru in os.listdir():
        rewrite = input("File already exists! Do you want to rewrite the file?\n")
        if rewrite == "no":
            return "No changes!"
    
    obsah = ""
    file = open(jmeno_souboru,"w",encoding="UTF-8").close()
    file = open(jmeno_souboru,"r+",encoding="UTF-8")
    file.write(zprava)
    file.seek(0)
    obsah += file.read()
    file.close()
    return obsah

zprava1 = "I am the ocean"
zprava2 = "I am the sea"
zprava3 = "there is a world"
zprava4 = "inside of me"

soubor1 = "Sandbox72_1.txt"
soubor2 = "Sandbox72_2.txt"
soubor3 = "Sandbox72_3.txt"
soubor4 = "Sandbox72_4.txt"

print(zapis_zpravu_do_txt_souboru(soubor3,zprava3))
print(zapis_zpravu_do_txt_souboru(soubor4,zprava4))
    
# print(os.listdir())