def je_anagram(*args):

    vzor = sorted(args[0])

    for i in args:
        if sorted(i) != vzor:
            return False
        else: 
            return True
        
print(
    je_anagram("ship", "hips", "block"),
    je_anagram("ship", "hips", "duck"),
    sep="\n"
)