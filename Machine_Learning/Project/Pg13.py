# pip install pandas

import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New york', 'Los angeles', None]
}
df = pd.DataFrame(data, index=['a', 'b', 'c'])

# Label-based indexing
print(df.loc['a'])                # Row with index 'a'
print(df.loc['b', 'name'])        # Value at row 'b', column 'name'
print(df.loc[:, ['name', 'city']])  # All rows, columns 'name' and 'city'

# Position-based indexing
print(df.iloc[0])                 # First row by position
print(df.iloc[1, 0])              # Row 1, column 0 (second row, first column)
print(df.iloc[:, 0:2])            # All rows, columns 0 and 1

df2 = pd.DataFrame(data)          # DataFrame without custom index (default 0,1,2)

# Check for missing values in df
print("\nCheck for missing values with df.isnull():")
print(df.isnull())
# Drop rows that contain any missing values (NaN or None)
# This removes any row that has at least one missing value
print("\nDataFrame after dropping rows with missing values (dropna):")
print(df.dropna())
