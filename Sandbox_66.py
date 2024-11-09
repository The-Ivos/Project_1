import random

def muj_dekorator(your_name):

    def inner(func):

        def wrapper(*args, **kwargs):
            if your_name != "Ivos":
                return your_name+": "+str(func(*args,**kwargs))
            
            return "Drz hubu, Ivosu!"
        
        return wrapper
    
    return inner

def pocitam(cislo1,cislo2):
    return cislo1 + cislo2        

def courtney():
    return "We hate you, bitch!"

def tony():
    return "Fuck you, Tony!"

def ezekiel():
    return "Fuck you, Ezekiel!"

cislo1 = 2
cislo2 = 3

# user_definitions = []

# for i in (" ".join(dir()).split("__ __")[-1].split("__")[1].split(" ")):
#     if i:
#         user_definitions.append(i)

# print(user_definitions)

# print(dir())

# print(locals())

a = locals().get(input("Tony or Ezekiel? "))

print(muj_dekorator(input("What is your name? "))(a)())