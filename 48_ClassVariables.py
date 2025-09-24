# -------------------------------
# CLASS VARIABLES in Python
# -------------------------------
# Class variables are:
#   - Shared among ALL instances of a class
#   - Defined outside the constructor (__init__)
#   - Useful for storing information common to all objects

class Student:
    # Class variables (shared by all students)
    class_year = 2025
    num_students = 0

    # Constructor: runs every time a new Student is created
    def __init__(self, name, age):
        self.name = name   # instance variable (unique to each student)
        self.age = age     # instance variable (unique to each student)

        # Update class variable: count how many students exist
        Student.num_students += 1


# -------------------------------
# Create student objects (instances)
# -------------------------------
student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

# -------------------------------
# Accessing class variables
# -------------------------------
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print("------------------")

# -------------------------------
# Accessing instance variables
# -------------------------------
print("List of students:")
print(student1.name)  # Spongebob
print(student2.name)  # Patrick
print(student3.name)  # Squidward
print(student4.name)  # Sandy
