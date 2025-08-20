# Tuple Practice Problems - 1

subjects = {"Math", "Science", "English", "History", "Computer"}

subjects.add("Art")

subjects.discard("History")

print("Subjects chosen by students:")
for subject in subjects:
    print("-", subject)

print("\nTotal number of unique subjects:", len(subjects))

# Tuple Practice Problems - 2

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print("First 3 days:", days[:3])

print("Weekend days:", days[-2:])

if "Friday" in days:
    print("Friday is present in the tuple.")
else:
    print("Friday is not present in the tuple.")

# Tuple Practice Problems - 3

students = ("Alice", "Bob", "Charlie", "Alice", "Eve")

name = input("Enter a student name: ")

if name in students:
    position = students.index(name)
    count = students.count(name)
    print(f"{name} is at position {position}")
    print(f"{name} appears {count} time(s) in the tuple.")
else:
    print(f"{name} is not found in the tuple.")

