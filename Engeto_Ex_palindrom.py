zadana_slova = ["jaro","jej","kolo","aha"]
slovo = (zadana_slova[1].lower())
compare = slovo[::-1]

if slovo == compare:
    print("Slovo",slovo,"je palindrom!")
else:
    print("Slovo",slovo,"neni palindrom!")