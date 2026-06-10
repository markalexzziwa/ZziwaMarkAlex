username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin":
    if password == "admin123":
        print("Access granted. Welcome, admin!")
    else:
        print("Access denied. Incorrect password.")
else:    print("Access denied. Unknown username.")