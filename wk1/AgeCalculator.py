firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
city = input("What city do you live in? ")
birthyear = int(input("What is your birth year? "))
currentyear = 2026
age = currentyear - birthyear
print(f"Hi {firstname} {lastname} from {city}, \n you are {age} years old.")