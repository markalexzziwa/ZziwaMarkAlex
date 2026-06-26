#inheritance
class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print('Name: ', self.name)
        
class Student(Person):
    def study(self):
        print('I an studying python')
student = Student('Alex')
student.display()
student.study()
