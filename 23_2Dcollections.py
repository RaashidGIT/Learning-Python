# Exploring Different 2D Collections in Python

# ---------------------------
# 2D List of Lists
print("\n2D List of Lists")
num_pad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]
]
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# ---------------------------
# 2D List of Tuples
print("\n 2D List of Tuples")
num_pad = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
]
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# ---------------------------
# 2D List of Sets
print("\n2D List of Sets (unordered rows)")
num_pad = [
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {"*", 0, "#"}
]
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# ---------------------------
# 2D Tuple of Lists
print("\n 2D Tuple of Lists")
num_pad = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]
)
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# ---------------------------
# 2D Tuple of Tuples
print("\n 2D Tuple of Tuples")
num_pad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
)
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# ---------------------------
# 2D Tuple of Sets (unordered rows)
print("\n 2D Tuple of Sets")
num_pad = (
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {"*", 0, "#"}
)
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# ---------------------------
# 2D Set of Lists – NOT VALID
print("\n2D Set of Lists – Invalid (lists are unhashable)")
print("Cannot create a set containing lists – will cause TypeError.")

# ---------------------------
# 2D Set of Tuples
print("\n 2D Set of Tuples")
num_pad = {
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
}
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# ---------------------------
# 2D Set of Sets – NOT VALID
print("\n2D Set of Sets – Invalid (sets are unhashable)")
print("Cannot create a set containing sets – will cause TypeError.")
