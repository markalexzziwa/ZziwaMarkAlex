#data hiding
class MobileMoney:
    def __init__(self):
        self.__balance = 500000
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def check_balance(self):
        return self.__balance
acc = MobileMoney()
acc.deposit(200000)
acc.withdraw(50000)
print(f'Your account has UGX.{acc.check_balance():,}')