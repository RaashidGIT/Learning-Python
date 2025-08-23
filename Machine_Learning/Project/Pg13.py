# pip install pandas

import pandas as pd

# Create sample data with one missing value
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New york', 'Los angeles', None]  # 'Charlie' has a missing city
}
df = pd.DataFrame(data, index=['a', 'b', 'c'])

# Label-based indexing examples
print("Row with index 'a':")
print(df.loc['a'])

print("\nValue at row 'b', column 'name':")
print(df.loc['b', 'name'])

print("\nAll rows, columns 'name' and 'city':")
print(df.loc[:, ['name', 'city']])

# Position-based indexing examples
print("\nFirst row by position (iloc[0]):")
print(df.iloc[0])

print("\nValue at row 1, column 0 (iloc[1, 0]):")
print(df.iloc[1, 0])

print("\nAll rows, columns 0 and 1 (iloc[:, 0:2]):")
print(df.iloc[:, 0:2])

# Create df2 with default integer index
df2 = pd.DataFrame(data)

# Check for missing values
print("\nCheck for missing values with df.isnull():")
print(df.isnull())

# Drop rows that contain any missing values (NaN or None)
print("\nDataFrame after dropping rows with missing values (dropna):")
print(df.dropna())

# Fill missing values with 0 (useful for numeric or placeholder values)
print("\nDataFrame after filling missing values with 0 (fillna):")
print(df.fillna(0))
