import json
from mypac import Human


l_connect = [
    {"user_name":"user",
     "password":"password123"},
    {"user_name":"user1",
     "password":"password321"},
    {"country":["RU",'USA','KG','KZ']}
]


with open("simple.json",'w') as file:
    json.dump(l_connect,fp=file,indent=2)

with open("simple.json",'r') as file:
    jo = json.load(fp=file)

print(jo)
print(type(jo))

