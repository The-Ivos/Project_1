answer = "NO"
name = "Ivos"

def greet(name):
    print("Zdar " + name + "!")
    answer = input("Wanna use another name? YES/NO: ")
    if answer == "YES":
        name = input("What is your name then? ")
        greet(name)
        return name
    else:
        print("Ok, bye!")
        return name
     

greet(name)
print(name)