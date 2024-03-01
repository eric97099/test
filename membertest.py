# member_dict={}
# def member(name,age):
#     id_number=0
    
#     if id_number==0:
#         id_number=1
#         member_dict[name]={
#                 "age":age,
#                 "id":id_number
#             }
        
#         print(member_dict)
#     elif id_number!=0:
#         id_number+=1
#         member_dict[name]={
            
#                 "age":age,
#                 "id":id_number
#             }
#         print(member_dict)
    

# member("aaa",18)

import json
class member:
    
    def __init__(self):
        try:
            with open("member.json","r") as file:
                self.member_list = json.load(file)
                self.add_id = max([info['id'] for info in self.member_list.values()]) + 1
                
        except (FileNotFoundError, ValueError):
            self.member_list = {}
            self.add_id = 1

    def addmember_id(self):
        name = input(str("name:"))
        age = input("age:")
        self.member_list[name]={
            "id":self.add_id,
            "age":age
        }
        self.add_id+=1
    def get_member(self):
        return self.member_list  

 
MemberList = member()     
MemberList.addmember_id()
MemberToJson = MemberList.get_member()
with open("member.json","w") as file:
    json.dump(MemberToJson,file)







        






