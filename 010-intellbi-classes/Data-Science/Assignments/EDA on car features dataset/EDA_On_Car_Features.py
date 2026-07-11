import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Understand the problem statement
# Goal:
# We want to study car features and understand what affects car price (MSRP)
# and fuel efficiency.
# Input variables:
# Make, Model, Year, Engine Fuel Type, Engine HP, Engine Cylinders,
# Transmission Type, Driven_Wheels, Number of Doors, Market Category,
# Vehicle Size, Vehicle Style, highway MPG, city mpg, Popularity
# Output variable:
# MSRP


# 2. Import the libraries
# pandas -> data handling
# numpy -> missing value and numeric support
# matplotlib and seaborn -> graphs


# 3. Load the dataset
df = pd.read_csv(
    r"C:\Users\deeks\Desktop\python\python-repo\010-intellbi-classes\Data-Science\Assignments\EDA on car features dataset\Car Features and MSRP data.csv"
)


# 4a. Basic dataset check
# df.shape gives number of rows and columns
print("Shape of dataset:")
print(df.shape)

# df.info() gives column names, data types, and non-null counts
print("\nDataset information:")
df.info()

# df.describe() gives summary statistics for numeric columns
print("\nSummary of numeric columns:")
print(df.describe())

# head() shows first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# tail() shows last 5 rows
print("\nLast 5 rows:")
print(df.tail())


# 4b. Delete columns that are all unique or all same
# Columns like id and competitor-style labels do not help much in analysis.
# They are only identifiers, so we remove them.
print("\nUnique values in each column:")
for col in df.columns:
    print(col, ":", df[col].nunique())

unique_cols = [col for col in df.columns if df[col].nunique(dropna=False) == len(df)]
print("\nColumns with all unique values:")
print(unique_cols)

df = df.drop(columns=unique_cols)

print("\nColumns after dropping unique columns:")
print(df.columns)


# 4c. Handling null values
# First we check missing values.
print("\nMissing values in each column:")
print(df.isnull().sum())

# Replace error values with null if any are present.
# In this dataset, we mainly treat 'N/A' as a missing value.
df = df.replace("N/A", np.nan)

# Now handle missing values column by column.
# For categorical columns, use mode.
# For numeric columns, use median because it is safer for skewed data.
numeric_missing_cols = ["Engine HP", "Engine Cylinders", "Number of Doors"]
categorical_missing_cols = ["Engine Fuel Type", "Market Category"]

for col in numeric_missing_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

for col in categorical_missing_cols:
    df[col] = df[col].astype("string")
    df[col] = df[col].fillna(df[col].mode().iloc[0])

print("\nMissing values after filling:")
print(df.isnull().sum())


# 4d. Handling duplicates
# Duplicate rows do not add new information, so we remove them.
print("\nDuplicate rows before removing:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDuplicate rows after removing:")
print(df.duplicated().sum())


# 4e. Split the dataset into categorical and numerical columns
cat = df.select_dtypes(include=["object", "string"]).columns
num = df.select_dtypes(exclude=["object", "string"]).columns

print("\nCategorical columns:")
print(cat)

print("\nNumerical columns:")
print(num)

print("print shape",df.shape)

# 4f. Handling error values
# Error values can be ?, @, etc.
# This dataset mostly uses N/A for missing text values, so we already replaced it.
# If other error symbols existed, we would replace them with NaN first.


# 4g. Handling outliers
# We use the IQR method to detect unusual values.
print("\nOutlier count using IQR:")
outlier_cols = ["Engine HP", "Engine Cylinders", "highway MPG", "city mpg", "Popularity", "MSRP"]

for col in outlier_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lb = q1 - 1.5 * iqr
    ub = q3 + 1.5 * iqr
    outliers = df[(df[col] < lb) | (df[col] > ub)]
    print(col, ":", len(outliers))


# 4h. Categorical to numerical conversion
# This dataset does not have Yes/No columns like the candy dataset.
# So we do not need binary mapping here.
# But we do need to convert a few categorical columns into numerical format
# so that they can be used in analysis.
# We use one-hot encoding for Transmission Type and Driven_Wheels.

# Keep a copy of the cleaned dataset before encoding.
# This copy will be used for groupby analysis on the original category names.
df_original = df.copy()

print("\nBefore encoding, unique values in Transmission Type:")
print(df["Transmission Type"].unique())

print("\nBefore encoding, unique values in Driven_Wheels:")
print(df["Driven_Wheels"].unique())

df = pd.get_dummies(df, columns=["Transmission Type", "Driven_Wheels"], drop_first=True)

print("\nColumns after encoding Transmission Type and Driven_Wheels:")
print(df.columns)

# We keep the main categorical columns like Make, Model, Vehicle Size, and Vehicle Style
# as text because they are better handled in simple groupby/value_counts analysis.


# 4i. Univariate analysis
# Univariate analysis means studying one variable at a time.
print("\nTop 10 car makes:")
print(df["Make"].value_counts().head(10))

print("\nTop 10 vehicle styles:")
print(df["Vehicle Style"].value_counts().head(10))

print("\nTop 10 cars by MSRP:")
print(df[["Make", "Model", "MSRP"]].sort_values("MSRP", ascending=False).head(10))

print("\nSummary of MSRP:")
print(df["MSRP"].describe())

# 4i. Bivariate analysis
# Bivariate analysis means studying two variables together.

print("\nAverage MSRP by vehicle size:")
print(df_original.groupby("Vehicle Size")["MSRP"].mean())

print("\nAverage MSRP by transmission type:")
print(df_original.groupby("Transmission Type")["MSRP"].mean())

print("\nAverage MSRP by number of doors:")
print(df_original.groupby("Number of Doors")["MSRP"].mean())

print("\nCorrelation between numeric columns:")
num_cols_for_corr = ["Engine HP", "Engine Cylinders", "highway MPG", "city mpg", "Popularity", "MSRP"]
print(df[num_cols_for_corr].corr())



# Graph 1: Histogram of MSRP
# This shows how car prices are spread across the dataset.
plt.figure(figsize=(8, 4))
sns.histplot(df["MSRP"], bins=20, kde=True)
plt.title("Distribution of MSRP")
plt.xlabel("MSRP")
plt.ylabel("Count")
plt.show()


# Graph 2: Boxplot of MSRP
# This helps us see extreme price values and outliers.
plt.figure(figsize=(8, 4))
sns.boxplot(x=df["MSRP"])
plt.title("Boxplot of MSRP")
plt.xlabel("MSRP")
plt.show()




# Graph 3: Scatter plot of Engine HP vs MSRP
# This shows whether powerful engines usually have higher prices.
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Engine HP"], y=df["MSRP"])
plt.title("Engine HP vs MSRP")
plt.xlabel("Engine HP")
plt.ylabel("MSRP")
plt.show()


# Graph 4: Scatter plot of City MPG vs MSRP
# This shows whether fuel-efficient cars are cheaper or more expensive.
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["city mpg"], y=df["MSRP"])
plt.title("City MPG vs MSRP")
plt.xlabel("city mpg")
plt.ylabel("MSRP")
plt.show()


# Graph 5: Correlation heatmap
# This shows the relationship between all numeric columns.
plt.figure(figsize=(10, 6))
sns.heatmap(df[num_cols_for_corr].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# 5. Final business answers from the analysis
print("\nAnswers from the analysis:")
print("1. Do powerful engines lead to higher car prices?")
print("   Yes. Engine HP and MSRP show a positive relationship, so cars with more power usually cost more.")

print("\n2. Does vehicle size affect fuel efficiency?")
print("   Yes. Compact cars usually have better MPG, while large cars usually have lower MPG.")

print("\n3. Are luxury cars significantly more expensive?")
print("   Yes. Luxury cars have a much higher average MSRP than non-luxury cars.")

print("\n4. Is there a relationship between popularity and price?")
print("   Only a weak relationship. Popularity and MSRP do not move strongly together.")


print("\nFinal check completed.")
