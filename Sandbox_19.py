import random

R_Carlos = ("Roberto","Carlos","3","defender",4)
Salgado = ("Michel","Salgado","2","defender",3)
Beckham = ("David","Beckham","23","midfielder",5)

team = (R_Carlos,Salgado,Beckham)

onBall_player = "nobody"
receiver_zero = "nikdo"

def befpass():
    global onBall_player
    if onBall_player not in team:
        onBall_player = input("Choose a player who will do the pass: Beckham, R Carlos or Beckham? ")
        if onBall_player == "Beckham":
            onBall_player = Beckham
        elif onBall_player == "R Carlos":
            onBall_player = R_Carlos
        elif onBall_player == "Salgado":
            onBall_player = Salgado
        else:
            befpass()
        topass()
    global receiver_zero
    print("There is",onBall_player[1],"on the ball.")
    receiver_zero = input("Whom to you want to pass the ball? ")
    topass()

def topass():
    global receiver_zero
    if receiver_zero == onBall_player[1]:
        print("you cannot pass to yourself.")
        befpass()
    elif receiver_zero == "Salgado":
        receiver_zero = Salgado
        passing(onBall_player,receiver_zero)
    elif receiver_zero == "Beckham":
        receiver_zero = Beckham
        passing(onBall_player,receiver_zero)
    elif receiver_zero == "R Carlos":
        receiver_zero = R_Carlos
        passing(onBall_player,receiver_zero)
    else:
        befpass()

def passing(passer,receiver):
    global onBall_player
    passball = passer[4] + random.randint(1,6)
    print(passball)
    if passball >= 6:
        onBall_player = receiver
        befpass()
    else:
        onBall_player = "nobody"
        
befpass()

# passing(onBall_player,receiver_zero)
    
print(onBall_player[1])