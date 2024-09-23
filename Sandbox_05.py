Hierro = ("Fernando","Hierro")
Zidane = ("Zinedine","Zidane")

onBall = Hierro

metaAction = "Passing"

print(onBall[1])
print(metaAction)

def Action(onBall):
    print(onBall[1] + " is on the ball.")
    metaAction = input("What is he gonna do? ")
    if metaAction == "Passing":
        onBall = Zidane
        Action(onBall)
    elif metaAction == "Shooting":
        print(onBall[1] + " shoots!")
 #   elif metaAction == "Passing back":
 #       onBall = Hierro
 #       Action(onBall)
    else:
        print("Whatever")
        

Action(onBall)


print(onBall)