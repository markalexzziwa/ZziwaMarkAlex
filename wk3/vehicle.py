from abc import ABC, abstractmethod


# Abstract Class (Blueprint)
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass  # No implementation here


# Concrete Class (Fills in the details)
class Car(Vehicle):

    def start_engine(self):
        return "Engine started: Spark plugs ignited, fuel flowing!"


# Usage
# my_vehicle = Vehicle()  # ERROR: Cannot instantiate an abstract class directly

my_car = Car()
print(my_car.start_engine())  # Works perfectly
