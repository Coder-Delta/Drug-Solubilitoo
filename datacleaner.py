# In this projec we will clean and visulaze a real data-set
# 1. Download the data from official source.
# 2. clean and fill the data.
# 3. visulize the data in matplotlib

# Programe start from here.

import matplotlib
import pandas as pd

url = "https://raw.githubusercontent.com/deepchem/deepchem/master/datasets/delaney-processed.csv"
df = pd.read_csv(url)
df.to_csv("esol.csv", index=False)

print("Shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nFirst 5 rows:")
df.head()

print("Missing values per column:")
print(df.isnull().sum())

print("\nMissing % per column:")
print((df.isnull().sum() / len(df) * 100).round(2))
