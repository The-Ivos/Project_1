Hierro = ("Fernando","Hierro","4","defender")
Zidane = ("Zinedine","Zidane","5","midfielder")
Figo = ("Luis","Figo","10","midfielder")
Raul = ("","Raul","7","attacker")

myTeam = [Hierro, Zidane, Figo, Raul]

defence = [Hierro]
midfield = [Zidane, Figo]
attack = [Raul]

onBall = myTeam
onBall_player = Hierro
where_ball = midfield

post = len(where_ball)
post_c = len(where_ball)


while post_c != 0:
    print(where_ball[abs(post_c - post)][1])
    post_c = post_c -1
