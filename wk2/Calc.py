num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def add(a, b):
    return a + b
addition = add(num1, num2)

def subtract(a, b):
    return a - b
subtraction = subtract(num1, num2)

def multiply(a, b):
    return a * b
multiplication = multiply(num1, num2)

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
division = divide(num1, num2)

command =[1,2,3,4]
command = int(input("OPERATION?\n1. addition\n2. subtraction\n3. multiplication\n4. division\nReply: "))
if command == 1:
    print("Addition:", addition)
elif command == 2:
    print("Subtraction:", subtraction)
elif command == 3:
    print("Multiplication:", multiplication)
elif command == 4:
    print("Division:", division)
else:
    print("Invalid command.")