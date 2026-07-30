"""
Simple Linear Regression

Task:
Predict Salary using YearsExperience.

Input variable  = YearsExperience
Output variable = Salary
"""

# Step 1: Import the required libraries.
# pandas is used to read and work with the CSV file.
# matplotlib is used for graphs.
# sklearn is used to build and test the machine learning model.

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split




# Step 2: Load the dataset.
# We use the file that is attached with the assignment.
file_path = r"C:\Users\deeks\Desktop\python\python-repo\010-intellbi-classes\Data-Science\Dataset_DS\salary_data.csv"
df = pd.read_csv(file_path)


# Step 3: Check the dataset.
# shape tells us the number of rows and columns.
print("Dataset shape:", df.shape)

# info() shows column names and data types.
print("\nDataset info:")
print(df.info())

# describe() gives basic statistics like count, mean, min, and max.
print("\nDataset description:")
print(df.describe().T)

# head() shows the first few rows of the dataset.
print("\nFirst 5 rows:")
print(df.head())


# Step 4: Check for missing values and duplicate rows.
# This dataset is small, so we quickly verify data quality.
print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())


# Step 5: Basic data analysis.
# Here we plot the relationship between YearsExperience and Salary.
plt.figure(figsize=(6, 4))
plt.scatter(df["YearsExperience"], df["Salary"], color="blue")
plt.title("Salary vs YearsExperience")
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.show()

# Histogram for YearsExperience
plt.subplot(1, 2, 1)
plt.hist(df["YearsExperience"], bins=10, color="blue", edgecolor="black")
plt.title("YearsExperience Distribution")
plt.xlabel("YearsExperience")
plt.ylabel("Count")

# Histogram for Salary
plt.subplot(1, 2, 2)
plt.hist(df["Salary"], bins=10, color="green", edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# Step 5b: Check for outliers in Salary using the IQR method.
# Q1 is the 25th percentile and Q3 is the 75th percentile.
for col in df.columns:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)

# IQR tells us the middle spread of the data.
    iqr = q3 - q1

# Values below the lower bound or above the upper bound are considered outliers.
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    print("\nOutlier detection for Salary:")
    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", iqr)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)

# Find the rows where Salary is outside the bounds.
    outliers = df[(df["Salary"] < lower_bound) | (df["Salary"] > upper_bound)]

    print("\nOutlier rows in Salary:")
    print(outliers)

    print("removing outliers from dataframe")
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    print(df)


print("Dataset shape:", df.shape)

### Encoding not needed as only numeric columns are there.

## Correlation matrix using heatmap

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True)
plt.show()


# ==>ML Model building

# Step 6: Split the data into input and output.
# X contains the independent variable.
# y contains the dependent variable.
X = df[["YearsExperience"]]
y = df["Salary"]


# Step 7: Split the dataset into training and testing parts.
# Training data is used to teach the model.
# Testing data is used to check how well the model works.

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)


# Step 8: Create the model.
# LinearRegression() creates the simple linear regression model.
model = LinearRegression()


# Step 9: Train the model.
# The model learns the relationship between YearsExperience and Salary.
model.fit(X_train, y_train)

## Model parameters: C (intercept), m (coeff)
print("intercept : ",model.intercept_)
print("coeff : ",model.coef_)

# # Step 12: Show the regression equation.
# # This gives the straight-line equation learned by the model.
# print("\nRegression equation:")
# print("Salary = intercept + (coefficient * YearsExperience)")
# print("Intercept:", model.intercept_)
# print("Coefficient:", model.coef_[0])

# Step 10: Make predictions.
# The model predicts salary values for the test data.
y_pred = model.predict(X_test)


# Step 11: Evaluate the model.
# These scores tell us how good the model is.
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel evaluation:")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R2 Score:", r2)


# Step 13: Draw the regression line.

plt.figure(figsize=(6, 4))
plt.scatter(X_train, y_train, color="blue", label="Training data")
plt.plot(X_train, model.predict(X_train), color="red", label="Regression line")
plt.title("Simple Linear Regression")
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.legend()
plt.show()
