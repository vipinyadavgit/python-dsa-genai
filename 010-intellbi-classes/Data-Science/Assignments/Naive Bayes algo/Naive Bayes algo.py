"""
Naive Bayes Algorithm

Task:
Predict whether an adult earns >50K or <=50K.

Output variable:
income
<=50K or >50K
"""

# Step 1: Import the required libraries.
# pandas is used to read and work with the CSV file.
# matplotlib and seaborn are used for graphs.
# LabelEncoder is used to convert text columns into numbers.
# GaussianNB is the Naive Bayes model we need to use.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder


# Step 2: Load the dataset.
# The file has ? in some places, so we treat those as missing values.
file_path = r"C:\Users\deeks\Desktop\python\python-repo\010-intellbi-classes\Data-Science\Dataset_DS\Humans dataset.csv"
df = pd.read_csv(file_path, na_values=["?", "NA"])


# Step 3: Check the dataset.
# shape tells us the number of rows and columns.
print("Dataset shape:", df.shape)

# info() shows column names and data types.
print("\nDataset info:")
print(df.info())

# describe() gives basic statistics for numerical columns.
print("\nDataset description:")
print(df.describe())

# head() shows the first few rows of the dataset.
print("\nFirst 5 rows:")
print(df.head())


# Step 4: Check for missing values and duplicate rows.
# This helps us understand the quality of the data.
print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())


# Step 5: Split the dataset into categorical and numerical columns.
# Categorical columns contain text values.
# Numerical columns contain numbers.
cat_cols = df.select_dtypes(include="object").columns
num_cols = df.select_dtypes(exclude="object").columns
cat_feature_cols = [col for col in cat_cols if col != "income"]

print("\nCategorical columns:", list(cat_cols))
print("Numerical columns:", list(num_cols))


# Step 6: Handle missing values.
# For numerical columns, we fill missing values with the median.
# For categorical columns, we fill missing values with the mode.
for column in num_cols:
    if column != "income":
        df[column] = df[column].fillna(df[column].median())

for column in cat_cols:
    df[column] = df[column].fillna(df[column].mode()[0])


# Step 7: Remove duplicate rows.
# Duplicate rows do not add value to the model.
df = df.drop_duplicates()
print("\nShape after removing duplicates:", df.shape)


# Step 8: Handle outliers using the IQR method.
# We calculate outlier bounds only for numerical feature columns.
num_feature_cols = [col for col in num_cols if col != "income"]
q1 = df[num_feature_cols].quantile(0.25)
q3 = df[num_feature_cols].quantile(0.75)
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

# Remove rows that are outside the IQR range in any numerical feature column.
for column in num_feature_cols:
    df = df[(df[column] >= lower_bound[column]) & (df[column] <= upper_bound[column])]

print("\nShape after outlier removal:", df.shape)


# Step 9: Convert categorical columns into numerical columns.
# GaussianNB can work only with numbers, so we encode text columns.
encoders = {}

for column in cat_cols:
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    encoders[column] = encoder


# Step 10: Univariate analysis.
# Count plot shows how many people are in each income class.
plt.figure(figsize=(6, 4))
sns.countplot(x="income", data=df)
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Count")
plt.show()


# Step 11: Bivariate analysis.
# Heatmap shows the correlation between numerical columns.
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(numeric_only=True), cmap="YlGnBu", annot=False)
plt.title("Correlation Heatmap")
plt.show()


# Step 12: Split the data into input and output.
# X contains all the input variables.
# y contains the output variable.
X = df.drop("income", axis=1)
y = df["income"]


# Step 13: Split the dataset into training and testing parts.
# Training data is used to teach the model.
# Testing data is used to check how well the model works.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y )

#   stratify=y → Ensures the class distribution in train and test sets is similar to the original dataset.
#   This is especially important for classification problems with imbalanced classes.

# Step 14: Create the model.
# GaussianNB() creates the Naive Bayes classifier.
model = GaussianNB()


# Step 15: Train the model.
# The model learns the pattern between input variables and income class.
model.fit(X_train, y_train)


# Step 16: Make predictions.
# The model predicts whether each person earns <=50K or >50K.
y_pred = model.predict(X_test)


# Step 17: Evaluate the model.
# These are classification metrics.
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\nModel evaluation:")
print("Accuracy:", round(acc, 4))
print("Precision:", round(prec, 4))
print("Recall:", round(rec, 4))
print("F1 Score:", round(f1, 4))

print("\nConfusion Matrix:")
print(cm)


# Step 18: Show the model parameters.
# These values help us understand the trained model.
print("\nModel class counts:")
print(model.class_count_)

print("\nModel class prior probabilities:")
print(model.class_prior_)


# Step 19: Predict one new record.
# Here we give one valid example row, encode it the same way as training data, and ask the model to predict the income class.
new_record = {
    "age": 39,
    "workclass": "Private",
    "fnlwgt": 77516,
    "education": "Bachelors",
    "education.num": 13,
    "marital.status": "Never-married",
    "occupation": "Adm-clerical",
    "relationship": "Not-in-family",
    "race": "White",
    "gender": "Male",
    "capital.gain": 0,
    "capital.loss": 0,
    "hours.per.week": 40,
    "native.country": "United-States",
}

# Convert the new record into a one-row DataFrame so it matches the model input format.
new_record_df = pd.DataFrame([new_record])

# Apply the same label encoding used during training.
for column in cat_feature_cols:
    new_record_df[column] = encoders[column].transform(new_record_df[column])

# Reorder the columns to match the training data.
new_record_df = new_record_df[X.columns]

# Predict the income class for the new record.
new_prediction = model.predict(new_record_df)[0]

# Convert the numeric result back to the original label.
predicted_label = encoders["income"].inverse_transform([new_prediction])[0]

print("\nPrediction for one new record:")
print("Predicted income class:", predicted_label)
