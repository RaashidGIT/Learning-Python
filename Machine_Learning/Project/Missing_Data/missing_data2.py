import pandas as pd
data = pd.read_csv(r"C:\Users\user\Documents\MISSING_DATASET_HANDLING.csv", encoding = 'latin1')
print(data.isnull().sum())

data = data.drop(columns=["ADDRESSLINE2"]) # drops the column named ADDRESSLINE2
print(data.isnull().sum())
