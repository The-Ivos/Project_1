text = "Nazdar kunde!"

with open("zz_novej_file2.txt","x+") as file:
    
    file.write(text)

    file.seek(0)

    content = file.read()


print(content)