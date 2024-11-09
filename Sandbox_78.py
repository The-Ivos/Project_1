import json

with open("file.JSON","r",encoding="utf-8") as file:
    content = json.load(file)


csv_header = ",".join(list(content[0].keys()))+"\n"
csv_cont = ""


for i in range(len(content)):
    
    csv_cont += f"{",".join(map(str,list(content[i].values())))}\n"

open("vystup.csv","w").close()
with open("vystup.csv","a+",encoding="utf-8") as file:

    file.write(csv_header)
    file.write(csv_cont.strip())

    file.seek(0)

    content_csv = file.read()

print(f"""\
      
Vysledne CSV:
      
{content_csv}

""")

    
