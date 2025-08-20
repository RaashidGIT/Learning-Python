student_db = {}

def add_student(roll_no, name):
    if roll_no in student_db:
        print("Roll number already exists. Try updating instead.")
    else:
        student_db[roll_no] = name
        print(f"Student {name} added successfully.")

def display_students():
    if not student_db:
        print("No student records found.")
    else:
        print("\n--- Student Records ---")
        for roll_no, name in student_db.items():
            print(f"Roll No: {roll_no}, Name: {name}")

def search_student(roll_no):
    if roll_no in student_db:
        print(f"Student found: Roll No: {roll_no}, Name: {student_db[roll_no]}")
    else:
        print("Student not found.")

def update_student(roll_no, new_name):
    if roll_no in student_db:
        old_name = student_db[roll_no]
        student_db[roll_no] = new_name
        print(f"Student name updated from {old_name} to {new_name}.")
    else:
        print("Roll number not found. Cannot update.")

def delete_student(roll_no):
    if roll_no in student_db:
        deleted_name = student_db.pop(roll_no)
        print(f"Deleted student: Roll No: {roll_no}, Name: {deleted_name}")
    else:
        print("Roll number not found. Cannot delete.")

def show_total_students():
    total = len(student_db)
    print(f"\nTotal number of students in the database: {total}")

while True:
    print("Student Database Menu")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Roll No")
    print("4. Update Student Name")
    print("5. Delete Student")
    print("6. Show Total Students")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        add_student(int(roll_no), name)
    elif choice == '2':
        display_students()
    elif choice == '3':
        roll_no = input("Enter Roll No to Search: ")
        search_student(roll_no)
    elif choice == '4':
        roll_no = input("Enter Roll No to Update: ")
        new_name = input("Enter New Name: ")
        update_student(roll_no, new_name)
    elif choice == '5':
        roll_no = input("Enter Roll No to Delete: ")
        delete_student(roll_no)
    elif choice == '6':
        show_total_students()
    elif choice == '7':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1-6.")
