# -------------------------------------------------------------
# AIM: To understand and demonstrate how to use the 
#      match-case statement in Python (introduced in Python 3.10).
#
# The match-case statement is an alternative to using many 'elif' 
# statements. It allows you to execute code if a value matches 
# a specific 'case'.
#
# Benefits:
#   - Cleaner than multiple if-elif conditions
#   - Easier to read and maintain
#
# General Syntax:
#   match variable:
#       case value1 | value2:   # if variable matches value1 or value2
#           # code block
#       case value3:
#           # code block
#       case _:
#           # default case (like "else")
# -------------------------------------------------------------

# --------------------
# EXAMPLE: Check if a day is a weekend
# --------------------
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True      # Weekend
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False     # Weekday
        case _:              # Default case (when no match is found)
            return False


# --------------------
# TESTING THE FUNCTION
# --------------------
print("Is Monday a weekend? :", is_weekend("Monday"))   # Expected: False
print("Is Sunday a weekend? :", is_weekend("Sunday"))   # Expected: True
print("Is Holiday a weekend? :", is_weekend("Holiday")) # Expected: False
