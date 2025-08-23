# pip install pandas

import pandas as pd

# Create and print a Series
s = pd.Series([10, 20, 30, 40])
print("Pandas Series s:")
print(s)

# Create and print a DataFrame
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print("\nPandas DataFrame df:")
print(df)

# Use data2 here for df2
data2 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Score': [85, 90, 78, 92, 88, 75]
}
df2 = pd.DataFrame(data2)

print("\nFirst 5 rows of df2:")
print(df2.head())      # Default is 5 rows

print("\nFirst 3 rows of df2:")
print(df2.head(3))     # First 3 rows

print("\nLast 5 rows of df2:")
print(df2.tail())      # Default is 5 rows

print("\nLast 2 rows of df2:")
print(df2.tail(2))     # Last 2 rows
