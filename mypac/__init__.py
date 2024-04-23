class Human:
    age: int
    name: str
    def __init__(self,name="Igor"):
        self.name = name
        self.age = 29

    def sayHello(self):
        print('Hello '+ str(self.name))
