class Animal:
    def __init__(self, name):
        self.name = name
    def info(self):
        print('Animal name:', self.name)

class Dog(Animal):
    def __init__(self, name, breed):

        super().__init__(name)
        self.breed = breed
    def details(self):
        print(self.name, "is a", self.breed)

z= Dog("Bowie", "Wolf")
z.info()
z.details()
