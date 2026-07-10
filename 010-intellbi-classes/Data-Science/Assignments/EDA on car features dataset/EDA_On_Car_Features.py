import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read the csv file
df = pd.read_csv(
    r"C:\Users\deeks\Desktop\python\python-repo\010-intellbi-classes\Data-Science\Assignments\EDA on car features dataset\Car Features and MSRP data.csv"
)


print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nBasic info:")
print(df.info())

print("\nSummary of numeric columns:")
print(df.describe())


# Check missing values
print("\nMissing values in each column:")
print(df.isnull().sum())


# Check duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())


# Clean missing values
# For numeric columns, fill with median
numeric_cols = ["Engine HP", "Engine Cylinders", "Number of Doors"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

# For text columns, fill with mode
text_cols = ["Engine Fuel Type", "Market Category"]
for col in text_cols:
    df[col] = df[col].replace("N/A", pd.NA)
    df[col] = df[col].fillna(df[col].mode()[0])


# Remove duplicate rows
df = df.drop_duplicates()


print("\nData after cleaning:")
print(df.head())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())


# Univariate analysis
print("\nTop 10 car makes:")
print(df["Make"].value_counts().head(10))

print("\nTop 10 car styles:")
print(df["Vehicle Style"].value_counts().head(10))

print("\nTop 10 cars by MSRP:")
print(df[["Make", "Model", "MSRP"]].sort_values("MSRP", ascending=False).head(10))

print("\nSummary of MSRP:")
print(df["MSRP"].describe())


# Bivariate analysis
print("\nAverage MSRP by vehicle size:")
print(df.groupby("Vehicle Size")["MSRP"].mean())

print("\nAverage MSRP by transmission type:")
print(df.groupby("Transmission Type")["MSRP"].mean())

print("\nAverage MSRP by number of doors:")
print(df.groupby("Number of Doors")["MSRP"].mean())

print("\nCorrelation between numeric columns:")
print(df[["Engine HP", "Engine Cylinders", "highway MPG", "city mpg", "Popularity", "MSRP"]].corr())


# Outlier detection using IQR
print("\nOutlier count using IQR:")
for col in ["Engine HP", "Engine Cylinders", "highway MPG", "city mpg", "MSRP"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(col, ":", len(outliers))


# # Simple visualizations
# plt.figure(figsize=(8, 4))
# sns.histplot(df["MSRP"], bins=20, kde=True)
# plt.title("Distribution of MSRP")
# plt.show()
#
# plt.figure(figsize=(8, 4))
# sns.boxplot(x=df["MSRP"])
# plt.title("Boxplot of MSRP")
# plt.show()
#
# plt.figure(figsize=(8, 5))
# sns.scatterplot(x=df["Engine HP"], y=df["MSRP"])
# plt.title("Engine HP vs MSRP")
# plt.show()
#
# plt.figure(figsize=(8, 5))
# sns.scatterplot(x=df["city mpg"], y=df["MSRP"])
# plt.title("City MPG vs MSRP")
# plt.show()
#
# plt.figure(figsize=(10, 6))
# sns.heatmap(df[["Engine HP", "Engine Cylinders", "highway MPG", "city mpg", "Popularity", "MSRP"]].corr(), annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()
#
#
# print("\nFinal check completed.")
