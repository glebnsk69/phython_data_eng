#yaml

import yaml
from mypac import Human

l_connect = [
    {"user_name":"user",
    "password":"password123"},
    {"user_name":"user1",
    "password":"password321"}
]

hl = { 1:Human('Vasya'),
       2:Human('Doma'),
       3:Human('Roma')}
l_connect.append(hl)
print(l_connect)

flag = True
rezList = list()
if flag:
    with open(r'store_file.yaml','w') as file:
        yaml.dump(l_connect,file)

else:
    with open(r'store_file.yaml','r') as file:
        rezList = yaml.load(file,Loader=yaml.FullLoader)
        print (rezList)

