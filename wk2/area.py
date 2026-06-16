length = 10 #global variable
width = 5 #global variable
#calculate area
area = length * width
print("The area of the rectangle is for global variables:", area)

#local variable
def calculate_area2():
    length =10 #local variable
    width = 4 #local variable
    area = length * width
    print("The area of the rectangle is for local variables:", area)
calculate_area2()

#global variable
#accesible to the entire program it uses l=10 and w=5
def calculate_area():
    area = length * width
    print("The area of the rectangle is for global variables:", area)
calculate_area()

