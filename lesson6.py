import os


class Human:

    hands:int
    foots:int
    head:int
    eyes:int
    age:int
    sex:int
    name:str

    def __init__(self,name):
        self.hands=2
        self.foots=2
        self.head=1
        self.eyes=2
        self.age=30
        self.sex=1
        self.name = name
    def __str__(self):
        return str(self.name)+' '+str(self.age)+ ' years old'
    def mobilaze(self):
        if self.sex == 1:
            self.hands = int(self.hands/2)
            self.foots = int(self.foots/2)
            self.eyes = int(self.eyes/2)

    def see_info(self):
        print(self.name,self.foots,self.eyes,self.sex,self.hands)
        print(f'age={str(self.age)}')
a= Human("Vasya")
a.see_info()
a.mobilaze()
a.see_info()
a.mobilaze()
a.see_info()
print(a)