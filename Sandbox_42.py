import projekt_2_forimp
import os

def games():
    os.system("cls")
    print("""Hello, choose your game:
          
          1 - Bulls and Cows
          2 - Tic Tac Toe
""")
    choose_game = input("Choose your game (1 or 2): ")
    return choose_game

while True:
    choose_game = games()
    if choose_game.lower() == "bulls and cows" or choose_game.lower() == "tic tac toe":
        break
    elif choose_game.isdigit() and int(choose_game) in range(1,3):
        break
    else:
        print("""
This game isnt present in the menu.\nTry again!""")
        input("""
Press any key to continue...""")
        
if choose_game == "1" or choose_game == "bulls and cows":
    projekt_2_forimp.game()


        

# bulls_and_cows(number)
