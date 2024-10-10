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

            # TEXT WITHOUT PUNCTUATION
            nopuncttext = texttoex.replace(","," ").replace("."," ").replace("!"," ").replace(";"," ").replace(":"," ").replace("?"," ").split()


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

            # STARS
            stars_dict = {}
            stars_dict_big = {}

            for i in nopuncttext:
                if len(str(i)) < 10:
                    stars_dict[len(str(i))] = 0
                else:
                    stars_dict_big[len(str(i))] = 0

            dict_to_comp = list(stars_dict)
            dict_to_comp_big = list(stars_dict_big)

            for i in nopuncttext:
                for j in dict_to_comp:
                    if len(str(i)) == j:
                        stars_dict[len(str(i))] += 1
                    
            for i in nopuncttext:
                for j in dict_to_comp_big:
                    if len(str(i)) == j:
                        stars_dict_big[len(str(i))] += 1

            pre_stars = list(stars_dict.items())
            pre_stars_big = list(stars_dict_big.items())

            # MAX LINE-LENGTH
            pre_maxlength = pre_stars + pre_stars_big
            notyet_maxlength = []
            for i,b in pre_maxlength:
                notyet_maxlength.append(b)
            maxlength = max(notyet_maxlength)
            

            abeceda = []
            for i,b in pre_stars:
                adda = str((3 - len(str(i))) * " ") + str(i) + "|" + str(b * "*") + str(((maxlength - b) + 2)*" ") + "|" + str(b)
                abeceda.append(adda)

            abeceda_big = []
            for i,b in pre_stars_big:
                adda = str((3 - len(str(i))) * " ") + str(i) + "|" + str(b * "*") + str(((maxlength - b) + 2)*" ") + "|" + str(b)
                abeceda_big.append(adda)

            sorted_abc = sorted(abeceda)
            sorted_abc_big = sorted(abeceda_big)

            print(oddelovac)
            print("LEN|  OCCURENCES  |NR.")
            print(oddelovac)

            for i in sorted_abc:
                print(str(i).replace("'","").replace(",","").strip("()"))

            for i in sorted_abc_big:
                print(str(i).replace("'","").replace(",","").strip("()"))
                

    # WRONG PASSWORD
    elif user in users and password != users[user]:
        print("Wrong password, terminating the program...")  
        user = False  
    
    # UNREGISTERED USER
    else:
        print("Unregistered user, terminating the program...")
        user = False

