import json
import os

def main():
    os.system("cls")
    print(f"""
==============================
WELCOME TO THE CHAT FOR LOSERS          
==============================
          
Start with login or register new user:
          
          1) LOGIN
          2) REGISTER NEW USER

          Q) QUIT

""")
    choice = input("Choose login(1),register new user(2) or (Q)uit:\n")

    while choice.lower() not in "12q":
        print("Please choose: '1', '2' or 'Q':")
        choice = input("")

    if choice == "1":
        return login()
    elif choice == "2":
        return register_user("")
    else:
        os.system("cls")
        print("See ya next time!")
        exit()
    
def login():
    os.system("cls")
    with open("users.json","r",encoding="utf-8") as file:
        content = json.load(file)

        username = input("username: ")

        while username not in content:
            new_reg = input(f"User not registered. Do you want to register new user {username}?\n")

            if new_reg.lower() == "yes":
                register_user(username)



        print(content)

def register_user(x):
    with open("users.json","r",encoding="utf-8") as users_file:
        reg_users = json.load(users_file)
   
  
    wrong_username = f"Choose your username or 'CANCEL' for cancel:"
    
    # check the user name
    while x == "":
        os.system("cls")
        print(wrong_username)
        x = input("username: ")

        if x == "":
            wrong_username = f"Username cannot be empty. Choose your username or 'CANCEL' for cancel:"
        elif x not in reg_users.keys():
            print(f"{x} not there")
            input("Press any key to cont")
            break
        else:
            wrong_username = f"Username {x} already exists! Choose another username or 'CANCEL' for cancel:"
            print(f"{x} there")
            input("Press any key to cont")
            x = ""
    return interlogin(x,"nopass")


def interlogin(x,y):
    if x.lower() == "cancel" or y.lower() == "cancel":
        return main()
    elif y == "nopass":
        return register_password(x)
    else:
        return register_account(x,y)

    
def register_password(x):
    os.system("cls")
    print(f"Choose your password for user {x} or 'CANCEL' for cancel:")
    password = input("password: ")

    return interlogin(x,password)

def register_account(x,y):
    os.system("cls")
    with open("users.json","r",encoding="utf-8") as file:
        content = json.load(file)

        content[x] = y

    with open("users.json","w",encoding="utf-8") as file:
        json.dump(content,file)

        print(f"""Thank you for your registration!
              
              
Your username is: {x}
Your password is: {y}


""")
        input("Press any key to continue to the home screen...")

        return main()


main()    

# register_user()

