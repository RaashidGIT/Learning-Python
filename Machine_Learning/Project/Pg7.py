student = {
    "100": "Gokul",
    "101": "Sourav",
    "102": "Sainadh",
    "103": "Aravind"
}

name = input("Enter the name: ")

found = False
for student_id, student_name in student.items():
    if student_name.lower() == name.lower():
        print("Student ID:", student_id)
        found = True
        break

if not found:
    print("Name not found in the student list.")
