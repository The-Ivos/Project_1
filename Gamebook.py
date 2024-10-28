import os

kinds = { 
"warrior" : {"name" : "Lopez",
             "Level": 1,
           "HP": 31,
           "Status" : " OK",
           "Defence": 6,
           "Attack": 10,
           "Speed" : 7,
           "Accuracy" : 9,
           "Attacklist": {"1": {"name": "powerhit"},
                          "2": {"name": "bomb-kick"},
                          "3": {"name" : "guillotine"}}
           },

"mage" : {"name" : "Sabrina",
          "Level" : 7,
           "HP": 80,
           "Status" : "PSN",
           "Defence": 1,
           "Attack": 3,
           "Speed" : 5,
           "Accuracy" : 6,
           "Attacklist": {"1": {"name": "powerhit"},
                          "2": {"name": "bomb-kick"},
                          "3": {"name" : "guillotine"}}
           },

"vampireidort" : {"name" : "Moleth",
                  "Level": 12,
           "HP": 100,
           "Status" : " OK",
           "Defence": 3,
           "Attack": 7,
           "Speed" : 10,
           "Accuracy" : 7,
           "Attacklist": {"1": {"name": "powerhit"},
                          "2": {"name": "bomb-kick"},
                          "3": {"name" : "guillotine"}}
           },
}

enemies = {
"giant rat" : {"name" : "Giant rat",
           "HP": 13,
           "Defence": 4,
           "Attack": 5,
           "Speed" : 2,
           "Accuracy" : 4
           },

}

# START VARS
listkeys = list(kinds.keys())
textkeys = str(listkeys).replace("['","").replace("', '"," ").replace("']","")

ent = list(kinds)
enument = list(enumerate(ent,1))
nrenument = dict(enument)

separator = "=" * 40
errorator = "-" * 40

def anykey():
    input('''
Press any key for continue...''')
    
def cleascreen():
    os.system('cls')

kind = ""
wronginp = False

# PLAYER SETTINGS
while kind == "":
    cleascreen()
    if wronginp:
        print("Thats not in the menu. Choose again.")
    print(separator)
    for i,b in enument:
        print(i,b)
    print(separator)

    kind = input("""Choose your kind (or 'Q' for quit.): """) 
    if kind.isdigit():
        kind = int(kind)
        if int(kind) not in range(1,len(enument) + 1):
            wronginp = True
            kind = ""
        else:
            kind = nrenument[kind]
    elif kind.lower() != "q":
        if kind.lower() not in listkeys:
            wronginp = True
            kind = ""
        else:
            kind = kind.lower()
# Q for QUIT
if kind.lower() == "q":
    exit("Bye")

cleascreen()
print("You have chosen to be a " + kind + ".")
kinds[kind]["name"] = ""
while kinds[kind]["name"] == "" or len(kinds[kind]["name"]) > 12:
    kinds[kind]["name"] = input("Now choose your name (max length 12 characters): ")
print("")
print("So you are a " + kind + " called " + kinds[kind]["name"] + ".")
print("")
print(separator)
print("Welcome to the World of Ivosland!".upper().center(40))
print(separator)
anykey()

#THE GAME
cleascreen()
enemy_kind = "giant rat"
hero = kinds[kind]
enemy = enemies[enemy_kind]
hero_name = hero["name"]
enemy_name = enemy["name"]
current_hp = hero["HP"]


def heroattack():
    cleascreen()
    menulength = hero["HP"]
    if enemy["HP"] > hero["HP"]:
        menulength = enemy["HP"]
    if menulength % 2 == 1:
        menulength +=1
    current_hero_hp = hero["HP"]
    print(hero_name + "'s move:")
    anykey()
    cleascreen()
    print("You are in the battle with " + enemy_name +"!")
    print("-"*(menulength +8))
    print(f"|{hero_name.upper():<{(int(menulength/2))}} {kind:>{(int(menulength/2)+4)}} |")
    print("| HP: " + hero["HP"]*"*" + int(menulength - hero["HP"])*" " + " |")
    print(f"|{current_hero_hp:>{(int(menulength +4)-len(str(hero['HP'])))}}/{hero['HP']} |")
    print("-"*(menulength +8))
    print(f"|{enemy_name.upper():<{int(menulength/2)}} {enemy_kind:>{int(menulength/2)+4}} |")
    print("| HP: " + enemy["HP"]*"*" + int(menulength - enemy["HP"])*" " + " |")
    print("-"*(menulength + 8))

    current_hero_hp = 23
    # hp_stars_calc = (current_hero_hp / hero["HP"]) * 100
    hp_stars_calc = (current_hero_hp / hero["HP"]) * 100

    hp_starsing = 1

    print(hp_stars_calc)

    if int(hp_stars_calc) in range(96,101):
        hp_starsing = 30
    elif int(hp_stars_calc) in range(92,96):
        hp_starsing = 29
    elif int(hp_stars_calc) in range(86,92):
        hp_starsing = 28
    elif int(hp_stars_calc) in range(82,86):
        hp_starsing = 27
    elif int(hp_stars_calc) in range(79,82):
        hp_starsing = 26
    elif int(hp_stars_calc) in range(76,79):
        hp_starsing = 25
    elif int(hp_stars_calc) in range(72,69):
        hp_starsing = 24
    elif int(hp_stars_calc) in range(69,72):
        hp_starsing = 23
    elif int(hp_stars_calc) in range(66,69):
        hp_starsing = 22
    elif int(hp_stars_calc) in range(63,66):
        hp_starsing = 21
    elif int(hp_stars_calc) in range(60,63):
        hp_starsing = 20
    elif int(hp_stars_calc) in range(57,60):
        hp_starsing = 19
    elif int(hp_stars_calc) in range(55,57):
        hp_starsing = 18
    elif int(hp_stars_calc) in range(52,55):
        hp_starsing = 17
    elif int(hp_stars_calc) in range(48,52):
        hp_starsing = 16
    elif int(hp_stars_calc) in range(44,48):
        hp_starsing = 15
    elif int(hp_stars_calc) in range(40,44):
        hp_starsing = 14
    elif int(hp_stars_calc) in range(36,40):
        hp_starsing = 13
    elif int(hp_stars_calc) in range(33,36):
        hp_starsing = 12
    elif int(hp_stars_calc) in range(30,33):
        hp_starsing = 11
    elif int(hp_stars_calc) in range(26,30):
        hp_starsing = 10
    elif int(hp_stars_calc) in range(23,26):
        hp_starsing = 9
    elif int(hp_stars_calc) in range(20,23):
        hp_starsing = 8
    elif int(hp_stars_calc) in range(17,20):
        hp_starsing = 7
    elif int(hp_stars_calc) in range(14,17):
        hp_starsing = 6
    elif int(hp_stars_calc) in range(11,14):
        hp_starsing = 5
    elif int(hp_stars_calc) in range(8,11):
        hp_starsing = 4
    elif int(hp_stars_calc) in range(6,8):
        hp_starsing = 3
    elif int(hp_stars_calc) in range(4,6):
        hp_starsing = 2
    elif int(hp_stars_calc) in range(1,4):
        hp_starsing = 1
    else:
        hp_starsing = 0

    hp_stars = int(hp_starsing) * "*"

    print("|",hero_name.upper(),(12 - (len(hero_name))) * " ",kind,(12 - (len(kind))) * " ","LEVEL:",(2-len(str(hero["Level"]))) * " ",hero["Level"],"|")
    print("| HP:",hp_stars,(30 - (len(hp_stars))) * " " + hero["Status"],"|")
    print(f"| {current_hero_hp:>28}/{current_hp}        |")
    

    print("What is going to be your next move?")
    print(separator)
    for i in range(1,len(hero["Attacklist"])+1):
        print(i,hero["Attacklist"][str(i)]["name"])
    

def enemyattack():
    cleascreen()
    print(enemy_name + "'s move!")
    anykey()


def battle(a,b):
    print("Its a battle betwen",a["name"],"and",b["name"],"!")
    anykey()
    if a["Speed"] >= b["Speed"]:
        heroattack()
    else:
        enemyattack()


battle(hero,enemy)

