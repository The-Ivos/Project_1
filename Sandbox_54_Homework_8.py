import random

def vrat_m_textove_znaky():
    return letters[random.randint(0,len(letters)-1)]

def vrat_v_textove_znaky():
    return letters[random.randint(0,len(letters)-1)].upper()

def vrat_ciselne_znaky():
    return random.randint(0,9)

def main(mala,velka,cisla,delka):
    if mala == "ne" and velka == "ne" and cisla == "ne":
        print("_"*delka)
        exit()

    elif mala == "ano" and velka == "ano" and cisla == "ano":
        pocet_mala = round(delka / 3)
        pocet_velka = round(delka / 3)
        pocet_cislo = delka - pocet_velka - pocet_mala
    
    elif mala == "ano" and velka == "ano" and cisla == "ne":
        pocet_velka = int(delka / 2)
        pocet_mala = delka - pocet_velka
        pocet_cislo = 0

    elif mala == "ano" and velka == "ne" and cisla == "ne":
        pocet_mala = delka
        pocet_cislo = 0
        pocet_velka = 0

    elif mala == "ano" and velka == "ne" and cisla == "ano":
        pocet_mala = round(delka / 2)
        pocet_cislo = delka - pocet_mala
        pocet_velka = 0

    elif mala == "ne" and velka == "ano" and cisla == "ano":
        pocet_velka = round(delka / 2)
        pocet_cislo = delka - pocet_velka
        pocet_mala = 0

    elif mala == "ne" and velka == "ano" and cisla =="ne":
        pocet_velka = delka
        pocet_mala = 0
        pocet_cislo = 0

    else:
        pocet_mala = 0
        pocet_velka = 0
        pocet_cislo = delka

    pre_captcha = ""

    for _ in range(pocet_mala):
        pre_captcha += str(vrat_m_textove_znaky())
        
    for _ in range(pocet_velka):
        pre_captcha += str(vrat_v_textove_znaky())

    for _ in range(pocet_cislo):
        pre_captcha += str(vrat_ciselne_znaky())

    pre_captcha = list(pre_captcha)
    random.shuffle(pre_captcha)

    print("".join(pre_captcha))

def vytvor_captchu():
    while True:
        male = input("Chcete v captche male znaky? (ano/ne):\n")
        if male == "ano" or male == "ne":
            break
        else:
            print("Musite zadat pouze 'ano / ne'. ")

    while True:
        velke = input("Chcete v captche valke znaky? (ano/ne):\n")
        if velke == "ano" or velke == "ne":
            break
        else:
            print("Musite zadat pouze 'ano / ne'. ")

    while True:
        ciselne = input("Chcete v captche ciselne znaky? (ano/ne):\n")
        if ciselne == "ano" or ciselne == "ne":
            break
        else:
            print("Musite zadat pouze 'ano / ne'. ")

    while True:
        delka = input("Jakou delku captchy chcete? (zadejte cislo):\n")
        if delka.isdigit():
            delka = int(delka)
            break
        else:
            print("Musite zadat pouze cislo.")

    main(male,velke,ciselne,delka)

letters = ["a","b","c","d","e","f","g","h",
           "i","j","k","l","m","n","o","p",
           "q","r","s","t","u","v","w","x",
           "y","z"]

# print(vrat_m_textove_znaky())
# print(vrat_v_textove_znaky())
# print(vrat_ciselne_znaky())

# main("ano","ano","ano",13)

vytvor_captchu()