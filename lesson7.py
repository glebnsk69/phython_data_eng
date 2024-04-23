class Human:
    name:str
    __age:int

    def __init__(self,name='Vasya'):
        self.name = name
        self.__age = 30
    def __str__(self):
        return str(self.name)+' ('+str(self.__age)+')'

o_vas = Human("Vas")
print(o_vas)