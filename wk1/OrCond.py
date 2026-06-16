age = int(input("Enter your age: "))
marital_status = input("Enter your marital status (single/married): ").lower()
if age >=18 or marital_status == "married":
    print("You have an aspect of an adult.")
else:
    print("You are not a complete adult.")