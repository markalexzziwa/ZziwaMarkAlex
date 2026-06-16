def login_system():
    print("Welcome to the Login System")

    # Predefined credentials (in real app, use a database)
    users = {
        "Admin": "password123",
        "Technician": "pass456",
        "Farmer": "pass789"
    }

    # Attempt to login
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if user name exists
        if username in users:
            if users[username] == password:
                print("Login successful")
                return True
            else:
                print("Incorrect password")
        else:
            print("Username not found")

        attempts += 1
        print(f"Attempt {attempts} of {max_attempts}")
    print("Maximum login attempts reached. Access denied.")
    return False
login_system()
