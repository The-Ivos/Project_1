import os

os.system('cls')

Hierro = ("Fernando","Hierro","4","defender")
Zidane = ("Zinedine","Zidane","5","midfielder")
Figo = ("Luis","Figo","10","midfielder")
Raul = ("","Raul","7","attacker")
Guti = ("","Guti","14","midfielder")
Helguera = ("Ivan","Helguera","6","defender")
R_Carlos = ("Roberto","Carlos","3","defender")
Salgado = ("Michel","Salgado","2","defender")
Beckham = ("David","Beckham","23","midfielder")
Morientes = ("Fernando","Morientes","9","attacker")

myTeam = [Hierro, Zidane, Figo, Raul]

defence = [Hierro, Helguera, Salgado, R_Carlos]
midfield = [Zidane, Figo, Guti, Beckham]
attack = [Raul, Morientes]

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
 os.system('cls')
 print(onBall_player[1],"is with the ball in midfield.")
 print("There are: ")
 midfield_r = midfield.copy()
 midfield_r.remove(onBall_player)
 for i in range(len(midfield_r)): 
        if i != 0:
            print(midfield_r[i][1], end = ", ")
 print("and",midfield_r[0][1],end="")
 print(" in midfield with him.")
 for i in range(len(defence)):
        if i !=0: 
            print(defence[i][1], end = ", ")
 print("and",defence[0][1],end="")
 print(" in defence.")
 move_where = input("so what do you want to do? ")
 if move_where == "up":
    defence.insert(0,midfield.pop(midfield.index(onBall_player)))
    def_move()
 elif move_where == "down": 
    attack.insert(0,midfield.pop(midfield.index(onBall_player)))
    att_move()
 else:
     mid_move()

def def_move():
 os.system('cls')
 print(onBall_player[1],"is with the ball in defence.")
 print("There are: ")
 defence_r = defence.copy()
 defence_r.remove(onBall_player)
 for i in range(len(defence_r)): 
        if i != 0:
            print(defence_r[i][1], end = ", ")
 print("and",defence_r[0][1],end="")
 print(" in defence with him.")
 for i in range(len(midfield)): 
        if i != 0:
            print(midfield[i][1], end = ", ")
 print("and",midfield[0][1],end="")
 print(" in midfield.")
 move_where = input("so what do you want to do? ")
 if move_where == "up":
     print("You cannot go to goalkeeper.")
     def_move()
 elif move_where == "down": 
    midfield.insert(0,defence.pop(defence.index(onBall_player)))
    mid_move()
 else:
     def_move()

def att_move():
 os.system('cls')
 print(onBall_player[1],"is with the ball in attack.")
 move_where = input("Where do you want to move? ")
 if move_where == "up":
    midfield.insert(0,attack.pop(attack.index(onBall_player)))
    mid_move()
 elif move_where == "down": 
    print("There is only goalkeeper.")
    att_move()
 else:
     att_move()

while onBall == myTeam and where_ball == midfield:
   mid_move()

while onBall == myTeam and where_ball == defence:
   def_move()

while onBall == myTeam and where_ball == attack:
   att_move()