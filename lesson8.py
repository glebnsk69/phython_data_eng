class Human:
    __name:str
    __location:str

    def __init__(self,name='Unknown'):
        self.__name = name
        self.__location="Unknown"

    def get_location(self):
        return self.__name +': '+ self.__location

    def set_location(self,location):
        self.__location=location
    def get_name(self):
        return self.__name
    def getInfo(self):
        return 'name:'+str(self.__name)+' locations:'+str(self.__location)+' '

class Child(Human):
    __age = 16
    _comment = ":"

    def __init__(self,name):
        super().__init__(name)

    def set_age(self,age):
        self.__age = age
    def get_age(self):
        return str(super().get_name())+":"+str(self.__age)
    def getInfo(self):
        return str(super().getInfo())+' age:'+ str(self.__age)
    def test(self):
        print('- '*20)
        print(super().get_name())
        print(self.__age)

class Bus:
    __humans: list()

    def __init__(self,humans:list):
        self.__humans = humans

    def addHuman(self,h:Human):
        self.__humans.append(h)
    def printList(self):
        for i in self.__humans:
            print(i.getInfo())
    def addChildren(self,children:list):
        self.__humans = self.__humans+children

    def removePerson(self,name:str):
        for i in self.__humans:
            if i.get_name()==name:
                self.__humans.remove(i)
                return
    def test(self,name:str):
        pass

h = Human('Vasya')
h1 = Child('Masha')
h1.set_location("Tula")
h1.set_age(113)

humans = [Human('Roman'),Human('Ostap'),Child('Sasha')]
humans.append(Human('SergeyVladimirovich'))
bus = Bus(humans)

bus.addHuman(h)
bus.addHuman(h1)
bus.addChildren([Child('mira'),Child('dina'),Child('seva')])
#bus.test()
bus.removePerson('mira')
bus.removePerson('seva')
bus.removePerson('dina')
bus.printList()

# Обработка ошибок

a = [1,2,3,4]
b = ['q','w',"e",92,18,2]
c = a+b


def ld(l:list):
    n=0
    for i in l:
        n+=1
        try:
            print(n,i/2,sep=') ')
        except Exception as e:
            print('Exception',end=': ')

            print(e)
#        finally:
#            print('='*10)

ld(c)