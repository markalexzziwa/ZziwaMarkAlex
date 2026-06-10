car_input = input("Enter a German car brand (lowercase only): ")
car=["bmw", "mercedes", "audi"]
if car_input not in car:
    print("You did not enter a German car brand.")
else:
    print("You entered a German car brand.")