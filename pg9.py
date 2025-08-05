# -----------------------------------------
# PYTHON TEMPERATURE CONVERTER
# -----------------------------------------

# Tip: To type the degree symbol (°)
# Windows: Hold Alt and type 0176 → Alt+0176
# macOS: Option + Shift + 8
# Or just copy-paste this: °

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    # Convert Celsius to Fahrenheit
    converted = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {converted}°F")
elif unit == "F":
    # Convert Fahrenheit to Celsius
    converted = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {converted}°C")
else:
    print(f"'{unit}' is an invalid unit. Please enter 'C' or 'F'.")
