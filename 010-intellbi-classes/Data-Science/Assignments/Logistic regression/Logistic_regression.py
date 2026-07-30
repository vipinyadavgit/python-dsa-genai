"""
Logistic Regression

Task:
Predict 10-year risk of coronary heart disease (CHD).

Output variable:
TenYearCHD
0 = No
1 = Yes
"""

# Step 1: Import the required libraries.
# pandas is used to read and work with the CSV file.
# matplotlib and seaborn are used for graphs.
# sklearn is used to build and test the machine learning model.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split


# Step 2: Load the dataset.
# We use the file that is attached with the assignment.
file_path = r"C:\Users\deeks\Desktop\python\python-repo\010-intellbi-classes\Data-Science\Dataset_DS\heart disease.csv"
# "NA" in the file means missing value, so we convert it to proper nulls while loading.
df = pd.read_csv(file_path)


# Step 3: Check the dataset.
# shape tells us the number of rows and columns.
print("Dataset shape:", df.shape)

# info() shows column names and data types.
print("\nDataset info:")
print(df.info())

# describe() gives basic statistics like count, mean, min, and max.
print("\nDataset description:")
print(df.describe())

# head() shows the first few rows of the dataset.
print("\nFirst 5 rows:")
print(df.head())


# Step 4: Check for missing values and duplicate rows.
# This dataset has missing values, so we need to handle them.
print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())


# Step 5: Separate categorical and numerical columns.
# This helps us decide how to fill missing values.
cat_cols = df.select_dtypes(include="object").columns
num_cols = df.select_dtypes(exclude="object").columns

print("\nCategorical columns:", list(cat_cols))
print("Numerical columns:", list(num_cols))


# Step 6: Handle missing values.
# For numerical columns, we fill missing values with the median.
# Median is a good choice because it is less affected by outliers.
for column in num_cols:
    if column != "TenYearCHD":
        df[column] = df[column].fillna(df[column].median())

# The target column should not have missing values, but we keep this check for safety.
df = df.dropna(subset=["TenYearCHD"])

# If there were any categorical columns, we would fill them with the mode.
# This dataset does not have object columns after loading, so no encoding is needed here.


# Step 7: Check for outliers using the IQR method.
# We calculate the bounds for each numerical column, then remove rows that fall outside those bounds.
num_cols_no_target = [col for col in num_cols if col != "TenYearCHD"]
q1 = df[num_cols_no_target].quantile(0.25)
q3 = df[num_cols_no_target].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print("\nOutlier detection using IQR:")
print("Q1:")
print(q1)
print("\nQ3:")
print(q3)
print("\nIQR:")
print(iqr)
print("\nLower bounds:")
print(lower_bound)
print("\nUpper bounds:")
print(upper_bound)

# Keep only the rows where every numerical feature is within the IQR limits.
for col in num_cols_no_target:
    df = df[(df[col] >= lower_bound[col]) & (df[col] <= upper_bound[col])]

print("\nShape after outlier removal:", df.shape)



# Step 8: Univariate analysis.
# Histogram shows the distribution of the target variable.
plt.figure(figsize=(6, 4))
sns.countplot(x="TenYearCHD", data=df)
plt.title("Distribution of TenYearCHD")
plt.xlabel("TenYearCHD")
plt.ylabel("Count")
plt.show()

# Heatmap shows correlation between numerical columns.
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()


# Step 9: Split the data into input and output.
# X contains all the input variables.
# y contains the output variable.
X = df.drop("TenYearCHD", axis=1)
y = df["TenYearCHD"]


# Step 10: Split the dataset into training and testing parts.
# Training data is used to teach the model.
# Testing data is used to check how well the model works.
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2 )


# Step 11: Create the model.
# LogisticRegression() creates the logistic regression classifier.
model = LogisticRegression(max_iter=1000)


# Step 12: Train the model.
# The model learns the relationship between the input columns and TenYearCHD.
model.fit(X_train, y_train)


# Step 13: Make predictions.
# The model predicts whether the person has CHD risk or not.
y_pred = model.predict(X_test)


# Step 14: Evaluate the model.
# These scores tell us how good the classification model is.
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, zero_division=0)
rec = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)
cm = confusion_matrix(y_test, y_pred)

print("\nModel evaluation:")
print("Accuracy:", acc)
print("Precision:", prec)
print("Recall:", rec)
print("F1 Score:", f1)

print("\nConfusion Matrix:")
print(cm)


# Step 15: Show the model parameters.
# Intercept and coefficients help us understand the fitted model.
print("\nModel parameters:")
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)


# Step 16: Show class prediction counts.
# This helps us see how many 0s and 1s the model predicted.
print("\nPredicted class counts:")
print(pd.Series(y_pred).value_counts())
