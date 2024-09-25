Squirtle = {"water gun": {"power": 7, "acc": 3},
              "bubblebeam": {"power": 5, "acc":4},
              "HP": 25}

Charmander = {"ember": 6,
                 "tackle": 4,
                 "HP": 28}

myPokemon = Squirtle
foePokemon = Charmander

def squirtle_move():
    global squirtleattack
    squirtleattack = input("Which attack do you want Squirtle to use? ")
    if squirtleattack == "1":
        squirtleattack = "water gun"
        attack_water_gun()
    elif squirtleattack == "2":
        squirtleattack = "bubblebeam"
        attack_bubblebeam()

def attack_water_gun():
    global foeCharmander
    print("Squirtle used water gun!")
    foeCharmander.update({"HP": foeCharmander["HP"] - mySquirtle[squirtleattack]["power"]})

def main_screen():

squirtle_move()

print(mySquirtle[squirtleattack]["acc"])
print(foeCharmander["HP"])