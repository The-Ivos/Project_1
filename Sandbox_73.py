def precti_logy(soubor: str):
    with open(soubor,"r+",encoding="UTF-8") as file:
        content = file.read()
        return print(content)
 
# def vyber_pouze_typ(obsah_souboru,typ):
#     with open(soubor,"r+",encoding="UTF-8") as file:
#         content = file.readlines()
#         return content


precti_logy("zaznamy.txt")