import time
starttime= time.time()
t=time.localtime(starttime)
print(t.tm_hour,t.tm_min,t.tm_sec,sep=':')

def f1(a:int):
    print("1",a*2)

#def f1(a:str):
#    print("2",a*10)

f1(int(10))
f1("aas")
f1()