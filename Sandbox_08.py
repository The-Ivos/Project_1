Hierro = (("Fernando","Hierro"),("Spain"),(34))
Zidane = (("Zinedine","Zidane"),("France"),(30))
Figo = (("Luis","Figo"),("Portugal"),(30))
Raul = (("Raul","Gonzales"),("Spain"),(25)) 
Guti = (("Jose Maria","Guti"),("Spain"),(26))
onBall = Hierro

onBall = (input("Choose a player: " ))
if onBall == "Figo":
    onBall = Figo
elif onBall == "Zidane":
    onBall = Zidane
elif onBall == "Raul":
    onBall = Raul
elif onBall == "Guti":
    onBall = Guti
else:
    onBall = Hierro


players = [Hierro, Zidane, Figo, Raul, Guti]
players2 = []


print(str(players).replace("["," ").replace("]"," ").replace("("," ").replace(")"," ").replace(","," ").replace("'"," ").replace("    "," ").replace("  "," "))
print(str(players2).replace("["," ").replace("]"," ").replace("("," ").replace(")"," ").replace(","," ").replace("'"," ").replace("    "," ").replace("  "," "))

print(len(players))
print(len(players2))

move = players2.insert(0, players.pop(players.index(onBall)))



print(str(players).replace("["," ").replace("]"," ").replace("("," ").replace(")"," ").replace(","," ").replace("'"," ").replace("    "," ").replace("  "," "))
print(str(players2).replace("["," ").replace("]"," ").replace("("," ").replace(")"," ").replace(","," ").replace("'"," ").replace("    "," ").replace("  "," "))

print(len(players))
print(len(players2))

print(players)
print(players2)

onBall = (input("Choose a player: " ))
if onBall == "Figo":
    onBall = Figo
elif onBall == "Zidane":
    onBall = Zidane
elif onBall == "Raul":
    onBall = Raul
else:
    onBall = Hierro

move = players2.insert(0, players.pop(players.index(onBall)))


print(str(players).replace("["," ").replace("]"," ").replace("("," ").replace(")"," ").replace(","," ").replace("'"," ").replace("    "," ").replace("  "," "))
print(str(players2).replace("["," ").replace("]"," ").replace("("," ").replace(")"," ").replace(","," ").replace("'"," ").replace("    "," ").replace("  "," "))

print(len(players))
print(len(players2))

print(players)
print(players2)

onBall = (input("Choose a player: " ))
if onBall == "Figo":
    onBall = Figo
elif onBall == "Zidane":
    onBall = Zidane
elif onBall == "Raul":
    onBall = Raul
else:
    onBall = Hierro

insertend = (len(players2))

move = players2.insert(insertend, players.pop(players.index(onBall)))


print(str(players).replace("["," ").replace("]"," ").replace("("," ").replace(")"," ").replace(","," ").replace("'"," ").replace("    "," ").replace("  "," "))
print(str(players2).replace("["," ").replace("]"," ").replace("("," ").replace(")"," ").replace(","," ").replace("'"," ").replace("    "," ").replace("  "," "))

print(len(players))
print(len(players2))

print(players)
print(players2)