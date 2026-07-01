import json
try:
    # Attempt to open and read the JSON file
    with open("student.json", "r") as file:
        data = json.load(file)
        print("File read successfully!")
        print(data)

except FileNotFoundError:
    print("Error: The file 'students.json' does not exist in this directory.")

except json.JSONDecodeError as e:
    print(f"Error: 'students.json' contains invalid JSON syntax.")
    print(f"Details: {e}")

except PermissionError:
    print("Error: You do not have permission to read this file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")