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

filmy = {
    film_1["jmeno"]: film_1,
    film_2["jmeno"]: film_2,
    film_3["jmeno"]: film_3
}

# Programová logika ve smyčce
print("\t\tVÍTEJ V NAŠEM FILMOVÉM SLOVNÍKU")
print(oddelovac)
print(sluzby)
print(oddelovac)
while True:
    # Výběr služby uživatelem
    choice_sluzba = input("Zadej název služby z nabídky: dostupné filmy | detaily filmu | seznam režisérů (nebo 'konec' pro ukončení): \n")

    # Možnost ukončení programu
    if choice_sluzba.lower() == "konec":
        print("Děkujeme za použití filmového slovníku. Nashledanou!")
        break

    # Zobrazení dostupných filmů
    elif choice_sluzba.lower() == "dostupné filmy":
        print("\t\t\tDostupné filmy:")
        print(oddelovac)
        print(tuple(filmy.keys()))
        print(oddelovac)

    # Zobrazení seznamu režisérů
    elif choice_sluzba.lower() == "seznam režisérů":
        print("Všichni režiséři:")
        print(oddelovac)
        reziseri = set([film["reziser"] for film in filmy.values()])
        print(", ".join(reziseri))
        print(oddelovac)

    # Zobrazení detailů filmu
    elif choice_sluzba.lower() == "detaily filmu":
        print("Dostupné filmy pro zobrazení detailů:")
        print(oddelovac)
        print(tuple(filmy.keys()))
        print(oddelovac)

        choice_movie = input("Zadej název filmu pro zobrazení detailu: \n")

        if choice_movie in filmy:
            print(oddelovac)
            for key, value in filmy[choice_movie].items():
                print(f"{key.title()}: {value}")
            print(oddelovac)
        else:
            print("Tento film není v nabídce.")
    else:
        print("Zvolená služba není v nabídce. Zkuste to znovu.")  