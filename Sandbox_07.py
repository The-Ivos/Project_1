Hierro = (("Fernando","Hierro"),("Spain"),(34))
Zidane = (("Zinedine","Zidane"),("France"),(30))
Figo = (("Luis","Figo"),("Portugal"),(30))
Raul = (("Raul","Gonzales"),("Spain"),(25)) 
New = (("Newname","Newsurname"),("Newcountry"),(int(0))) 
 

person = input("Choose a person: (Zidane, Hierro or Figo): ")
if person == "Zidane":
    person = Zidane
elif person == "Figo":
    person = Figo
elif person == "Hierro":
    person = Hierro
else:
    person = New

print("Hi, I am " + person[0][0] + " from " + person[1] + ".")