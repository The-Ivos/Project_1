def muj_dekorator(func):
    def wrapper(*args,**kwargs):
        
        login = {"ivos":"vaclavjemujidol",
         "vaclav":"valerie",
         "standa":"memeking"}
        
        username = input("zadej username: ")
        password = input("zadej password: ")

        if password != login[username] or username not in login:
            print("Sorry, spatny heslo nebo uzivatel!")
            exit()

        func(*args,**kwargs)
        print("="*20)
    return wrapper

@muj_dekorator
def say_hi(a):
    return print("Hi",a+"!")

name = "Ivos"

say_hi(name)
