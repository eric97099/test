import json
import os

english_word=dict()
if os.path.exists("English_Word.json"):
    with open ("English_Word.json","r",encoding='utf-8') as file:
        english_word=json.load(file)
        print(english_word)
else :
    with open("English_Word.json","w")as file:
        json.dump(english_word,file,indent=2)


while True:
    key=input("英文 :")
    if key =="exit".lower():
        break
    if key in english_word:
        print(key,"已存在於單字本中")
    else:
        value=input("中文 :") 
        english_word[key] = value
        print("如果要停止輸入,請輸入exit")
print(english_word)

with open("English_Word.json","w", encoding='utf-8') as file1:
    json.dump(english_word,file1,ensure_ascii=False,indent=2)
    
