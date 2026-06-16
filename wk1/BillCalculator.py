# Zziwa Mark Alex
# 24/U/11978/EVE
# 2400711978
print("BILL CALCULATOR")
# validating user input for bill amount, number of people, and tip percentage
bill_amount = float(input("Enter the bill amount: "))
number_of_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage: "))
tip_amount = bill_amount * (tip_percentage / 100)
total_bill = bill_amount + tip_amount
amount_per_person = total_bill / number_of_people
print("             ------------            ")
print("             Bill Summary            ")
print("             ------------            ")
print(f"Tip amount:\n Bill Amount x Tip Percentage = UGX. {tip_amount:.2f}""/=")
print(f"Total bill: \n Bill Amount + Tip Amount = UGX. {total_bill:.2f}""/=")
print(f"Amount per person: \n Total Bill / Number of People = UGX. {amount_per_person:.2f}""/=")
