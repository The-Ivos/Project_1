def type_check_decorator(expectedtype):

    def inner(func):

        def wrapper(*args,**kwargs):

            if all(isinstance(arg,expectedtype) for arg in args):

                return func(*args,**kwargs)
            return "Invalid input!"

        return wrapper
    
    return inner

# @type_check_decorator(int)
def pocitani(x,y):
    return x + y

a = 2
b = 3

# print(pocitani(a,b)) 

print(type_check_decorator(str)(pocitani)(a,b))
            
        