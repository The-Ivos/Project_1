velikost = 10
sachovnice = []
symboly = ['#',' ']

for i in range(velikost):
    rada = []
    for j in range(velikost):
        index = (i+j)%2
        rada.append(symboly[index])
    sachovnice.append("".join(rada))

print("\n".join(sachovnice))