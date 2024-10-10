text = "8, 5, 5, 12, 2, 9, 4, 11, 6, 3, 1, 1, 7, 4, 9, 1, 3, 6, 10, 1, 11, 1"

newlisttotext = text.replace(" ","")
print(newlisttotext)

tuplovanejlist = newlisttotext.split(",")

print(max(tuplovanejlist))