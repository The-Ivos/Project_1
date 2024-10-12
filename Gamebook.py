kinds = { 
"warrior" : {"name" : "Lopez",
           "HP": 35,
           "Defence": 6,
           "Attack": 10,
           },

"mage" : {"name" : "Sabrina",
           "HP": 80,
           "Defence": 1,
           "Attack": 3,
           },
}


listkeys = list(kinds.keys())
textkeys = str(listkeys).replace("['","").replace("', '"," ").replace("']","")

kind = input(textkeys + """
             
             
             Choose your kind: """)

#input(kind["name"] := "What is your name: ")

print(kinds[kind])


