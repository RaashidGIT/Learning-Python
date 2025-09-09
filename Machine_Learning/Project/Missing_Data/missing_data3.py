import pandas as pd
data = pd.read_csv(r"C:\Users\user\Documents\MISSING_DATASET_HANDLING.csv", encoding = 'latin1')

data = data.dropna(subset = ["ORDERDATE", "PRODUCTLINE"]) # deletes the row with missing value
print(data.isnull().sum())
