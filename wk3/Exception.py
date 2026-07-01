try:
    number=int(input('Enter number: '))
    result = 100/number
    print(result)
except ZeroDivisionError:
    print('Cannot divide by zero')
except ValueError:
    print('Inavlid number entered')
    