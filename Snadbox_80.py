import json

with open("example_1.json","r+",encoding="utf-8") as file:
    content = json.load(file)
    content["prize"] = 68
    print(content)

with open("example_1.json","w",encoding="utf-8") as file:
    json.dump(content,file)

# with open("example_2.json","r",encoding="utf-8") as file:
#     content_2 = json.load(file)



print(content)


# print(content_2)

# print(content_2["quiz"]["maths"]["q2"])

