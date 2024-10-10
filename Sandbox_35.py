animals = ["ahoj","lala","subu","jo","muzebyt"]

animals2 = ["leg","prase","kun","ruka"]

newdict = {}

for i in animals:
    newdict[len(i)] = 0

dict_to_comp = list(newdict)

for i in animals:
    for j in dict_to_comp:
        if len(i) == j:
            print("there",i,j)
            newdict[len(i)] += 1
        else:
            print("not there",i,j)

print(dict_to_comp)

stars = list(newdict.items())
print(stars)

for i,b in stars:
    print(i,b * "*")



print(newdict)












#foePokemon.update({"HP" : int(foePokemon["HP"] - (a["first"][str(myPokemon["attacks"]["first"]).split(" ")[0].replace("{'","").replace("'","").replace(":","")]["power"])*(eff + critical))})