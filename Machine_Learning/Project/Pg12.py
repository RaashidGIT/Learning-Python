import pandas as pd

# Create and print a Series
s = pd.Series([10, 20, 30, 40])
print("Pandas Series s:")
print(s)

# Create and print DataFrame df1
data1 = {'name': ['Alice', 'Bob'], 'Age': [25, 30]}
df1 = pd.DataFrame(data1)
print("\nDataFrame df1:")
print(df1)

# Create DataFrame df2 with more data
data2 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'score': [85, 90, 78, 92, 88, 75]
}
df2 = pd.DataFrame(data2)

print("\nFirst 5 rows of df2 (default head):")
print(df2.head())

print("\nFirst 3 rows of df2:")
print(df2.head(3))

print("\nInfo about df2:")
df2.info()

print("\nSummary statistics of df2:")
print(df2.describe())

print("\nColumn names of df2:")
print(df2.columns)

print("\nShape of df2 (rows, columns):")
print(df2.shape)
