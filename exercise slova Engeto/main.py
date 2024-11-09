import os

def zobraz_slova(textovy_soubor):
    with open(textovy_soubor,"r+",encoding="UTF-8") as file:
        content = file.readlines()
        newcont = ""
        for i in content:
            if len(i) > 6:
                newcont += i.replace("\n"," ")
        return newcont

# print(os.listdir())

# print(os.getcwd())

if __name__ == "__main__":
    print(zobraz_slova("slova.txt"))


