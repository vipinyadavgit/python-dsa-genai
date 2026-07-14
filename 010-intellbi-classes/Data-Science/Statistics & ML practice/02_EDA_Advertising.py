import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pyparsing import col

#df  =   pd.read_csv(r"C:\Users\deeks\Desktop\python\python-repo\010-intellbi-classes\Data-Science\Dataset_DS\Advertisement_Dataset.csv")
print("Loading data...")
df = pd.read_csv("../Dataset_DS/Advertisement_Dataset.csv")
print("Data Loaded")

print("\nPrint top 5 rows")
print(df.head())

print("\nPrint bottom 5 rows")
print(df.tail())

print("\nTotal  number of rows and columns")
print(df.shape)

print(''' \n Info() :-
Index range → e.g., RangeIndex: 100 entries, 0 to 99
Column names → all columns in the DataFrame
Non‑null counts → how many values are present (helps spot missing data)
Data types → int64, float64, object (strings), etc.
Memory usage → how much memory the DataFrame consumes''')
df.info()

print('''\n generates summary statistics for numeric columns in your DataFrame,
      means transpose.It flips the rows and columns.
      So instead of statistics being rows and columns being features, 
      you get features as rows and statistics as columns''')
print(df.describe().T)

print('''\n Drop the column which has all unique value or has all same values
         because it does not adds any value''')

#df.dropna(subset=['NO'], inplace=True)
df.drop('No',axis=1,inplace=True)

print(df.head())

print('''\n check null values''')
print(df.isnull().sum())
#print(df.isnull().sum().sort_values(ascending=False))

print("\nSplit the dataset into categorical and numerical columns")
cat = df.select_dtypes(include='object').columns
num = df.select_dtypes(exclude='object').columns

print(cat)
print(num)

print(df.isnull().sum())

print("\nHandling outliers")
print("\n Outlier count using IQR:")
outlier_col = ["TV","Radio","Newspaper","Sales"]

for col in outlier_col:

    q1=df[col].quantile(0.25)
    q3=df[col].quantile(0.75)
    iqr = q3 - q1
    lb= q1-1.5*iqr
    ub= q3+1.5*iqr
    print(col,"iqr", ":", iqr)

    outliers = df[(df[col] < lb) | (df[col] > ub)]
    print("lower band",lb)
    print("upper band",ub)
    print(col,"outliers", ":", len(outliers))

    print("removing outliers from dataframe")
    df = df[(df[col] >= lb) & (df[col] <= ub)]
    print("\n")


print(df.head())

print(df.shape)

print("\n univariate analysis")
'''
What standard things are usually checked in univariate analysis

For numeric columns:
•minimum
•maximum
•mean
•median
•spread
•outliers
•histogram
•boxplot

For categorical columns:
•unique values
•most common category
•count of each category
'''

# 4i. Bivariate analysis
# Bivariate analysis means studying two variables together.

print("\n bivariate analysis")
print(df.corr())

