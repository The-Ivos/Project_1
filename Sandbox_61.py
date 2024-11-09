def muj_dekorator(like):
    print("Inside dekorator")

    def inner(func):
        print("Inside inner")
        print("I like",like)

        def wrapper():
            print("Inside wrapper")
            func()
            print("end of wrapper")
            print("Do you also like",like,"?")

        return wrapper
    
    return inner

@muj_dekorator("Ivos")
def add():
    print("This is inside the real function")


add()
        