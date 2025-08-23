import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New york', 'Los angeles', 'Chicago']
}
df = pd.DataFrame(data, index=['a', 'b', 'c'])

# Using label-based indexing
print(df.loc['a'])               # Row with label 'a'
print(df.loc['b', 'name'])       # Value in row 'b', column 'name'
print(df.loc[:, ['name', 'city']])  # All rows, columns 'name' and 'city'

# Using position-based indexing
print(df.iloc[0])                # First row (position 0)
print(df.iloc[1, 0])             # Row 1, column 0
print(df.iloc[:, 0:2])           # All rows, columns 0 and 1 (slices up to 2)
