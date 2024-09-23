Hierro = ("Fernando","Hierro","4")
Zidane = ("Zinedine","Zidane","5")
Figo = ("Luis","Figo","10")
Raul = ("Raul","Gonzales","7")

myTeam = [Hierro, Zidane, Figo, Raul]

defence = [Hierro]
midfield = [Figo]
attack = [Raul, Zidane]

onBall = myTeam
onBall_player = Hierro
where_player = defence
where_ball = defence

while onBall == myTeam and where_ball == defence:
    print(onBall_player[0],"has a ball!")
    print("He can pass the ball forward to:",midfield)
    onBall_player = input("Whom do you want him to pass the ball? ")
    if onBall_player == "Zidane":
        onBall_player = Zidane
        if onBall_player in midfield:
            where_ball = midfield
        elif onBall_player in defence:
            where_ball = defence
        elif onBall_player in attack:
            where_ball = attack

while onBall == myTeam and where_ball == midfield:
    print(onBall_player[0],"Now has the ball in",where_ball,".")
    onBall = "opponent"

print(onBall_player,where_ball)



