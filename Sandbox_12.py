Hierro = ("Fernando","Hierro","4","defender")
Zidane = ("Zinedine","Zidane","5","midfielder")
Figo = ("Luis","Figo","10","midfielder")
Raul = ("Raul","Gonzales","7","attacker")

myTeam = [Hierro, Zidane, Figo, Raul]

defence = [Hierro]
midfield = [Zidane, Figo]
attack = [Raul]

onBall = myTeam
onBall_player = Hierro
where_player = defence
where_ball = defence

while onBall == myTeam:
    print(onBall_player[1],"is on the ball. There is",midfield[len(midfield)-1][1],"in front of him.")
    onBall = "opponent"