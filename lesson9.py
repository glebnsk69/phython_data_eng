#Урок 9: import, pip install
import datetime
import pandas
from mypac import Human
from mypac.utils import Man as m

d = datetime.datetime.now()
print(d)
print(type(d))

p = Human('Misha')
p.sayHello()
print('-'*80)
lp = [p,Human('Vasya'),Human('Petya'),Human('Dima')]
for i in lp:
    i.sayHello()

lp.append(Human('Nina'))
print('-'*80)
for i in lp:
    i.sayHello()

Leo = m(25.5)
Leo.sey()