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

punctuation = ".,!:"

user = input("username: ")
if user == "":
    user = "anonymouse"

while user:
    # USER AND PASS CORRECT
    if (password := input("password: ")) == users.get(user):
        print(oddelovac)
        print("Welcome to the app,",user)
        print("We have 3 texts to be analyzed.")
        print(oddelovac)
        
        # TEXT CHOICE
        choice = int(input("Enter a number btw. 1 and 3 to select: ")) -1
        print(oddelovac)

        # TEXT CHOICE DOESNT EXIST
        if choice not in range(3):
            print("Option",choice,"doesnt exist, terminating program...")
            break
        else:
            
            # CHOSEN TEXT
            texttoex = TEXTS[choice]
            
            # TEXT TO LIST
            splittedtext = texttoex.split()

            # LIST TEXT WITHOUT ANY NUMBERS
            total_numberlesstext = splittedtext.copy()
            to_remove = set()
            for i in splittedtext:
                for j in i:
                    if j.isnumeric():
                        to_remove.add(i)
                        remove_list = list(to_remove)
            for i in range(len(remove_list)):
                total_numberlesstext.remove(remove_list[i])

            # WORDCOUNT
            wordcount = len(splittedtext)
            print("There are", wordcount ,"words in the selected text.")
            
            # TITLES
            titles = []
            for i in splittedtext:
                if i[0].isupper():
                    titles.append(i)
            print("There are",(len(titles)),"titlecase words.")

            # UPPERCASE WORDS
            uppercases = []
                        
            for i in total_numberlesstext:
                if i == i.upper():
                    uppercases.append(i)
            
            print("There are",len(uppercases),"uppercase words.")

            # LOWERCASE WORDS
            lowercases = []
                                    
            for i in total_numberlesstext:
                if i == i.lower():
                    lowercases.append(i)
            
            print("There are",len(lowercases),"lowercase words.")      

            # NUMERIC STRINGS
            numericstrings = []

            for i in splittedtext:
                if i.isnumeric():     
                    numericstrings.append(i)

            print("There are",len(numericstrings),"numeric strings.")

            # NUM SUM
            numstosum = []
            for i in numericstrings:
                numstosum.append(int(i))
            summednums = sum(numstosum)
            print("The sum of all the numbers:",summednums)

                

    # WRONG PASSWORD
    elif user in users and password != users[user]:
        print("Wrong password, terminating the program...")  
        user = False  
    
    # UNREGISTERED USER
    else:
        print("Unregistered user, terminating the program...")
        user = False

