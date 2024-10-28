from random import randint

# CREATING THE FIRST NUMBER WHICH CANNOT BE 0
first_num = str(randint(1,9))
pre_nums = []
# trash_nums = []

# CREATING THE REST (3) UNIQUE NUMBERS
while len(pre_nums) != 3:
    a = randint(0,9)
    if str(a) in pre_nums or str(a) == first_num:
        # trash_nums.append(a) 
        continue
    else:
        pre_nums.append(str(a))

print(pre_nums)

# JOINING THE NUMBER IN ONE
nums = "".join(pre_nums)
number = first_num + nums

oddelovac = "-"*60

print("Hi There!")
print(oddelovac)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(oddelovac)

print(number)
print("Guess the 4-digit number (or 'q' for quit):")

# START GUESSES
guesses = 1

# LOOP FOR MAIN GUESSING
while True:

    # USER INPUT LOOP
    while True:
        
        # LISTS FOR CONDITION LOOPS 
        ok_nums = []
        notunique = []
        notdigit = []

        #USER INPUT
        print(oddelovac)
        guess = input("")
        
        # LOOP FOR NOT DIGIT INPUT
        for i in guess:
            if not i.isdigit():
                notdigit.append(i)


        # LOOP FOR NOT UNIQUE NUMBERS IN USER INPUT
        for i in guess:
            if i not in ok_nums:
                ok_nums.append(i)
            else:
                notunique.append(i)

        # QUIT CONDITION
        if guess.lower() == "q":
            print("Ok. Bye!")
            exit()

        # INPUT HAS TO BE ONLY NUMBERS
        elif len(notdigit) > 0:
            print("Number cannot include letters.\nTry again!")
        
        # NUMBER CANNOT START WITH 0
        elif guess.startswith("0"):
            print("Number cannot start with 0.\nTry again!")
        
        # NUMBER HAS TO BE 4 DIGITS ONLY
        elif len(guess) != 4:
            print("Number has to have 4 digits.\nTry again!")
        
        # ALL NUMBERS IN INPUT HAS TO BE UNIQUE
        elif len(notunique) > 0:
            print("All numbers has to be unique.\nTry again!")
        
        # ALL CONDITIONS OK
        else:
            break
 

    # CONVERTING THE NUMBER TO LIST FOR INDEX SEARCHING
    strnumber = list(number)

    # RESET START VALUES
    bulls = 0
    cows = 0
    index = -1

    # MAIN LOOP
    for i in guess:
        index +=1
        if i in strnumber and i == strnumber[index]:
            bulls +=1
        elif i in strnumber:
            cows +=1

    # CORRECTING THE SPELLING ACCORDING TO THE COUNTS
    textbulls = "bulls"
    textcows = "cows"

    if bulls == 1:
        textbulls = "bull"
    if cows == 1:
        textcows = "cow"
    
    # WINNING CONDITION
    if bulls == 4:
        print("Correct, you've guessed the right number")
        print("in " + str(guesses) + " guesses!")
        print(oddelovac)
        print("That's amazing!")
        break

    # SCORE AFTER EVERY GUESS    
    print(str(bulls) + " " + textbulls + ", " + str(cows) + " " + textcows)

    guesses +=1



