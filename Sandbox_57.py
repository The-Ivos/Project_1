def muj_dekorator(func):
    def wrapped(*args,**kwargs):
        oddelovac = "*"*20
        print(oddelovac)
        func(*args,**kwargs)
        print(oddelovac)
    return wrapped

def shout(x):
    return print(x.upper())

@muj_dekorator
def whisper(x):
    return print(x.lower())

def greet(func):
    return func(text)

def how(): 
    global text
    text = input("What do you wanna say? ")
    inhow = input("How do you wanna say it? Shout or whisper? ")
    if inhow == "shout":
        inhow = shout
    if inhow == "whisper":
       inhow = whisper
    return greet(inhow)



how()



