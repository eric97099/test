import json
with open("member.json","r") as file:
    read =json.load(file)
    print(read)

a = {
    "yue":{
    "id":1,
    "age":"12"
    },
    "tem":{
        "id":2,
        "age":"13"
    }
}
print(a.items())
with open("test1.json","w") as file1:    
    write = json.dump(a,file1)

# with open("test.json","r") as file2:
#     b = json.load(file2)
#     print(b)
#     print(type(b))
#     print(b.items())
#     for i,ship in b.items():
#         print(i)
#         print(ship["id"])
    



