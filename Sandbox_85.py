def funkce_2():
    print("And I belong to funkce 2.")

def funkce_1(a):
    if a > 5:
        return funkce_2()

    print("I am print from funkce 1.")

# def funkce_1(a):
#     if a > 5:
#         return funkce_2()

#     print("Nothing happened")

a = 6

funkce_1(a)