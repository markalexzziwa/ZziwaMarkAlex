import csv
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

headers = ["regno.", "name", "gender", "age", "course", "score"]

new_student = {
    "regno.": "24/U/11978/EVE",
    "name": "Zziwa Mark Alex",
    "gender": "Male",
    "age": 21,
    "course": "Software Engineering",
    "score": 87,
}

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)

    writer.writerow(new_student)

print("successfully added") 
