def game():
    player_1_turn()
        
def game_check(a):
    rounds.append("round")
    if top_line_values[0] == a and top_line_values[1] == a and top_line_values[2] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif middle_line_values[0] == a and middle_line_values[1] == a and middle_line_values[2] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif bottom_line_values[0] == a and bottom_line_values[1] == a and bottom_line_values[2] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif top_line_values[0] == a and middle_line_values[0] == a and bottom_line_values[0] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif top_line_values[1] == a and middle_line_values[1] == a and bottom_line_values[1] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif top_line_values[2] == a and middle_line_values[2] == a and bottom_line_values[2] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif top_line_values[0] == a and middle_line_values[1] == a and bottom_line_values[2] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif top_line_values[2] == a and middle_line_values[1] == a and bottom_line_values[0] == a:
        show_table()
        print("Player",a,"wins!")
        exit()
    elif len(rounds) == 9:
        show_table()
        print("It's a draw!")
        exit()



def show_table():

    top_line = "|",top_line_values[0],"|",top_line_values[1],"|",top_line_values[2],"|"
    middle_line = "|",middle_line_values[0],"|",middle_line_values[1],"|",middle_line_values[2],"|"
    bottom_line = "|",bottom_line_values[0],"|",bottom_line_values[1],"|",bottom_line_values[2],"|"

    top_line = " ".join(top_line)
    middle_line = " ".join(middle_line)
    bottom_line = " ".join(bottom_line)

    print("+---+---+---+")
    print(top_line)
    print("+---+---+---+")
    print(middle_line)
    print("+---+---+---+")
    print(bottom_line)
    print("+---+---+---+")


def player_1_input():
    while True:
        choose = input("Choose a position (1-9):\n")
        if choose.isdigit() and choose != "0" and len(choose) == 1:
            break
        else:
            show_table()
            print("Wrong input.\nTry again!")
            print("")
            print("Player X:")
            
    return choose


def player_2_input():
    while True:
        choose = input("Choose a position (1-9):\n")
        if choose.isdigit() and choose != "0" and len(choose) == 1:
            break
        else:
            show_table()
            print("Wrong input.\nTry again!")
            print("")
            print("Player O:")
            
    return choose


def player_1_turn():

    show_table()

    player_1_choose()


def player_2_turn():

    show_table()

    player_2_choose()


def player_1_choose():
    
    print("Player X:")
    choose = player_1_input()
   
    if choose == "1" and top_line_values[0] == " ":
        top_line_values[0] = "X"
    elif choose == "2" and top_line_values[1] == " ":
        top_line_values[1] = "X"
    elif choose == "3" and top_line_values[2] == " ":
        top_line_values[2] = "X"
    elif choose == "4" and middle_line_values[0] == " ":
        middle_line_values[0] = "X"
    elif choose == "5" and middle_line_values[1] == " ":
        middle_line_values[1] = "X"
    elif choose == "6" and middle_line_values[2] == " ":
        middle_line_values[2] = "X"
    elif choose == "7" and bottom_line_values[0] == " ":
        bottom_line_values[0] = "X"
    elif choose == "8" and bottom_line_values[1] == " ":
        bottom_line_values[1] = "X"
    elif choose == "9"and bottom_line_values[2] == " ":
        bottom_line_values[2] = "X"
    else:
        show_table()
        print("The position is occupied already!\nTry again!")
        print("")
        player_1_choose()

    game_check("X")

    player_2_turn()


def player_2_choose():

    print("Player O:")
    choose = player_2_input()
   
    if choose == "1" and top_line_values[0] == " ":
        top_line_values[0] = "O"
    elif choose == "2" and top_line_values[1] == " ":
        top_line_values[1] = "O"
    elif choose == "3" and top_line_values[2] == " ":
        top_line_values[2] = "O"
    elif choose == "4" and middle_line_values[0] == " ":
        middle_line_values[0] = "O"
    elif choose == "5" and middle_line_values[1] == " ":
        middle_line_values[1] = "O"
    elif choose == "6" and middle_line_values[2] == " ":
        middle_line_values[2] = "O"
    elif choose == "7" and bottom_line_values[0] == " ":
        bottom_line_values[0] = "O"
    elif choose == "8" and bottom_line_values[1] == " ":
        bottom_line_values[1] = "O"
    elif choose == "9"and bottom_line_values[2] == " ":
        bottom_line_values[2] = "O"
    else:
        show_table()
        print("The position is occupied already!\nTry again!")
        print("")
        player_2_choose()

    game_check("O")

    player_1_turn()

rounds = []

top_line_values = [" "," "," "]
middle_line_values = [" "," "," "]
bottom_line_values = [" "," "," "]



game()