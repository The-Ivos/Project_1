texttoex = "Nazdar vole, jak se vede? Je to doby, voe? Jasny, nazdar."

text = "nazdar,"

nopuncttext = texttoex.replace(","," ").replace("."," ").replace("!"," ").replace(";"," ").replace(":"," ").replace("?"," ").split()

print(nopuncttext)
print(len(text))

