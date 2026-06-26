class Animal:
    def __init__(self, name):
        self.name = name
    def info(self):
        print('Animal name:', self.name)

class Dog(Animal):
    def sound(self):
        print('The dog barks')
d=Dog('Bowie')
d.info()
d.sound()
