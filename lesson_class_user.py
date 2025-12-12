class User:
    def __init__(self, name):
        print("Я создан")
        self.username = name
        self.age = 22

    def sayName(self):
        print("Меня зовут", self.username)

    def sayAge(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge

    def addCard(self,card):
        self.card = card
    
    def getCard(self):
        return self.card
