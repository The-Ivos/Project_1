Hierro = ("Fernando","Hierro","4","defender")
Zidane = ("Zinedine","Zidane","5","midfielder")
Figo = ("Luis","Figo","10","midfielder")
Raul = ("","Raul","7","attacker")

myTeam = [Hierro, Zidane, Figo, Raul]

defence = [Hierro]
midfield = [Zidane, Figo]
attack = [Raul]

pitch = ("goalkeeper",defence,midfield,attack)

onBall_player = input("""Choose a player:
Hierro,
Zidane,
Figo,
Raul
                      """)
if onBall_player == "Hierro":
   onBall_player = Hierro
elif onBall_player == "Zidane":
   onBall_player = Zidane
elif onBall_player == "Figo":
   onBall_player = Figo
else:
   onBall_player = Raul

onBall = myTeam
where_ball = "somewhere"

def change(x):
   global where_ball
   where_ball = pitch[x]

def pitch_ball(player):
   if player in pitch[3]:
      return change(3) 
   elif player in pitch[2]:
      return change(2)
   elif player in pitch[1]:
      return change(1)
   
pitch_ball(onBall_player)

def mid_move():
 print(onBall_player[1],"is with the ball in midfield.")
 move_where = input("Where do you want to move? ")
 if move_where == "up":
    defence.insert(0,midfield.pop(midfield.index(onBall_player)))
    def_move()
 elif move_where == "down": 
    attack.insert(0,midfield.pop(midfield.index(onBall_player)))
    att_move()

def def_move():
 print(onBall_player[1],"is with the ball in defence.")
 move_where = input("Where do you want to move? ")
 if move_where == "up":
     print("You cannot go to goalkeeper.")
     def_move()
 elif move_where == "down": 
    midfield.insert(0,defence.pop(defence.index(onBall_player)))
    mid_move()

def att_move():
 print(onBall_player[1],"is with the ball in attack.")
 move_where = input("Where do you want to move? ")
 if move_where == "up":
    midfield.insert(0,attack.pop(attack.index(onBall_player)))
    mid_move()
 elif move_where == "down": 
    print("There is only goalkeeper.")
    att_move()

while onBall == myTeam and where_ball == midfield:
   mid_move()

while onBall == myTeam and where_ball == defence:
   def_move()

while onBall == myTeam and where_ball == attack:
   att_move()