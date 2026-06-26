'''
#public
class Employee:
    def __init__(self):
        self.name="Peter"
emp = Employee()
print(emp)        


#protected
class Employee:
    def __init__(self):
        self._salary=600000
emp = Employee()
print(emp._salary)   
'''
#private
class Employee:
    def __init__(self):
        self.__allowance=600000
emp = Employee()
print(emp.__allowance) 