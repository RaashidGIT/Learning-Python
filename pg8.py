# -----------------------------------------
# PYTHON WEIGHT CONVERTER
# -----------------------------------------

weight = float(input("Enter your weight: "))
unit = input("Is the weight in Kilograms or Pounds? (K or L): ").strip().upper()

if unit == "K":
    weight_in_lbs = weight * 2.205
    print(f"Your weight is: {round(weight_in_lbs, 1)} Lbs.")
elif unit == "L":
    weight_in_kgs = weight / 2.205
    print(f"Your weight is: {round(weight_in_kgs, 1)} Kgs.")
else:
    print(f"'{unit}' is not a valid unit. Please enter 'K' for Kilograms or 'L' for Pounds.")
