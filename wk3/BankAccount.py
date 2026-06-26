#data hiding
class Bankaccount:
    def __init__(self):
        self.__balance=2800000
    def deposit(self, amount):
        self.__balance += amount
    def show_balance(self):
        return self.__balance
acc= Bankaccount()
acc.deposit(580000)
acc.deposit(620000)
print(acc.show_balance())