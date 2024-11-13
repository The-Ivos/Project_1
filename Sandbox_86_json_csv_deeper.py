import json
from pprint import pprint

Abra = {"name": "ABRA",
            "type": "psychic",
            "attacks": {
                "first" : {"tackle" : {"name": "TACKLE", "power": 3, "acc": 5, "stc": "OK","type": "normal","CNF":"NO"}}, 
                "second" : {"confusion" : {"name": "CONFUSION", "power": 0, "acc": 4, "stc": "OK","type": "psychic","CNF":"YES"}},
                "third" : {"hypnosis" : {"name": "HYPNOSIS", "power": 0, "acc": 4, "stc": "SLP","type": "psychic","CNF":"NO"}},
                "fourth" : {"psychic" : {"name": "PSYCHIC", "power": 5, "acc": 4, "stc": "OK","type": "psychic","CNF":"NO"}}
                },
            "HP": 25,
            "status": "OK",
            "speed":5,
            "confused": "NO"}

Bulbasaur = {"name": "BULBASAUR",
            "type": "grass",
            "attacks": {
                "first" : {"tackle" : {"name": "TACKLE", "power": 3, "acc": 5, "stc": "OK","type": "normal","CNF":"NO"}}, 
                "second" : {"vine whip" : {"name": "VINE WHIP", "power": 4, "acc": 5, "stc": "OK","type": "grass","CNF":"NO"}},
                "third" : {"poison powder" : {"name": "POISON POWDER", "power": 0, "acc": 4, "stc": "PSN","type": "poison","CNF":"NO"}},
                "fourth" : {"sleep powder" : {"name": "SLEEP POWDER", "power": 0, "acc": 4, "stc": "SLP","type": "grass","CNF":"NO"}}
                },
            "HP": 29,
            "status": "OK",
            "speed":1,
            "confused": "NO"}

Squirtle = {"name": "SQUIRTLE",
            "type": "water",
            "attacks": {
                "first" : {"tackle" : {"name": "TACKLE", "power": 3, "acc": 5, "stc": "OK","type": "normal","CNF":"NO"}}, 
                "second" : {"bubble" : {"name": "BUBBLE", "power": 4, "acc": 5, "stc": "OK","type": "water","CNF":"NO"}},
                "third" : {"water gun" : {"name": "WATER GUN", "power": 5, "acc": 4, "stc": "OK","type": "water","CNF":"NO"}},
                "fourth" : {"skull bash" : {"name": "SKULL BASH", "power": 7, "acc": 3, "stc": "OK","type": "normal","CNF":"NO"}}
                },
            "HP": 25,
            "status": "OK",
            "speed": 2,
            "confused": "NO"}

Pidgey = {"name": "PIDGEY",
            "type": "flying",
            "attacks": {
                "first" : {"gust" : {"name": "GUST", "power": 3, "acc": 5, "stc": "OK","type": "flying","CNF": "NO"}}, 
                "second" : {"wing slap" : {"name": "WING SLAP", "power": 4, "acc": 4, "stc": "OK","type": "flying","CNF":"NO"}},
                "third" : {"sing" : {"name": "SING", "power": 0, "acc": 4, "stc": "SLP","type": "normal", "CNF": "NO"}},
                "fourth" : {"whirlwind" : {"name": "WHIRLWIND", "power": 2, "acc": 3, "stc": "OK","type": "flying","CNF":"YES"}}
                },
            "HP": 21,
            "status": "OK",
            "speed": 5,
            "confused": "NO"}

Pikachu = {"name": "PIKACHU",
            "type": "electric",
            "attacks": {
                "first" : {"tackle" : {"name": "TACKLE", "power": 3, "acc": 5, "stc": "OK","type": "normal","CNF":"NO"}}, 
                "second" : {"thundershock" : {"name": "THUNDERSHOCK", "power": 4, "acc": 5, "stc": "OK","type": "electric","CNF":"NO"}},
                "third" : {"thunder wave" : {"name": "THUNDER WAVE", "power": 0, "acc": 4, "stc": "PAR","type": "electric","CNF":"NO"}},
                "fourth" : {"toxic" : {"name": "TOXIC", "power": 1, "acc": 4, "stc": "PSN","type": "poison","CNF":"NO"}}
                },
            "HP": 24,
            "status": "OK",
            "speed": 3,
            "confused": "NO"}

Charmander = {"name": "CHARMANDER",
            "type": "fire",
            "attacks": {
                "first" : {"scratch" : {"name": "SCRATCH", "power": 3, "acc": 5, "stc": "OK","type": "normal","CNF":"NO"}}, 
                "second" : {"ember" : {"name": "EMBER", "power": 3, "acc": 5, "stc": "BRN","type": "fire","CNF":"NO"}},
                "third" : {"bite" : {"name": "BITE", "power": 4, "acc": 4, "stc": "OK","type": "dark","CNF":"NO"}},
                "fourth" : {"flame wheel" : {"name": "FLAME WHEEL", "power": 5, "acc": 3, "stc": "BRN","type": "fire","CNF":"NO"}}
                },
            "HP": 28,
            "status": "OK",
            "speed": 4,
            "confused": "NO"}

Sandshrew = {"name": "SANDSHREW",
            "type": "ground",
            "attacks": {
                "first" : {"scratch" : {"name": "SCRATCH", "power": 3, "acc": 5, "stc": "OK","type": "normal","CNF":"NO"}}, 
                "second" : {"rock throw" : {"name": "ROCK THROW", "power": 3, "acc": 5, "stc": "OK","type": "rock","CNF":"NO"}},
                "third" : {"mud-slap" : {"name": "MUD-SLAP", "power": 3, "acc": 5, "stc": "OK","type": "ground","CNF":"NO"}},
                "fourth" : {"earthquake" : {"name": "EARTHQUAKE", "power": 6, "acc": 4, "stc": "OK","type": "ground","CNF":"NO"}}
                },
            "HP": 26,
            "status": "OK",
            "speed": 4,
            "confused": "NO"}

pokemons = [Abra,Bulbasaur,Squirtle,Pidgey,Pikachu,Charmander,Sandshrew]

# pokemons_for_json = f"{pprint(Sandshrew)}"

# print(pokemons_for_json)

open("pokejson.json","w",encoding="utf-8").close()
with open("pokejson.json","r+",encoding="utf-8") as file:
    file.write("{")
    for i in pokemons:

        if i == pokemons[0]:
            
            file.write(f'"{i["name"]}":')
            json.dump(i,file,indent=4)
            file.write("\n")

        else:

            file.write(f',"{i["name"]}":')
            json.dump(i,file,indent=4)
            file.write("\n")

    file.write("}")

with open("pokejson.json","r+",encoding="utf-8") as file:

    content_json = json.load(file)


# for key, value in content_json.items():
#     print(f"{value}")

# for i in content_json.values():
#     print(i)

header = ""
for key, value in content_json[list(content_json.keys())[0]].items():
    header += key+","

header = header.strip(",")

cont = ""

for key, value in content_json.items():
    for i in value.values():

        if type(i) == dict:
            i = list(i["fourth"])[0]
        
        cont += f"{str(i)},"
    cont = cont.strip(",")
    cont +="\n"

cont = cont.strip()


print(cont)

open("pokecsv.csv","w",encoding="utf-8").close()
with open("pokecsv.csv","w",encoding="utf-8") as file:

    file.write(header+"\n")
    file.write(cont)



