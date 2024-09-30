slovo = "pes"
print(slovo)

slovo_napul = list(slovo)
print(slovo)
slovicko = list(slovo_napul)
slovinecko = slovicko.insert(1,"\n")
lajna = str(str(slovicko).replace("'","").replace("]","").replace("[",""))
lajna = str(lajna).replace(",","").replace(" ","")
print(type(lajna))
print(lajna)


message = "Hello \n World"
print(type(message))
print(message)