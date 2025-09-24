# 🌟 Python Example: List vs Set vs Tuple

# 🔹 List: Ordered, Changeable, Allows Duplicates
print("List Example")
fruits = ['apple', 'banana', 'apple', 'cherry']
print("Original list:", fruits)

fruits.append('orange')         # Add item at the end
fruits.insert(1, 'mango')       # Insert at index 1
fruits.remove('banana')         # Remove item by value
fruits[0] = 'grape'             # Modify first item
print("Modified list:", fruits)
print("First fruit:", fruits[0])
print("Number of fruits:", len(fruits))
print()

# 🔹 Set: Unordered, Changeable, No Duplicates
print("Set Example")
colors = {'red', 'blue', 'green', 'red'}
print("Original set (no duplicates):", colors)

colors.add('yellow')            # Add new item
colors.discard('blue')          # Remove item safely
print("Modified set:", colors)
print("Is 'green' in set?", 'green' in colors)
print()

# 🔹 Tuple: Ordered, Unchangeable, Allows Duplicates
print("Tuple Example")
coordinates = (10, 20, 10)
print("Original tuple:", coordinates)

print("First coordinate:", coordinates[0])
print("Count of 10:", coordinates.count(10))
print("Index of 20:", coordinates.index(20))
print("Length of tuple:", len(coordinates))
