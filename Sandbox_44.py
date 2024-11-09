def je_anagram(*args):
    anagram = 0
    for i in range(1,len(args)):
        for j in args[i]:
            if j not in args[0]:
                anagram = +1
    if anagram > 0:
        anagram = False
    else:
        anagram = True
    return anagram
    
print(
    je_anagram("ship", "hips", "phis"),
    je_anagram("ship", "hips", "duck"),
    sep="\n"
)