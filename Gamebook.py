import os

kinds = { 
"warrior" : {"name" : "Lopez",
           "HP": 35,
           "Defence": 6,
           "Attack": 10,
           },

"mage" : {"name" : "Sabrina",
           "HP": 80,
           "Defence": 1,
           "Attack": 3,
           },

"vampire" : {"name" : "Moleth",
           "HP": 12,
           "Defence": 3,
           "Attack": 7,
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

kind = ""


# START GAME
while kind == "":
    os.system('cls')
    print(separator)
    for i,b in enument:
        print(i,b)
    print(separator)

    kind = input("""Choose your kind (or 'Q' for quit.): """) 
    if kind.isdigit():
        kind = int(kind)
        if int(kind) not in range(1,len(enument) + 1):
            print(errorator + "\nNot in the menu above. Choose again.")
            anykey()
            kind = ""
        else:
            kind = nrenument[kind]
    elif kind.lower() != "q":
        if kind.lower() not in listkeys:
            print(errorator + "\nNot in the menu above. Choose again.")
            anykey()
            kind = ""
        else:
            kind = kind.lower()
# Q for QUIT
if kind.lower() == "q":
    exit("Bye")

print(kinds[kind])
