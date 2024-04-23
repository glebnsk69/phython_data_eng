import sys

print(sys.version_info)
#два способа создания листа
v_list = list()
v2_list = [1,2,3]
v_list.append("222")
v_list.append(55)

print(v_list)
print(v_list[1])
v_row = list()
for i in range(10):
    v_row.append(list())
    for j in range(5):
        v_row[i].append(i*10+j)
print('-'*80)
print(v_row)
print(v_row[3])
print(v_row[3][3])

#словарь
#два способа объявления словаря

d1 = dict()
d2 = {
    "val1":1,
    "val2":2,
    "val3":"val3"
}

d1["first"]=1
d1["second"]=2
d1[0]="""
string1
string2
string3
"""
print("d1",d1)
d1["second"] = "second"
d1.get('first')
print(d1.keys())
print(d2.keys())
print(d1)
print(d2)
print(d1.get('first'))
#Объединение словарей
d3 = {**d1,**d2}
print('-'*80)

for i in d3.keys():
    print(i,d3.get(i),sep=':')
print('-'*80)
a = (1,2,3,'d')
print(a)
print('='*80)
a = [1,2,3,4]
b = ['q','w',"e"]
c = a+b
print(a)
print(b)
print(c)
