import json

def json_csv(jsonfile,csvfile):
    with open(jsonfile,"r+",encoding="utf-8") as file:
        content_json = json.load(file)
        # print(content_json)
        
        header = "player,"+",".join(map(str,list(content_json[list(content_json)[0]].keys())))
        cont = ""
        
        for i in content_json.keys():
            cont += i + "," + ",".join(map(str,list(content_json[i].values()))) + "\n"

    open(csvfile,"w",encoding="utf-8").close()
    with open(csvfile,"w",encoding="utf-8") as file:
        file.write(f"{header}\n")
        file.write(f"{cont.strip()}")

def json_csv_simple(jsonfile,csvfile):
    with open(jsonfile,"r+",encoding="utf-8") as file:
        content_json = json.load(file)

        header = "user,password\n"
        cont = ""
        
        for i,j in content_json.items():
            cont += f"{i},{j}\n"

    open(csvfile,"w",encoding="utf-8").close()
    with open(csvfile,"w",encoding="utf-8") as file:
        file.write(header)
        file.write(cont.strip())


json_csv_simple("users.json","users_out.csv")

