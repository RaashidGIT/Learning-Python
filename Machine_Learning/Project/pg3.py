# Set Problem - 1

subjects = {"Math", "Science", "English", "History", "Computer"}

subjects.add("Art")

subjects.discard("History")

print("Subjects chosen by students:")
for subject in subjects:
    print("-", subject)

print("\nTotal number of unique subjects:", len(subjects))

# Set Problem - 2

student_a_hobbies = {"reading", "swimming", "coding", "painting"}
student_b_hobbies = {"cycling", "coding", "painting", "gaming"}

common_hobbies = student_a_hobbies & student_b_hobbies
print("Common hobbies:", common_hobbies)

unique_to_a = student_a_hobbies - student_b_hobbies
print("Hobbies unique to Student A:", unique_to_a)

all_hobbies = student_a_hobbies | student_b_hobbies
print("All hobbies (combined):", all_hobbies)

# Set Problem - 3

fruits = {"apple", "banana", "mango", "orange", "grape"}

fruit_name = input("Enter a fruit name: ").strip().lower()

if fruit_name in fruits:
    print(f"{fruit_name} is present in the set.")
else:
    print(f"{fruit_name} is not present in the set.")
