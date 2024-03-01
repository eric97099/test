import json
import os

error_word=dict()
# if os.path.exists("erro.json") and os.path.getsize("erro.json") > 0:
#     with open("erro.json", "r", encoding="utf-8") as file:
#         try:
#             error_word = json.load(file)
#         except json.JSONDecodeError:
#             print("無法解析 JSON 檔案")
# else:
#     print("檔案不存在或者是空的，將使用空的字典")
with open ("erro.json","r",encoding="utf-8")as file:
    error_word =json.load(file)
    print(error_word)
with open("English_Word.json","r",encoding="utf-8") as file:
    read = json.load(file)
    print(read)
for eng , chi in read.items():
    print(eng)
    asw = input("請輸入中文 : ")
    if asw != chi:
        print("錯誤答案!!")
        if eng in error_word:
            print("此單字重複錯誤")
        else:
            error_word[eng] =chi
print(error_word)
with open("erro.json","w",encoding="utf-8") as file:
    a = json.dump(error_word,file,ensure_ascii=False,indent=2)

   
