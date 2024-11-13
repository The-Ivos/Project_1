def board(x,y):
    diagonal = x * "_|"
    header = f"    {(x) * "__"}"
    
    header_nums = ""
    for i in range(1,x+1):

        if i == 1:
            i = "a"
        if i == 2:
            i = "b"
        if i == 3:
            i = "c"
        if i == 4:
            i = "d"
        if i == 5:
            i = "e"
        if i == 6:
            i = "f"
        if i == 7:
            i = "g"
        if i == 8:
            i = "h"
        if i == 9:
            i = "i"
        if i == 10:
            i = "j"
        if i == 11:
            i = "k"
        if i == 12:
            i = "l"
        if i == 13:
            i = "m"
        if i == 14:
            i = "n"
        if i == 15:
            i = "o"
        if i == 16:
            i = "p"
        if i == 17:
            i = "q"
        if i == 18:
            i = "r"
        if i == 19:
            i = "s"
        if i == 20:
            i = "t"
        if i == 21:
            i = "u"
        if i == 22:
            i = "v"
        if i == 23:
            i = "w"
        if i == 24:
            i = "x"
        if i == 25:
            i = "y"
        if i == 26:
            i = "z"

        header_nums += str(i.upper()) + " "
    
    print(f"    {header_nums}")
    print(header)
    
    for i in range(1,x+1):
       
        print(f"{i:2d} |{diagonal}")
        
    



board(26,26)