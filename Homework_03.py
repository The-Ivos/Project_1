import os

sluzby = ("dostupné filmy", "detaily filmu", "seznam režisérů")
oddelovac = "=" * 62

film_1 = {
    "jmeno": "Shawshank Redemption",
    "rating": "93/100",
    "rok": 1994,
    "reziser": "Frank Darabont",
    "stopaz": 144
}

film_2 = {
    "jmeno": "The Godfather",
    "rating": "92/100",
    "rok": 1972,
    "reziser": "Francis Ford Coppola",
    "stopaz": 175
}

film_3 = {
    "jmeno": "The Dark Knight",
    "rating": "90/100",
    "rok": 2008,
    "reziser": "Christopher Nolan",
    "stopaz": 152
}

filmy = {film_1["jmeno"]: film_1, film_2["jmeno"]: film_2 ,film_3["jmeno"]: film_3}

welcome = "VITEJ V NASEM FILMOVEM SLOVNIKU!"
welcome_len = len(welcome)
text_centring = 62
center_txt = welcome.center(text_centring)
menu_lines = "=" * (text_centring)
menu = "dostupne filmy | detaily filmu | seznam reziseru"
center_menu = menu.center(text_centring)
dostupne_filmy = "Dostupne filmy:"

os.system('cls')

# print(film_1["jmeno"])
# print(film_1)

print(center_txt)
print(oddelovac)
print(center_menu)
print(oddelovac)

# print(filmy[film_1["jmeno"]]["jmeno"])

sluzba = input("Vyber sluzbu: ").lower()


if sluzba == "dostupne filmy":
    os.system('cls')
    print(dostupne_filmy.center(text_centring))
    print(oddelovac)
    print(filmy[film_1["jmeno"]]["jmeno"] + ", " + filmy[film_2["jmeno"]]["jmeno"] + ", " + filmy[film_3["jmeno"]]["jmeno"])
    print(oddelovac)
    print("")
    chcete_detaily = input("Chcete zobrazit detaily filmu? ").upper()
    if chcete_detaily == "ANO":
        os.system('cls')
        print(dostupne_filmy.center(text_centring))
        print(oddelovac)
        print(filmy[film_1["jmeno"]]["jmeno"] + ", " + filmy[film_2["jmeno"]]["jmeno"] + ", " + filmy[film_3["jmeno"]]["jmeno"])
        print(oddelovac)
        print("")
        detail_filmu = input("Vyberte film, jehoz detaily chcete zobrazit: ").title()
        if detail_filmu == film_1["jmeno"]:
            os.system('cls')
            print("Detaily filmu: ")
            print(oddelovac)
            print(film_1)
            print(oddelovac)
        elif detail_filmu == film_2["jmeno"]:
            os.system('cls')
            print("Detaily filmu: ")
            print(oddelovac)
            print(film_2)
            print(oddelovac)
        elif detail_filmu == film_3["jmeno"]:
            os.system('cls')
            print("Detaily filmu: ")
            print(oddelovac)
            print(film_3)
            print(oddelovac)
        else:
            print("Film",detail_filmu,"nenalezen.")
    elif chcete_detaily == "NE":
        print("Ok.")
    else:
        print("Nerozumime odpovedi. Dekujeme za navstevu!")
elif sluzba == "detaily filmu":
    os.system('cls')
    print(dostupne_filmy.center(text_centring))
    print(oddelovac)
    print(filmy[film_1["jmeno"]]["jmeno"] + ", " + filmy[film_2["jmeno"]]["jmeno"] + ", " + filmy[film_3["jmeno"]]["jmeno"])
    print(oddelovac)
    print("")
    detail_filmu = input("Vyberte film, jehoz detaily chcete zobrazit: ").title()
    if detail_filmu == film_1["jmeno"]:
        os.system('cls')
        print("Detaily filmu: ")
        print(oddelovac)
        print(film_1)
        print(oddelovac)
    elif detail_filmu == film_2["jmeno"]:
        os.system('cls')
        print("Detaily filmu: ")
        print(oddelovac)
        print(film_2)
        print(oddelovac)
    elif detail_filmu == film_3["jmeno"]:
        os.system('cls')
        print("Detaily filmu: ")
        print(oddelovac)
        print(film_3)
        print(oddelovac)
    else:
        print("Film",detail_filmu,"nenalezen.")
elif sluzba == "seznam reziseru":
    reziseri = {film_1["reziser"],film_2["reziser"],film_3["reziser"]}
    os.system('cls')
    print("Vsichni reziseri: ")
    print(oddelovac)
    print(reziseri)
    print(oddelovac)
elif sluzba == "":
    print("Musite zadat nazev sluzby.")
else:
    print('Sluzba "' + sluzba + '" nenalezena.')



