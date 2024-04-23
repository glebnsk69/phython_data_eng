a = 4
if a==1:
    print("one")
elif a==2:
    print("two")
elif a==3:
    print("three")
else:
    print("other")

print("-"*80)
print("циклы")
print("-"*80)
#проход по листу
l1= list()
l1.append(0)
l1.append(2)
l1.append("three")

for i in l1:
    print(i)

#по словарю
print("-"*80)
d1 = {
    1:1,
    2:2,
    'c':'three'
}

for i in d1:
    print(i)
print("-*"*80)
i=0
import time
while i<100:
    print("hello",i)
    print(time.localtime(time.time()))
    i+=10
    time.sleep(2)