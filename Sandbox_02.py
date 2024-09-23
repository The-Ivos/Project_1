Hierro = ["Fernando","Hierro"]
Zidane = ["Zinedine","Zidane"]
Figo = ["Luis","Figo"]
Action = 0
onBall = Hierro

def passing(onBall):
    onBall = Zidane
    changeball(onBall)


def changeball(onBall):
    print(str(onBall[1]) + " is on th ball.")
    print("""What do you want him to do?
          1 - Shoot
          2 - Pass
          3 - Long ball
          4 - Dribble
          5 - Run with the ball 
      """)

changeball(onBall)


Action = str(input("Choose an action: "))
if Action == 1:
    Action = str("Shooting")
elif Action == 2:
    Action = str("Passing")
elif Action == 3:
    Action = str("Long Ball")
elif Action == 4:
    Action = str("Dribbling")
elif Action == 5:
    Action = ("Running with the ball")

if Action == "Passing":
    passing(onBall)

print(onBall)