animals = ["ahoj","lal","ok","ok","he","ju","ok","ok","he","ju","ok","ok","he","ju","subu","uidhiuwqygtrwrqvaqqavcrrcaqyavuq","jo","u","muzebyt","tutu","tuut","rqeq","panejo","tyvado","paradni!","kuuuurva!","YES",8707627521823]

animals2 = ["leg","prase","kun","ruka"]

oddelovac = "-" * 40

newdict = {}
newdict_big = {}

for i in animals:
    if len(str(i)) < 10:
        newdict[len(str(i))] = 0
    else:
        newdict_big[len(str(i))] = 0

dict_to_comp = list(newdict)
dict_to_comp_big = list(newdict_big)

for i in animals:
    for j in dict_to_comp:
        if len(str(i)) == j:
            print("there",i,j)
            newdict[len(str(i))] += 1
        else:
            print("not there",i,j)

for i in animals:
    for j in dict_to_comp_big:
        if len(str(i)) == j:
            print("there",i,j)
            newdict_big[len(str(i))] += 1
        else:
            print("not there",i,j)

print(dict_to_comp)
print(dict_to_comp_big)

stars = list(newdict.items())
print(stars)

stars_big = list(newdict_big.items())
print(stars_big)

abeceda = []
for i,b in stars:
    adda = str((3 - len(str(i))) * " ") + str(i) + "|" + str(b * "*") + str((14 - b)*" ") + "|" + str(b)
    abeceda.append(adda)

abeceda_big = []
for i,b in stars_big:
    adda = str((3 - len(str(i))) * " ") + str(i) + "|" + str(b * "*") + str((14 - b)*" ") + "|" + str(b)
    abeceda_big.append(adda)

sorted_abc = sorted(abeceda)
sorted_abc_big = sorted(abeceda_big)


print(abeceda)
print(sorted_abc)

print(sorted_abc_big)

# print(newdict)

# print(stars)
print(oddelovac)
print("LEN|  OCCURENCES  |NR.")
print(oddelovac)

for i in sorted_abc:
    print(str(i).replace("'","").replace(",","").strip("()"))

for i in sorted_abc_big:
    print(str(i).replace("'","").replace(",","").strip("()"))













#foePokemon.update({"HP" : int(foePokemon["HP"] - (a["first"][str(myPokemon["attacks"]["first"]).split(" ")[0].replace("{'","").replace("'","").replace(":","")]["power"])*(eff + critical))})