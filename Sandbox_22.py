eff = 1
   
def effic(a,b): #a = pokemon type, b = attack type
   global eff
   if a == "fire" and b == "water" or b == "fire":
      eff = 0.5
   if a == "flying" and b == "nice":
      eff = 0
   if a == "water" and b == "grass":
      eff = 2
   if a =="grass" and b == "water":
      eff = 0.5
   if a =="fire" and b == "grass":
      eff = 0.5
   if a == "flying" and b == "electric":
      eff = 2
   return eff

effic("flying","nice")

print(eff)