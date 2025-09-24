# dictionary =  a collection of {key:value} pairs
#               ordered (Python 3.7+ maintains insertion order)
#               changeable (you can update, add, or remove)
#               no duplicate keys allowed

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# ------------------- INSPECTING A DICTIONARY -------------------

# print(dir(capitals))   # shows all available dictionary methods
# print(help(capitals))  # shows detailed help about dict class
# print(capitals.get("Japan"))   # safely get value (returns None if not found)

# ------------------- CHECKING IF A KEY EXISTS -------------------

# if capitals.get("Russia"):   # .get() avoids error if key doesn’t exist
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# ------------------- ADDING / UPDATING -------------------

# capitals.update({"Germany": "Berlin"})   # adds a new key-value pair
# capitals.update({"USA": "Detroit"})      # updates an existing key

# ------------------- REMOVING -------------------

# capitals.pop("China")   # removes the entry with key "China"
# capitals.popitem()      # removes the last inserted item
# capitals.clear()        # clears the entire dictionary

# ------------------- ITERATING -------------------

# keys = capitals.keys()      # gets all keys
# for key in capitals.keys():
#     print(key)

# values = capitals.values()  # gets all values
# for value in capitals.values():
#     print(value)

# items = capitals.items()    # gets all (key, value) pairs
# for key, value in capitals.items():
#     print(f"{key}: {value}")
