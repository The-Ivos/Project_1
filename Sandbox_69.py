import math
functions = []

def register_user_function(func):
    functions.append(func)


def shout(x):
    "shouts an text - param"
    return x.upper()

def whisper(x):
    return x.lower()

def greet(func, text):
    return func(text)

def print_help():
    lresult = ''
    for index, func in enumerate(functions):
        lresult += '\n' + str(index) + ' - ' + func.__name__
        if func.__doc__ != None:
            lresult += ': ' + func.__doc__
    return lresult

register_user_function(shout)
register_user_function(whisper)
register_user_function(greet)
register_user_function(math.atan)

print('type some oh those:' + print_help())

chose = input('type a number of function')
func = functions[int(chose)]

print(f'Well done, you have chosen the "{func.__name__}"')

print(func(input('Enter the text you want to modify')))