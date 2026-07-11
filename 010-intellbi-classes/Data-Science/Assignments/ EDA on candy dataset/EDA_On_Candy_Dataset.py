import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Understand the problem statement
# Goal:
# We need to study the candy dataset and understand which candy features
# are related to winpercent, which is the output variable.
# Input variables:
# chocolate, fruity, caramel, peanutyalmondy, nougat, crispedricewafer,
# hard, bar, pluribus, sugarpercent, pricepercent
# Output variable:
# winpercent


# 2. Import the libraries
# pandas -> data handling
# numpy -> missing value / numeric support
# matplotlib and seaborn -> graphs


# 3. Load the dataset
df = pd.read_csv(r"C:\Users\deeks\Desktop\python\python-repo\010-intellbi-classes\Data-Science\Assignments\ EDA on candy dataset\candy.csv")


# 4a. Basic dataset check
# df.shape gives rows and columns
print("Shape of dataset:")
print(df.shape)

# df.info() gives column names, data types, and non-null counts
print("\nDataset information:")
print(df.info())

# df.describe() gives summary for numeric columns
print("\nSummary of numeric columns:")
print(df.describe())

# head() shows first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# tail() shows last 5 rows
print("\nLast 5 rows:")
print(df.tail())


# 4b. Delete columns that are all unique or same
# id is only an identifier, so it does not help in analysis.
# competitorname is also an identifier-style column, so we can drop it for EDA.
print("\nUnique values in each column:")
for col in df.columns:
    print(col, ":", df[col].nunique())

df = df.drop(["id", "competitorname"], axis=1)

print("\nColumns after dropping identifier columns:")
print(df.columns)


# 4c. Handling null values
# First, check if there are null values.
print("\nNull values in each column:")
print(df.isnull().sum())

# This dataset does not have null values, so no filling is needed here.
# If there were nulls:
# - categorical columns -> mode
# - continuous numeric columns -> mean
# - discrete numeric columns -> median


# 4d. Handling duplicates
print("\nDuplicate rows in dataset:")
print(df.duplicated().sum())

# Remove duplicate rows if any exist.
df = df.drop_duplicates()

print("\nDuplicate rows after removing duplicates:")
print(df.duplicated().sum())


# 4e. Split dataset into categorical and numerical columns
cat = df.select_dtypes(include="object").columns
num = df.select_dtypes(exclude="object").columns

print("\nCategorical columns:")
print(cat)

print("\nNumerical columns:")
print(num)


# 4f. Handling error values
# Error values can be symbols like ?, @, etc.
# The candy dataset does not contain such error values.
# If they were present, we would replace them with NaN using:
# df.replace("?", np.nan)


# 4g. Handling outliers
# We check outliers using the IQR method.
# Since winpercent, sugarpercent, and pricepercent are numeric, we use them here.
print("\nOutlier count using IQR:")
numeric_cols = ["sugarpercent", "pricepercent", "winpercent"]

for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lb = q1 - 1.5 * iqr
    ub = q3 + 1.5 * iqr
    outlier_rows = df[(df[col] < lb) | (df[col] > ub)]
    print(col, ":", len(outlier_rows))


# 4h. Categorical to numerical conversion
# The binary columns contain Yes/No values.
# We convert them to 1/0 so that we can do numerical analysis like correlation.
yes_no_cols = [
    "chocolate",
    "fruity",
    "caramel",
    "peanutyalmondy",
    "nougat",
    "crispedricewafer",
    "hard",
    "bar",
    "pluribus",
]

print("\nUnique values before conversion:")
for col in yes_no_cols:
    print(col, ":", df[col].unique())

for col in yes_no_cols:
    df[col] = df[col].map({"Yes": 1, "No": 0})

print("\nData after converting Yes/No to 1/0:")
print(df.head())


# 4i. Univariate analysis
# Univariate analysis means studying one variable at a time.

print("\nCount of 1 and 0 values in each binary column:")
for col in yes_no_cols:
    print("\n", col)
    print(df[col].value_counts())

print("\nTop 10 candies by winpercent:")
print(df[["winpercent"]].sort_values("winpercent", ascending=False).head(10))

print("\nHistogram of winpercent:")
# This graph shows how winpercent values are distributed.
plt.figure(figsize=(8, 4))
sns.histplot(df["winpercent"], bins=15, kde=True)
plt.title("Distribution of Win Percent")
plt.xlabel("winpercent")
plt.ylabel("Count")
plt.show()


# 4i. Bivariate analysis
# Bivariate analysis means studying two variables together.

print("\nAverage winpercent for chocolate and non-chocolate candies:")
print(df.groupby("chocolate")["winpercent"].mean())

print("\nAverage winpercent for fruity and non-fruity candies:")
print(df.groupby("fruity")["winpercent"].mean())

print("\nCorrelation between numeric columns:")
print(df[["sugarpercent", "pricepercent", "winpercent"]].corr())

print("\nCorrelation heatmap:")
# This graph shows the relationship between sugarpercent, pricepercent, and winpercent.
plt.figure(figsize=(8, 5))
sns.heatmap(df[["sugarpercent", "pricepercent", "winpercent"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("\nScatter plot between pricepercent and winpercent:")
# This graph shows whether expensive candies tend to have higher or lower winpercent.
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["pricepercent"], y=df["winpercent"])
plt.title("Price Percent vs Win Percent")
plt.xlabel("pricepercent")
plt.ylabel("winpercent")
plt.show()

print("\nBoxplot of winpercent:")
# This graph helps us spot extreme values in winpercent.
plt.figure(figsize=(8, 4))
sns.boxplot(x=df["winpercent"])
plt.title("Boxplot of Win Percent")
plt.xlabel("winpercent")
plt.show()


# Final check
print("\nFinal check completed.")
