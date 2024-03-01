thisdict = {
'tim':{
    "id": 1,
    "age": "19",
    "school": "a"
  },  
 'jerry':{
    "id" : 2,
    "age":"56",
    "school":"b" 
 } 
}
x = thisdict["tim"]["id"]
# print(x)
x = thisdict.get("id")
# print(x)
x = thisdict.keys()
# print(x)
x = thisdict.values()
# print(x)
x = thisdict.items()
# print(x)
for name,member_dict in thisdict.items():
    print("name : ",name)
    print("age",member_dict["age"])

english_word={
    "name":"名字",
    "apple":"蘋果"
}
for i,list in english_word.items():
    print("英文 :",i)
    print("中文 :",list)
    