#data hiding
class MobileMoney:
    def __init__(self):
        self.__balance = 500000
    def deposit(self, x):
        self.__balance += x
    def withdraw(self, y):
        if self.__balance>y:
            self.__balance -= y
        else:
            print('Insufficient Balance to withdraw required amount')
    def check_balance(self):
        return self.__balance
x=int(input('Enter the amount to deposit: '))
y=int(input('Enter the amount to withdraw: '))
acc = MobileMoney()
acc.deposit(x)
acc.withdraw(y)
print(f'Your account has UGX.{acc.check_balance():,}')