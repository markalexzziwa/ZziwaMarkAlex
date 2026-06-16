marks = int(input("Enter your marks: "))

#assign grades to marks
if marks >= 90:
    Grade = "A+"
elif marks >= 80:
    Grade = "A"
elif marks >= 70:
    Grade = "B"
elif marks >= 60:
    Grade = "C"
elif marks >= 50:
    Grade = "D"
else:
    Grade = "F"

#grade comments
if Grade == "A+":
    Comment = "Excellent work!"
elif Grade == "A":
    Comment = "Great job!"
elif Grade == "B":
    Comment = "Good effort!"
elif Grade == "C":
    Comment = "Fair performance!"
elif Grade == "D":
    Comment = "Needs improvement!"
else:
    Comment = "Failed!"
print(f"The student's grade is {Grade} with {marks} marks\n Comment: {Comment}.")