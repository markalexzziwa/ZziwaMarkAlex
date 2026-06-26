class Animal:
    def sound(self):
        print("Animal sound")
        
class Cow(Animal):
    def sound(self):
        print('moo')

c=Cow()
c.sound()