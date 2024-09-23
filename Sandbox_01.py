import random
Atts = ("Running","Running with the ball","Dribbling","Tackling","Passing","Long balls","Shooting","Aerials")
Zidane = [[3,3,5,3,5,5,4,4],["Zinedine","Zidane"]]
Figo = [[4,3,4,2,5,5,4,3],["Luis","Figo"]]
Hierro = [[2,1,3,5,5,4,4,5],["Fernando","Hierro"]]
onBall = Hierro
Action = 0
Attack = ("Running with the ball","Dribbling","Passing","Long ball","Aerial","Shooting")


print("""1 - Running
2 - Running with the ball
3 - Dribbling
4 - Tackling
5 - Passing
6 - Long balls
7 - Shooting
8 - Aerials
""")

# Skill = int(input("Choose skill (number 1-8): "))

# print(str((Zidane[1])[1]) + ": " + str(Atts[Skill - 1]) + ": " + str((Zidane[1 - 1])[Skill - 1]))

if onBall == Hierro:
    print("Hierro is on the ball.")
    print("""
          1 - Shoot
          2 - Pass
          3 - Long ball
          4 - Dribble
          5 - Run with the ball          
 """)
    Action = int(input("What do you want him to do? "))
    if Action == 1:
        Action = "Shooting"
    elif Action == 2:
        Action = "Passing"
    elif Action == 3:
        Action = "Long ball"
    elif Action == 4:
        Action = "Dribbling"
    elif Action == 5:
        Action = "Running with the ball"
    
 #   Action = str(Attack[random.randrange(0, 5)])
 #   print(Action)
  
if Action == "Shooting":
    print(str((onBall[1])[1]) + " shoots!")
elif Action == "Passing":
    print(str((onBall[1])[1]) + " passes the ball. There is Figo.")
    onBall = Figo
elif Action == "Long ball":
    print(str((onBall[1])[1]) + " sends a long ball!")
elif Action == "Dribbling":
    print(str((onBall[1])[1]) + " tries to dribble the opponent!")
elif Action == "Running with the ball":
    print(str((onBall[1])[0]) + " " + str((onBall[1])[1]) + " keeps the ball and tries to proceed forward.")


if onBall == Figo:
    print("Figo is on the ball.")
    print("""
          1 - Shoot
          2 - Pass
          3 - Long ball
          4 - Dribble
          5 - Run with the ball          
 """)
    Action = int(input("What do you want him to do? "))
    if Action == 1:
        Action = "Shooting"
    elif Action == 2:
        Action = "Passing"
    elif Action == 3:
        Action = "Long ball"
    elif Action == 4:
        Action = "Dribbling"
    elif Action == 5:
        Action = "Running with the ball"
    
 
if Action == "Shooting":
    print(str((onBall[1])[1]) + " shoots!")
elif Action == "Passing":
    print(str((onBall[1])[1]) + " passes the ball. There is Zidane.")
    onBall = Zidane
elif Action == "Long ball":
    print(str((onBall[1])[1]) + " sends a long ball!")
elif Action == "Dribbling":
    print(str((onBall[1])[1]) + " tries to dribble the opponent!")
elif Action == "Running with the ball":
    print(str((onBall[1])[0]) + " " + str((onBall[1])[1]) + " keeps the ball and tries to proceed forward.")

if onBall == Zidane:
    print("Zidane is on the ball.")
    print("""
          1 - Shoot
          2 - Pass
          3 - Long ball
          4 - Dribble
          5 - Run with the ball          
 """)
    Action = int(input("What do you want him to do? "))
    if Action == 1:
        Action = "Shooting"
    elif Action == 2:
        Action = "Passing"
    elif Action == 3:
        Action = "Long ball"
    elif Action == 4:
        Action = "Dribbling"
    elif Action == 5:
        Action = "Running with the ball"
    
 #   Action = str(Attack[random.randrange(0, 5)])
 #   print(Action)
  
if Action == "Shooting":
    print(str((onBall[1])[1]) + " shoots!")
elif Action == "Passing":
    print(str((onBall[1])[1]) + " passes the ball. There is Hierro.")
    onBall = Hierro
elif Action == "Long ball":
    print(str((onBall[1])[1]) + " sends a long ball!")
elif Action == "Dribbling":
    print(str((onBall[1])[1]) + " tries to dribble the opponent!")
elif Action == "Running with the ball":
    print(str((onBall[1])[0]) + " " + str((onBall[1])[1]) + " keeps the ball and tries to proceed forward.")

# if Ball == Hierro:
#    print(str((Hierro[1])[1]) + ": " + str(Atts[random.randrange(1, 8)]))

