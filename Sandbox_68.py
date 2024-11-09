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
    for func in functions:
        lresult += '\n' + func.__name__
        if func.__doc__ != None:
            lresult += ': ' + func.__doc__
    return lresult

register_user_function(shout)
register_user_function(whisper)
register_user_function(greet)
register_user_function(math.atan)

print('type some oh those:' + print_help())