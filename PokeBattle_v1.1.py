import random
import os

os.system('cls')

Bulbasaur = {"name": "BULBASAUR",
            "type": "grass",
            "attacks": {
                "first" : {"tackle" : {"name": "TACKLE", "power": 3, "acc": 4, "stc": "OK","type": "normal"}}, 
                "second" : {"vine whip" : {"name": "VINE WHIP", "power": 4, "acc": 4, "stc": "OK","type": "grass"}},
                "third" : {"poison powder" : {"name": "POISON POWDER", "power": 0, "acc": 3, "stc": "PSN","type": "poison"}},
                "fourth" : {"sleep powder" : {"name": "SLEEP POWDER", "power": 0, "acc": 3, "stc": "SLP","type": "grass"}}
                },
            "HP": 29,
            "status": "OK",
            "speed":1}

Squirtle = {"name": "SQUIRTLE",
            "type": "water",
            "attacks": {
                "first" : {"tackle" : {"name": "TACKLE", "power": 3, "acc": 4, "stc": "OK","type": "normal"}}, 
                "second" : {"bubble" : {"name": "BUBBLE", "power": 4, "acc": 4, "stc": "OK","type": "water"}},
                "third" : {"water gun" : {"name": "WATER GUN", "power": 5, "acc": 3, "stc": "OK","type": "water"}},
                "fourth" : {"skull bash" : {"name": "SKULL BASH", "power": 7, "acc": 2, "stc": "OK","type": "normal"}}
                },
            "HP": 25,
            "status": "OK",
            "speed": 2}

Pidgey = {"name": "PIDGEY",
            "type": "flying",
            "attacks": {
                "first" : {"gust" : {"name": "GUST", "power": 3, "acc": 4, "stc": "OK","type": "flying"}}, 
                "second" : {"peck" : {"name": "PECK", "power": 4, "acc": 4, "stc": "OK","type": "flying"}},
                "third" : {"sing" : {"name": "SING", "power": 0, "acc": 3, "stc": "SLP","type": "normal"}},
                "fourth" : {"wing slap" : {"name": "WING SLAP", "power": 5, "acc": 2, "stc": "OK","type": "flying"}}
                },
            "HP": 21,
            "status": "OK",
            "speed": 5}

Pikachu = {"name": "PIKACHU",
            "type": "electric",
            "attacks": {
                "first" : {"tackle" : {"name": "TACKLE", "power": 3, "acc": 4, "stc": "OK","type": "normal"}}, 
                "second" : {"thundershock" : {"name": "THUNDERSHOCK", "power": 4, "acc": 4, "stc": "OK","type": "electric"}},
                "third" : {"sing" : {"name": "SING", "power": 0, "acc": 3, "stc": "SLP","type": "normal"}},
                "fourth" : {"toxic" : {"name": "TOXIC", "power": 1, "acc": 4, "stc": "PSN","type": "poison"}}
                },
            "HP": 24,
            "status": "OK",
            "speed": 3}

Charmander = {"name": "CHARMANDER",
            "type": "fire",
            "attacks": {
                "first" : {"scratch" : {"name": "SCRATCH", "power": 3, "acc": 4, "stc": "OK","type": "normal"}}, 
                "second" : {"ember" : {"name": "EMBER", "power": 3, "acc": 4, "stc": "OK","type": "fire"}},
                "third" : {"bite" : {"name": "BITE", "power": 4, "acc": 3, "stc": "OK","type": "dark"}},
                "fourth" : {"flame wheel" : {"name": "FLAME WHEEL", "power": 5, "acc": 2, "stc": "OK","type": "fire"}}
                },
            "HP": 28,
            "status": "OK"
            ,"speed": 4}

Sandshrew = {"name": "SANDSHREW",
            "type": "ground",
            "attacks": {
                "first" : {"scratch" : {"name": "SCRATCH", "power": 3, "acc": 4, "stc": "OK","type": "normal"}}, 
                "second" : {"rock throw" : {"name": "ROCK THROW", "power": 3, "acc": 4, "stc": "OK","type": "rock"}},
                "third" : {"mud-slap" : {"name": "MUD-SLAP", "power": 3, "acc": 4, "stc": "OK","type": "ground"}},
                "fourth" : {"earthquake" : {"name": "EARTHQUAKE", "power": 6, "acc": 3, "stc": "OK","type": "ground"}}
                },
            "HP": 26,
            "status": "OK"
            ,"speed": 4}

myPokemon = Squirtle
foePokemon = Bulbasaur

choice = [Bulbasaur["name"], Charmander["name"], Squirtle["name"], Pikachu["name"], Pidgey["name"], Sandshrew["name"]]

cont = "Press ENTER to continue..."

onTurn = myPokemon

def foeAttack():
   os.system('cls')
   if myPokemon["status"] == "PSN":
       print(myPokemon["name"],"is hurt by poison!")
       print("")
       print(input(cont))
       myPokemon.update({"HP" : myPokemon["HP"] -2})
       os.system('cls')
   if foePokemon["status"] == "PSN":
       print(foePokemon["name"],"is hurt by poison!")
       print("")
       print(input(cont))
       foePokemon.update({"HP" : foePokemon["HP"] - 2})
   os.system('cls')  
   if foePokemon["status"] == "SLP":
       sleep = random.randint(1,3)
       if sleep <= 2:
          print(foePokemon["name"],"sleeps!")
       else:
          print(foePokemon["name"],"woke up!") 
          foePokemon.update({"status" : "OK"})    
       print("")
       print(input(cont))
       os.system('cls') 
   if foePokemon["HP"] <= 0 or myPokemon["HP"] <= 0:
      endgame()
      exit()    
   print("=" * 35)
   print(myPokemon["name"] + "  HP: " + str(myPokemon["HP"]) + "   status: " + myPokemon["status"])
   print(foePokemon["name"]+ "  HP: " + str(foePokemon["HP"]) + "   status: " + foePokemon["status"])
   print("=" * 35)
   print("")
   print("enemy",foePokemon["name"],"is going to attack!")
   print("")
   print(input(cont))
   os.system('cls')
   foeAttackNum = random.randint(1,len(foePokemon["attacks"].keys()))
   global eff
   if foeAttackNum == 1:
    # print(foePokemon["name"],"used",str(foePokemon["attacks"]["first"]).replace("'","").replace("{","").replace("}","").split()[2].replace(",","!"))
    foeAtt = str(foePokemon["attacks"]["first"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[5]
    foeAcc = int(str(foePokemon["attacks"]["first"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[10])
    foePwr = int(str(foePokemon["attacks"]["first"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[8])
    foeTyp = str(foePokemon["attacks"]["first"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[17]
    foeSta = str(foePokemon["attacks"]["first"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[13]
    effic(myPokemon["type"],foePokemon["attacks"]["first"][foeAtt.lower()]["type"])
    foeAccuracy = foeAcc + random.randint(1,6)
    if foePokemon["status"] == "SLP":
        print("")
        print("ZzZzZ...")
        print(input(cont))
    elif foeAccuracy >= 7 and myPokemon["status"] == "OK":
       print(foePokemon["name"],"used",foeAtt,"!")
       if eff == 2:
           print("It's super effective!")
       if eff == 0:
            print("But it didn't work.")
       if eff == 0.5:
            print("It's not very effective.")
       print("")
       print(input("Press ENTER to continue..."))
       myPokemon.update({"HP" : myPokemon["HP"] - int(foePwr*eff)})
       if eff != 0:
        myPokemon.update({"status" : foeSta})
    elif foeAccuracy >= 7:
        print(foePokemon["name"],"used",foeAtt,"!")
        if eff == 2:
           print("Its super effective!")
        if eff == 0:
            print("But it didn't work.")
        if eff == 0.5:
            print("It's not very effective.")   
        print("")
        print(input("Press ENTER to continue..."))
        myPokemon.update({"HP" : myPokemon["HP"] - int(foePwr*eff)})
    else:
        print(foePokemon["name"],"used",foeAtt,"! But...")
        print(foePokemon["name"],"attack missed!")
        print("")
        print(input("Press ENTER to continue..."))
           
   if foeAttackNum == 2:
    # print(foePokemon["name"],"used",str(foePokemon["attacks"]["second"]).replace("'","").replace("{","").replace("}","").split()[2].replace(",","!"))
    foeAtt = str(foePokemon["attacks"]["second"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[5]
    foeAcc = int(str(foePokemon["attacks"]["second"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[10])
    foePwr = int(str(foePokemon["attacks"]["second"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[8])
    foeTyp = str(foePokemon["attacks"]["second"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[17]
    foeSta = str(foePokemon["attacks"]["second"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[13]
    effic(myPokemon["type"],foePokemon["attacks"]["second"][foeAtt.lower()]["type"])
    foeAccuracy = foeAcc + random.randint(1,6)
    if foePokemon["status"] == "SLP":
        print("")
        print("ZzZzZ...")
        print(input(cont))
    elif foeAccuracy >= 7 and myPokemon["status"] == "OK":
       print(foePokemon["name"],"used",foeAtt,"!")
       if eff == 2:
           print("It's super effective!")
       if eff == 0:
            print("But it didn't work.")
       if eff == 0.5:
            print("It's not very effective.")
       print("")
       print(input("Press ENTER to continue..."))
       myPokemon.update({"HP" : myPokemon["HP"] - int(foePwr*eff)})
       if eff != 0:
        myPokemon.update({"status" : foeSta})
    elif foeAccuracy >= 7:
        print(foePokemon["name"],"used",foeAtt,"!")
        if eff == 2:
           print("Its super effective!")
        if eff == 0:
            print("But it didn't work.")
        if eff == 0.5:
            print("It's not very effective.")   
        print("")
        print(input("Press ENTER to continue..."))
        myPokemon.update({"HP" : myPokemon["HP"] - int(foePwr*eff)})
    else:
        print(foePokemon["name"],"used",foeAtt,"! But...")
        print(foePokemon["name"],"attack missed!")
        print("")
        print(input("Press ENTER to continue..."))
   if foeAttackNum == 3:
    # print(foePokemon["name"],"used",str(foePokemon["attacks"]["third"]).replace("'","").replace("{","").replace("}","").split()[2].replace(",","!"))
    foeAtt = str(foePokemon["attacks"]["third"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[5]
    foeAcc = int(str(foePokemon["attacks"]["third"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[10])
    foePwr = int(str(foePokemon["attacks"]["third"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[8])
    foeTyp = str(foePokemon["attacks"]["third"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[17]
    foeSta = str(foePokemon["attacks"]["third"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[13]
    effic(myPokemon["type"],foePokemon["attacks"]["third"][foeAtt.lower()]["type"])
    foeAccuracy = foeAcc + random.randint(1,6)
    if foePokemon["status"] == "SLP":
        print("")
        print("ZzZzZ...")
        print(input(cont))
    elif foeAccuracy >= 7 and myPokemon["status"] == "OK":
       print(foePokemon["name"],"used",foeAtt,"!")
       if eff == 2:
           print("It's super effective!")
       if eff == 0:
            print("But it didn't work.")
       if eff == 0.5:
            print("It's not very effective.")
       print("")
       print(input("Press ENTER to continue..."))
       myPokemon.update({"HP" : myPokemon["HP"] - int(foePwr*eff)})
       if eff != 0:
        myPokemon.update({"status" : foeSta})
    elif foeAccuracy >= 7:
        print(foePokemon["name"],"used",foeAtt,"!")
        if eff == 2:
           print("Its super effective!")
        if eff == 0:
            print("But it didn't work.")
        if eff == 0.5:
            print("It's not very effective.")   
        print("")
        print(input("Press ENTER to continue..."))
        myPokemon.update({"HP" : myPokemon["HP"] - int(foePwr*eff)})
    else:
        print(foePokemon["name"],"used",foeAtt,"! But...")
        print(foePokemon["name"],"attack missed!")
        print("")
        print(input("Press ENTER to continue..."))
   if foeAttackNum == 4:
    # print(foePokemon["name"],"used",str(foePokemon["attacks"]["fourth"]).replace("'","").replace("{","").replace("}","").split()[2].replace(",","!"))
    foeAtt = str(foePokemon["attacks"]["fourth"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[5]
    foeAcc = int(str(foePokemon["attacks"]["fourth"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[10])
    foePwr = int(str(foePokemon["attacks"]["fourth"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[8])
    foeTyp = str(foePokemon["attacks"]["fourth"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[17]
    foeSta = str(foePokemon["attacks"]["fourth"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[13]
    effic(myPokemon["type"],foePokemon["attacks"]["fourth"][foeAtt.lower()]["type"])
    foeAccuracy = foeAcc + random.randint(1,6)
    if foePokemon["status"] == "SLP":
        print("")
        print("ZzZzZ...")
        print(input(cont))
    elif foeAccuracy >= 7 and myPokemon["status"] == "OK":
       print(foePokemon["name"],"used",foeAtt,"!")
       if eff == 2:
           print("It's super effective!")
       if eff == 0:
            print("But it didn't work.")
       if eff == 0.5:
            print("It's not very effective.")
       print("")
       print(input("Press ENTER to continue..."))
       myPokemon.update({"HP" : myPokemon["HP"] - int(foePwr*eff)})
       if eff != 0:
        myPokemon.update({"status" : foeSta})
    elif foeAccuracy >= 7:
        print(foePokemon["name"],"used",foeAtt,"!")
        if eff == 2:
           print("Its super effective!")
        if eff == 0:
            print("But it didn't work.")
        if eff == 0.5:
            print("It's not very effective.")   
        print("")
        print(input("Press ENTER to continue..."))
        myPokemon.update({"HP" : myPokemon["HP"] - int(foePwr*eff)})
    else:
        print(foePokemon["name"],"used",foeAtt,"! But...")
        print(foePokemon["name"],"attack missed!")
        print("")
        print(input("Press ENTER to continue..."))
   eff = 1
   main_screen()
  


def endgame():
   if myPokemon["HP"] > foePokemon["HP"]:
    print("""


    """)
    print("=" * 45)
    print(foePokemon["name"],"fainted.",myPokemon["name"],"wins the battle!")
    print("=" * 45)
    print("""


    """)
   else:
      print("""


    """)
      print("=" * 45)
      print(myPokemon["name"],"fainted.",foePokemon["name"],"wins the battle!")
      print("=" * 45)
      print("""


    """)
   

eff = 1
   
def effic(a,b): #a = pokemon type, b = attack type
   global eff
   if a == "fire" and (b == "water" or b == "ground"):
      eff = 2
   if a == "water" and (b == "grass" or b == "electric"):
      eff = 2
   if a == "grass" and (b == "fire" or b == "flying"):
      eff = 2
   if a == "electric" and (b == "ground" or b == "rock"):
      eff = 2
   if a == "flying" and (b == "electric" or b == "rock"):
      eff = 2
   if a == "ground" and (b == "water" or b == "ground"):
      eff = 2
   if a =="grass" and (b == "water" or b == "grass"):
      eff = 0.5
   if a =="fire" and (b == "grass" or b == "fire"):
      eff = 0.5
   if a =="water" and (b == "water" or b == "fire"):
      eff = 0.5
   if a =="electric" and (b == "electric"):
      eff = 0.5
   if a =="flying" and (b == "grass"):
      eff = 0.5
   if a =="ground" and (b == "normal"):
      eff = 0.5
   if a =="ground" and (b == "electric"):
      eff = 0
   if a == "flying" and (b == "ground"):
      eff = 0 
   return eff

def main_screen():
    global eff
    eff = 1
    os.system('cls')
    if myPokemon["status"] == "SLP":
       sleep = random.randint(1,3)
       if sleep <= 2:
          print(myPokemon["name"],"sleeps!")
       else:
          print(myPokemon["name"],"woke up!") 
          myPokemon.update({"status" : "OK"})    
       print("")
       print(input(cont))
       os.system('cls')
    if myPokemon["status"] == "PSN":
       print(myPokemon["name"],"is hurt by poison!")
       print("")
       print(input(cont))
       myPokemon.update({"HP" : myPokemon["HP"] -2})
       os.system('cls')
    if foePokemon["status"] == "PSN":
       print(foePokemon["name"],"is hurt by poison!")
       print("")
       print(input(cont))
       foePokemon.update({"HP" : foePokemon["HP"] - 2})
       os.system('cls')
    if foePokemon["HP"] <= 0 or myPokemon["HP"] <= 0:
       endgame()
       exit()    
    # print(len(myPokemon["attacks"].keys()))
    print("=" * 35)
    print(myPokemon["name"] + "  HP: " + str(myPokemon["HP"]) + "   status: " + myPokemon["status"])
    print(foePokemon["name"]+ "  HP: " + str(foePokemon["HP"]) + "   status: " + foePokemon["status"])
    print("=" * 35)
    myPokemon_attack()

def myPokemon_attack():
    global onTurn
    print("What do you want",myPokemon["name"],"to do? ")
    print("")
    attacks_count = len(myPokemon["attacks"].keys())
    if attacks_count == 4:
        print(str((myPokemon["attacks"]["first"])).replace("'","").replace(":",",").replace("{","").replace("}","").split(",")[0].upper())
        print(str((myPokemon["attacks"]["second"])).replace("'","").replace(":",",").replace("{","").replace("}","").split(",")[0].upper())
        print(str((myPokemon["attacks"]["third"])).replace("'","").replace(":",",").replace("{","").replace("}","").split(",")[0].upper())
        print(str((myPokemon["attacks"]["fourth"])).replace("'","").replace(":",",").replace("{","").replace("}","").split(",")[0].upper())
    elif attacks_count == 3:
        print(str((myPokemon["attacks"]["first"])).replace("'","").replace(":",",").replace("{","").replace("}","").split(",")[0].upper())
        print(str((myPokemon["attacks"]["second"])).replace("'","").replace(":",",").replace("{","").replace("}","").split(",")[0].upper())
        print(str((myPokemon["attacks"]["third"])).replace("'","").replace(":",",").replace("{","").replace("}","").split(",")[0].upper())
    elif attacks_count == 2:
        print(str((myPokemon["attacks"]["first"])).replace("'","").replace(":",",").replace("{","").replace("}","").split(",")[0].upper())
        print(str((myPokemon["attacks"]["second"])).replace("'","").replace(":",",").replace("{","").replace("}","").split(",")[0].upper())
    else:
        print(str((myPokemon["attacks"]["first"])).replace("'","").replace(":",",").replace("{","").replace("}","").split(",")[0].upper())
    print("")
    attackon(myPokemon["attacks"],input("Choose an attack! "))

def attackon(a,b):
    os.system('cls')
    global eff
    if b in a["first"]:
     effic(foePokemon["type"],a["first"][b]["type"])
     accuracy = a["first"][b]["acc"] + random.randint(1,6)
     if myPokemon["status"] == "SLP":
        print("")
        print("ZzZzZ...")
        print(input(cont))
     elif accuracy >= 7 and foePokemon["status"] == "OK":
        print(myPokemon["name"], "used", a["first"][b]["name"],"!")
        if eff == 2:
           print("It's super effective!")
        if eff == 0:
            print("But it didn't work.")
        if eff == 0.5:
            print("It's not very effective.")
        print("")
        print(input("Press ENTER to continue..."))
        foePokemon.update({"HP" : int((foePokemon["HP"] - (a["first"][b]["power"])*eff))})
        if eff != 0:
            foePokemon.update({"status" : a["first"][b]["stc"]})
     elif accuracy >= 7:
        print(myPokemon["name"], "used", a["first"][b]["name"],"!")
        if eff == 2:
           print("Its super effective!")
        if eff == 0:
            print("But it didn't work.")
        if eff == 0.5:
            print("It's not very effective.")   
        print("")
        print(input("Press ENTER to continue..."))
        foePokemon.update({"HP" : int((foePokemon["HP"] - (a["first"][b]["power"])*eff))})
     else:
        print(myPokemon["name"],"attack missed!")
        print("")
        print(input("Press ENTER to continue..."))
    elif b in a["second"]:
     effic(foePokemon["type"],a["second"][b]["type"])
     accuracy = a["second"][b]["acc"] + random.randint(1,6)
     if myPokemon["status"] == "SLP":
        print("")
        print("ZzZzZ...")
        print(input(cont))
     elif accuracy >= 7 and foePokemon["status"] == "OK":
        print(myPokemon["name"], "used", a["second"][b]["name"],"!")
        if eff == 2:
           print("It's super effective!")
        if eff == 0:
            print("But it didn't work.")
        if eff == 0.5:
            print("It's not very effective.")
        print("")
        print(input("Press ENTER to continue..."))
        foePokemon.update({"HP" : foePokemon["HP"] - int((a["second"][b]["power"])*eff)})
        if eff != 0:
            foePokemon.update({"status" : a["second"][b]["stc"]})
     elif accuracy >= 7:
        print(myPokemon["name"], "used", a["second"][b]["name"],"!")
        if eff == 2:
           print("Its super effective!")
        if eff == 0:
            print("But it didn't work.")
        if eff == 0.5:
            print("It's not very effective.")
        print("")
        print(input("Press ENTER to continue..."))
        foePokemon.update({"HP" : int(foePokemon["HP"] - (a["second"][b]["power"])*eff)})
     else:
        print(myPokemon["name"],"attack missed!")
        print("")
        print(input("Press ENTER to continue..."))
    elif b in a["third"]:
     effic(foePokemon["type"],a["third"][b]["type"])
     accuracy = a["third"][b]["acc"] + random.randint(1,6)
     if myPokemon["status"] == "SLP":
        print("")
        print("ZzZzZ...")
        print(input(cont))
     elif accuracy >= 7 and foePokemon["status"] == "OK":
        print(myPokemon["name"], "used", a["third"][b]["name"],"!")
        if eff == 2:
           print("It's super effective!")
        if eff == 0:
            print("But it didn't work.")
        if eff == 0.5:
            print("It's not very effective.")
        print("")
        print(input("Press ENTER to continue..."))
        foePokemon.update({"HP" : foePokemon["HP"] - int((a["third"][b]["power"])*eff)})
        if eff != 0:
            foePokemon.update({"status" : a["third"][b]["stc"]})
     elif accuracy >= 7:
        print(myPokemon["name"], "used", a["third"][b]["name"],"!")
        if eff == 2:
           print("Its super effective!")
        if eff == 0:
            print("But it didn't work.")
        if eff == 0.5:
            print("It's not very effective.")
        print("")
        print(input("Press ENTER to continue..."))
        foePokemon.update({"HP" : int(foePokemon["HP"] - (a["third"][b]["power"])*eff)})
     else:
        print(myPokemon["name"],"attack missed!")
        print("")
        print(input("Press ENTER to continue..."))
    elif b in a["fourth"]:
     effic(foePokemon["type"],a["fourth"][b]["type"])
     accuracy = a["fourth"][b]["acc"] + random.randint(1,6)
     if myPokemon["status"] == "SLP":
        print("")
        print("ZzZzZ...")
        print(input(cont))
     elif accuracy >= 7 and foePokemon["status"] == "OK":
        print(myPokemon["name"], "used", a["fourth"][b]["name"],"!")
        if eff == 2:
           print("It's super effective!")
        if eff == 0:
            print("But it didn't work.")
        if eff == 0.5:
            print("It's not very effective.")
        print("")
        print(input("Press ENTER to continue..."))
        foePokemon.update({"HP" : int((foePokemon["HP"] - (a["fourth"][b]["power"])*eff))})
        if eff != 0:
            foePokemon.update({"status" : a["fourth"][b]["stc"]})
     elif accuracy >= 7:
        print(myPokemon["name"], "used", a["fourth"][b]["name"],"!")
        if eff == 2:
           print("Its super effective!")
        if eff == 0:
            print("But it didn't work.")
        if eff == 0.5:
            print("It's not very effective.")
        print("")
        print(input("Press ENTER to continue..."))
        foePokemon.update({"HP" : int(foePokemon["HP"] - (a["fourth"][b]["power"])*eff)})
     else:
        print(myPokemon["name"],"attack missed!")
        print("")
        print(input("Press ENTER to continue..."))
    eff = 1   
    foeAttack()     

#print(str(foePokemon["attacks"]["third"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[5])
#print(input("wait"))

def choose():
    global myPokemon
    global foePokemon
    print(str(choice).replace("'","").replace("]","").replace("[",""))
    myPokemon = input("Choose your pokemon from the list above. ").upper()
    if myPokemon == "CHARMANDER":
       myPokemon = Charmander
    elif myPokemon == "SQUIRTLE":
       myPokemon = Squirtle
    elif myPokemon == "BULBASAUR":
       myPokemon = Bulbasaur
    elif myPokemon == "SANDSHREW":
       myPokemon = Sandshrew
    elif myPokemon == "PIDGEY":
       myPokemon = Pidgey
    elif myPokemon == "PIKACHU":
       myPokemon = Pikachu
    else:
       choose()
    os.system('cls')
    print("You have chosen",myPokemon["type"],"pokemon",myPokemon["name"])
    print("")
    print("Now you have to choose pokemon for your rival.")
    print(input(cont))
    os.system('cls')
    rival_list = choice.copy()
    rival_list.remove(myPokemon["name"])
    print(str(rival_list).replace("'","").replace("]","").replace("[",""))
    foePokemon = input("Choose your rival's pokemon from the list above. ").upper()
    if foePokemon == "CHARMANDER":
       foePokemon = Charmander
       print("You have chosen",foePokemon["type"],"pokemon",foePokemon["name"],"for your rival.")
    elif foePokemon == "SQUIRTLE":
       foePokemon = Squirtle
       print("You have chosen",foePokemon["type"],"pokemon",foePokemon["name"],"for your rival.")
    elif foePokemon == "BULBASAUR":
       foePokemon = Bulbasaur
       print("You have chosen",foePokemon["type"],"pokemon",foePokemon["name"],"for your rival.")
    elif foePokemon == "PIDGEY":
       foePokemon = Pidgey
       print("You have chosen",foePokemon["type"],"pokemon",foePokemon["name"],"for your rival.")
    elif foePokemon == "SANDSHREW":
       foePokemon = Sandshrew
       print("You have chosen",foePokemon["type"],"pokemon",foePokemon["name"],"for your rival.")
    elif foePokemon == "PIKACHU":
       foePokemon = Pikachu
       print("You have chosen",foePokemon["type"],"pokemon",foePokemon["name"],"for your rival.")
    else:
       print("Rival then has chosen his pokemon by his own.")
       print(input(cont))
       foePokemon = rival_list[random.randint(0,len(rival_list)-1)]
       if foePokemon == "CHARMANDER":
           foePokemon = Charmander
       elif foePokemon == "SQUIRTLE":
           foePokemon = Squirtle
       elif foePokemon == "BULBASAUR":
           foePokemon = Bulbasaur
       elif foePokemon == "PIDGEY":
           foePokemon = Pidgey
       elif foePokemon == "SANDSHREW":
           foePokemon = Sandshrew
       elif foePokemon == "PIKACHU":
           foePokemon = Pikachu
       print("Rival has chosen",foePokemon["type"],"pokemon",foePokemon["name"],"!") 
    print(input(cont))

os.system('cls')    

choose()

if myPokemon["speed"] >= foePokemon["speed"]:
   main_screen()
else:
   foeAttack()

# print(myPokemon["attacks"]["bubble"])
# main_screen()

