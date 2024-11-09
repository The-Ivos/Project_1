import random

def vrat_male_textove_znaky():
    return letters[random.randint(0,len(letters)-1)]

def vrat_velke_textove_znaky():
    return letters[random.randint(0,len(letters)-1)].upper()

def vrat_ciselne_znaky():
    return str(random.randint(0,9))

def main(pocet_cisel,pocet_m_pismen,pocet_v_pismen):
    captcha = ""
    for i in range(pocet_cisel):
        captcha += str(vrat_ciselne_znaky())
    
    for i in range(pocet_m_pismen):
        captcha += str(vrat_male_textove_znaky())

    for i in range(pocet_v_pismen):
        captcha += str(vrat_velke_textove_znaky())

    captcha = list(captcha)

    random.shuffle(captcha)

    return print("".join(captcha))
    

def vytvor_captchu():
    while True:
        pocet_cisel = input("Kolik chces v captche cisel?\n")
        pocet_v_pismen = input("Kolik chces v captche velkych pismen?\n")
        pocet_m_pismen = input("Kolik chces v captche malych pismen?\n")

        if pocet_cisel.isdigit() and pocet_m_pismen.isdigit() and pocet_v_pismen.isdigit():
            pocet_cisel = int(pocet_cisel)
            pocet_m_pismen = int(pocet_m_pismen)
            pocet_v_pismen = int(pocet_v_pismen)
            # break
            return main(pocet_cisel,pocet_m_pismen,pocet_v_pismen)
        else:
            print("Vsechna zadani musi byt ciselna. Zkus to znovu!\n")
            input("Press any key to continue...")
            continue




letters = ["a","b","c","d","e","f","g","h",
           "i","j","k","l","m","n","o","p",
           "q","r","s","t","u","v","w","x",
           "y","z"]

# print(vrat_male_textove_znaky())
# print(vrat_velke_textove_znaky())
# print(vrat_ciselne_znaky())

vytvor_captchu()