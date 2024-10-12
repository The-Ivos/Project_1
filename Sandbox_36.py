listas = ["Hej!","Coje?","Sme tady.","Jasny.","Tyvole.","Nefunguje."]
slovo = "Kojot"

hony = []
kone = listas.copy()
for i in kone:
    if i.endswith("."):
        listas.remove(i)
        listas.append(i.replace(".",""))
        



print(listas)
print(kone)



