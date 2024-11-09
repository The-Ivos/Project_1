def muj_dekorator(x,y):
    print(f"Vstupy pro x a y jsou x:{x}, y:{y}.")

    def inner(func):

        print("Summari{:.2f}zation of,".format(x-y),x,"and",y,"= {}".format(x+y))
        # print("Summation of values - {}".format(x+y) )

        def wrapper(*args,**kwargs):
            print(x * y)
            print("*"*20)
            func(*args,**kwargs)
            print("*"*20)

        return wrapper
    
    return inner

# @muj_dekorator(2,3)
def my_func(*args):
    for i in args:
        print(i)
    

muj_dekorator(2,3)(my_func)("Zdar","Ivosu","Dobry")



           
