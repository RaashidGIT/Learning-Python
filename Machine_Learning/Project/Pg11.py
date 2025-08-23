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

# New data and DataFrame
data2 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Score': [85, 90, 78, 92, 88, 75]
}

# Create df2 from data2 (not data)
df2 = pd.DataFrame(data2)

print("\nFirst 5 rows of df2:")
print(df2.head())

print("\nFirst 3 rows of df2:")
print(df2.head(3))
