class Car:
    def __init__(self, brand, model, price):
        self.brand = brand  
        self._model = model 
        self.__price = price
        print(f"Brand: {self.brand}")
        print(f"Model: {self._model}")
        print(f"Price: {self.__price:,} UGX")
car_1 = Car("BMW", "355i", 63000000)
