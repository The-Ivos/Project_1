def apply(func,value,value2):
    return func(value,value2)


def power(x,y):
    return x ** y

print(apply(power,3,2))