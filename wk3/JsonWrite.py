import json
student = {
    'name': 'Zed',
    'age':'21',
    'course': 'BSSE'
}
with open('student.json', 'w') as file:
    json.dump(student,file,indent=4)