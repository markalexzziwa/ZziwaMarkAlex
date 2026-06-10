total = 0
count = 0
while count < 5:
    number = int(input("Enter a number: "))
    total += number
    count += 1

average = total / 5 if count > 0 else 0
print(f"The average is: {average}")