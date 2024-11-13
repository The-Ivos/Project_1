bigdict = {}

Header = ["Jersey","Name","Surname","Position","Nationality"]
Casillas = [1,"Iker","Casillas","goalkeeper","Spain"]
Zidane = [5,"Zinedine","Zidane","midfielder","France"]
Hierro = [4,"Fernando","Hierro","defender","Spain"]

Players = [Casillas,Zidane,Hierro]

# for i in range(len(Players)):
#     for j in range(len(Header)):

#         Players[i].insert(j*2,Header[j])

Newplayers = ""
for i in Players:
    Newplayers += ",".join(map(str,i))+"\n"

print(Newplayers.strip())


open("players.csv","w",encoding="utf-8").close()
with open("players.csv","w",encoding="utf-8") as file:

    file.write(",".join(Header)+"\n")

    for i in Players:
        file.write(",".join(map(str,i))+"\n")
    














# print(bigdict)