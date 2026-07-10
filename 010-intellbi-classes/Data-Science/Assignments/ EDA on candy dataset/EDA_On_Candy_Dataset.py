import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read the csv file
df = pd.read_csv(r"C:\Users\deeks\Desktop\python\python-repo\010-intellbi-classes\Data-Science\Assignments\ EDA on candy dataset\candy.csv")


print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData type of each column:")
print(df.dtypes)

print("\nBasic information about dataset:")
print(df.info())

print("\nSummary of numeric columns:")
print(df.describe())


# Check missing values
print("\nMissing values in each column:")
print(df.isnull().sum())


# Check duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())


# Check for wrong values in Yes/No columns;

binary_cols = [
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

print("\nUnique values in binary columns:")
for col in binary_cols:
    print(col, ":", df[col].unique())


## convert categorical variables into numerical format
# Convert Yes/No columns into 1/0

for col in binary_cols:
    df[col] = df[col].replace({"Yes": 1, "No": 0})

print("\nData after converting Yes/No to 1/0:")
print(df.head())


# Univariate analysis
print("\nCount of candies with chocolate:")
print(df["chocolate"].value_counts())

print("\nCount of candies with fruity flavor:")
print(df["fruity"].value_counts())

#   sorted the candies by winpercent to find the top 10 most popular candies.
#   This helps us understand which candies have the highest winning percentage.
print("\nTop 10 candies by winpercent:")
print(df[["competitorname", "winpercent"]].sort_values("winpercent", ascending=False).head(10))


# Bivariate analysis
print("\nAverage winpercent by chocolate:")
print(df.groupby("chocolate")["winpercent"].mean())

print("\nAverage winpercent by fruity:")
print(df.groupby("fruity")["winpercent"].mean())

print("\nCorrelation between numeric columns:")
print(df[["sugarpercent", "pricepercent", "winpercent"]].corr())


# Outlier detection using IQR for numeric columns
print("\nOutlier count using IQR:")
numeric_cols = ["sugarpercent", "pricepercent", "winpercent"]

for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(col, ":", len(outliers))


# # Simple visualizations
# plt.figure(figsize=(8, 4))
# sns.histplot(df["winpercent"], bins=15, kde=True)
# plt.title("Distribution of Win Percent")
# plt.show()
#
# plt.figure(figsize=(8, 4))
# sns.boxplot(x=df["winpercent"])
# plt.title("Boxplot of Win Percent")
# plt.show()
#
# plt.figure(figsize=(8, 5))
# sns.scatterplot(x=df["pricepercent"], y=df["winpercent"])
# plt.title("Price Percent vs Win Percent")
# plt.show()
#
# plt.figure(figsize=(8, 5))
# sns.heatmap(df[["sugarpercent", "pricepercent", "winpercent"]].corr(), annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()
#
#
# print("\nFinal check completed.")
