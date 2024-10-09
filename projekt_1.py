"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ivo Srot
email: srot.ivo@gmail.com
discord: the Ivos
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

user = True

users = {"bob":"123", "ann":"pass123","mike":"password123","liz":"pass123"}
oddelovac = "-" * 40

user = input("username: ")
if user == "":
    user = "anonymus"

while user:
    if (password := input("password: ")) == users.get(user):
        print(oddelovac)
        print("Welcome to the app,",user)
        print("We have 3 texts to be analyzed.")
        print(oddelovac)
        choice = int(input("Enter a number btw. 1 and 3 to select: ")) -1
        if choice not in range(3):
            print("Option",choice,"doesnt exist, terminating program...")
            break
        else:
            texttoex = TEXTS[choice]
            wordcount = len(texttoex.split())
            print("There are", wordcount ,"words in the selected text.")
    elif user in users and password != users[user]:
        print("Wrong password, terminating the program...")  
        user = False  
    else:
        print("Unregistered user, terminating the program...")
        user = False

