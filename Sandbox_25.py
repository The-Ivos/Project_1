Bulbasaur = {"name": "BULBASAUR",
            "type": "grass",
            "attacks": {
                "first" : {"tackle" : {"name": "TACKLE", "power": 3, "acc": 5, "stc": "OK","type": "normal", "CNF": "NO"}}, 
                "second" : {"vine whip" : {"name": "VINE WHIP", "power": 4, "acc": 5, "stc": "OK","type": "grass"}},
                "third" : {"poison powder" : {"name": "POISON POWDER", "power": 0, "acc": 4, "stc": "PSN","type": "poison"}},
                "fourth" : {"sleep powder" : {"name": "SLEEP POWDER", "power": 0, "acc": 4, "stc": "SLP","type": "grass"}}
                },
            "HP": 29,
            "status": "BRN",
            "speed":1,
            "confused": "NO"}

foePokemon = Bulbasaur

foeCnf = str(foePokemon["attacks"]["first"]).replace(":","").replace(",","").replace("{","").replace("}","").split("'")[21]

print(foeCnf)