# type casting = The process of converting a value from one data type to another
#                (string, integer, float, boolean)
#                Can be Explicit (manual) or Implicit (automatic)

name = "Bro"
age = 21
gpa = 1.9
student = True

# Check original data types
# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student)) 

# Explicit type casting
age = float(age)          # int to float
print(age)

gpa = int(gpa)            # float to int (decimal part truncated)
print(gpa)

student = str(student)    # boolean to string
print(student)

name = bool(name)         # non-empty string to boolean (evaluates to True)
print(name)
