--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
### End-to-End EDA Workflow (Based on Completed Topics)
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
                
                Raw Dataset
                     |
                     ↓
          1. Understand Business Problem
                     |
                     ↓
          2. Data Understanding
                     |
                     ↓
          3. Data Quality Check
                     |
                     ↓
          4. Data Cleaning
                     |
                     ↓
          5. Univariate Analysis
                     |
                     ↓
          6. Bivariate Analysis
                     |
                     ↓
          7. Multivariate Analysis
                     |
                     ↓
          8. Statistical Analysis
                     |
                     ↓
          9. Feature Understanding
                     |
                     ↓
          10. Prepare Data for ML

-----------------------------------------------------------------------------------------
Step 1: Understand Business Problem

Before touching data, understand:

Questions:
What problem are we solving?
What is the target variable?
What are features?

Example:

Customer churn prediction:

Goal:

Predict whether customer will leave company.

Target:

Churn

Features:

Age
Monthly Bill
Contract Type
Usage
Location
------------------------------------------------------------
Step 2: Data Understanding

First look at the dataset.

Check:

1. Number of rows and columns
Example:

10000 rows
15 columns

Meaning:

Rows = observations
Columns = features
--------------
2. Identify Data Types

Classify columns:

Numerical

Example:

Age
Salary
Experience

Further:

Discrete:

Number of children
Number of products

Continuous:

Height
Weight
Salary
Categorical

Example:

Gender
City
Department

Further:

Nominal:

City
Gender

Ordinal:

Education Level
Rating
----------------------------------------------------------
Step 3: Data Quality Check

Now check data problems.

1. Missing Values

Questions:

How many missing values?
Which columns have missing values?

Decision:

Numerical
    |
    |
Distribution check
    |
 ----------------
 |              |
Normal      Outliers
 |              |
Mean       Median


Categorical
 |
Mode

2. Duplicate Values

Check:

Example:

Same customer repeated twice.

Problem:

Can create bias.

3. Wrong Values

Example:

Age:

25
30
35
250

250 is suspicious.

4. Outlier Detection

Use:

IQR method

Formula:

Lower Limit:

Q1 - 1.5 × IQR


Upper Limit:

Q3 + 1.5 × IQR
Step 4: Data Cleaning

After identifying issues:

Perform:

Missing value treatment

Example:

Salary:

Use:

Mean
Median
Mode
Remove duplicates
Handle outliers

Options:

Remove
Replace
Transform
Keep if meaningful

Example:

Salary:

CEO salary = 5 crore

Do not blindly remove.

Business context matters.

-------------------------------------------------------------------------
Step 5: Univariate Analysis

Now analyze one feature at a time.

A) Numerical Univariate Analysis

Example:

Age:

Questions:

Average age?
Distribution?
Spread?
Outliers?

Check:

Central Tendency

Mean

Median

Mode

Distribution

Check:

Normal distribution
Skewness
Spread

Check:

Range
IQR

Example:

Salary:

Find:

Mean salary

Median salary

Minimum salary

Maximum salary
B) Categorical Univariate Analysis

Example:

Department:

IT
HR
Finance

Questions:

Which category is highest?
How many records per category?

Use:

Frequency count

Mode

Visualization:

Bar chart

Step 6: Bivariate Analysis

Now analyze relationship between TWO variables.

Case 1:

Numerical vs Numerical

Example:

Experience
Salary

Goal:

Find relationship.

Use:

Scatter plot
Correlation

Question:

Does salary increase with experience?

Case 2:

Categorical vs Numerical

Example:

Department
Salary

Question:

Which department has higher salary?

Use:

Box plot
Group comparison
Case 3:

Categorical vs Categorical

Example:

Gender
Purchase Decision

Question:

Does gender influence purchase?

Use:

Bar chart
Count analysis
Step 7: Multivariate Analysis

Now analyze 3 or more variables.

Example:

Salary prediction:

Experience
+
Education
+
Age
+
Location

          ↓

       Salary

Questions:

Which features impact target?
Are features interacting?
Which features are important?

Common techniques:

Pair analysis
Correlation matrix
Heatmap
Step 8: Statistical Analysis

Now summarize the dataset.

Descriptive Statistics

Find:

Central Tendency
Mean
Median
Mode
Spread
Range
IQR
Variance
Standard Deviation (later)
Distribution Understanding

Check:

Normal distribution
Uniform distribution
Skewness
Kurtosis
Step 9: Feature Understanding

Before ML:

Ask:

Which features are useful?

Example:

Customer prediction:

Useful:

Age
Income
Usage
Contract

Not useful:

Customer_ID
Serial_Number
Step 10: Prepare Data for ML

Final steps:

Clean Data

        ↓

Handle Missing Values

        ↓

Handle Outliers

        ↓

Encode Categorical Data

        ↓

Feature Engineering

        ↓

Train ML Model
Complete EDA Checklist (Practice Template)

Whenever you take a dataset, follow this:

----------------------------------------------------------------------------------
------------------------------------------------------------------------------------
1. Understand Business Problem

2. Dataset Overview
   |
   |- Shape
   |- Columns
   |- Data Types


3. Data Quality
   |
   |- Missing Values
   |- Duplicate Values
   |- Wrong Values
   |- Outliers


4. Data Classification
   |
   |- Numerical
   |- Categorical
   |- Discrete
   |- Continuous
   |- Nominal
   |- Ordinal


5. Univariate Analysis
   |
   |- Mean
   |- Median
   |- Mode
   |- Distribution
   |- Skewness
   |- IQR


6. Bivariate Analysis
   |
   |- Numerical vs Numerical
   |- Numerical vs Categorical
   |- Categorical vs Categorical


7. Multivariate Analysis


8. Insights
   |
   |- Important Patterns
   |- Important Features


9. ML Preparation
_______________________________________________________________________________________
---------------------------------------------------------------------------------------

                         RAW DATASET
                              |
                              ↓
┌─────────────────────────────────────────┐
│ STEP 1: BUSINESS UNDERSTANDING          │
└─────────────────────────────────────────┘
                              |
                              ↓
        ┌──────────────────────────────┐
        │ Define Problem               │
        │                              │
        │ - What is the objective?     │
        │ - Prediction or Analysis?    │
        │ - Who will use result?       │
        └──────────────────────────────┘
                              |
                              ↓

Example:
Customer Churn Prediction

Target Variable:
        ↓
     Churn

Features:
        ↓
Age, Salary, Contract, Usage


                              |
                              ↓

>STEP 2: DATA UNDERSTANDING

                 DATASET
                    |
                    ↓
        ┌────────────────────┐
        │ Dataset Overview   │
        └────────────────────┘
                    |
        -------------------------
        |                       |
        ↓                       ↓

Check Shape              Check Columns

Rows                     Feature names
Columns                  Target column

        |
        ↓

Check Data Types

        |
        |
 -----------------------------
 |             |              |
Numerical   Categorical    Date
 |
 |
 -----------------------
 |                     |
Discrete          Continuous


Categorical:

 |
 ----------------
 |              |
Nominal      Ordinal

>   STEP 3: DATA QUALITY CHECK
 
                 DATA QUALITY CHECK
                         |
        ---------------------------------
        |               |               |
        ↓               ↓               ↓

 Missing Values    Duplicate Values   Wrong Values
        |               |               |
        ↓               ↓               ↓

How many?        Remove duplicates   Example:

Which column?                         Age = 250

Percentage?

>STEP 4: MISSING VALUE HANDLING
                    Missing Values
                       |
                       ↓
              Identify Data Type
                       |
          -------------------------
          |                       |
          ↓                       ↓
      Numerical             Categorical
          |                       |
          ↓                       ↓
Check Distribution            Mode Replacement
          |
     ----------------
     |              |
     ↓              ↓
 Normal        Outliers/Skewed
     |              |
     ↓              ↓
 Mean          Median

==>   STEP 5: OUTLIER DETECTION
                  Numerical Features
                      |
                      ↓
              Check Outliers
                      |
                      ↓
                 Use IQR Method
                      |
                      ↓

Calculate:
Q1
Q3

IQR = Q3-Q1
                      |
                      ↓

Lower Limit:
Q1 - 1.5*IQR

Upper Limit:
Q3 + 1.5*IQR
                      |
                      ↓

Outside Range?
        |
   -------------
   |           |
 Yes          No
Outlier     Normal

>   STEP 6: UNIVARIATE ANALYSIS

              One Feature Analysis
                       |
          -------------------------
          |                       |
          ↓                       ↓
 Numerical Feature          Categorical Feature
          |                       |
          ↓                       ↓
Mean                      Frequency Count
Median                   Mode
Range
IQR
          |
          ↓
Distribution Check
          |
 -------------------
 |                 |
Normal          Skewed

>   Check:
Average salary?
Median salary?
Outliers?
Distribution?

STEP 7: BIVARIATE ANALYSIS (Goal:Find relationship between two variables.)
                 Two Features
                       |
        --------------------------------
        |              |              |
        ↓              ↓              ↓
    Numeric        Numeric vs        Category
    vs             Category          vs Category
    Numeric
        |              |              |
        ↓              ↓              ↓
Scatter Plot    Box Plot       Bar Chart
        |
        ↓
Correlation

>   STEP 8: MULTIVARIATE ANALYSIS
        Goal:   Understand multiple features together.
    
Multiple Features
            |
            ↓
        Experience
             +
        Education
             +
        Age
             |
             ↓
          Salary

>Check:
Which features influence target?
Which features are important?
Are features related?


> STEP 9: STATISTICAL SUMMARY

              Statistical Analysis
                      |
        --------------------------------
        |                              |
        ↓                              ↓
Central Tendency              Spread


Mean                         Range

Median                       IQR

Mode                         Variance (Later)

                              Standard Deviation
                              (Later)


STEP 10: DISTRIBUTION ANALYSIS
             
            Data Distribution
                    |
                    ↓
        -----------------------
        |                     |
        ↓                     ↓
Normal Distribution      Skewness
                          |
                 -----------------
                 |               |
                 ↓               ↓
          Positive Skew    Negative Skew

>   Check:
Data balance
Tail behaviour
Outliers


STEP 11: FEATURE INSIGHTS
              
            Feature Analysis
                     |
                     ↓
Which features are useful?
                     |
        --------------------------
        |                        |
        ↓                        ↓
Important Features        Remove Features


Example:

Experience              Customer_ID
Salary                  Random_Number
Age


STEP 12: FINAL EDA REPORT
    
    EDA REPORT

1. Dataset Summary

2. Data Quality Issues Found

3. Missing Value Treatment

4. Outlier Analysis

5. Important Features

6. Data Distribution

7. Relationships Found

8. Business Insights

9. ML Preparation Recommendation


-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
>   Complete EDA Master Flow (One Page)
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------

START
  |
  ↓

Understand Business Problem

  |
  ↓

Load Dataset

  |
  ↓

Dataset Overview
(shape, columns, datatype)

  |
  ↓

Data Quality Check

  |
  |
 -------------------------
 |          |             |
Missing   Duplicate    Wrong Data

  |
  ↓

Clean Data

  |
  ↓

Outlier Detection
(IQR)

  |
  ↓

Univariate Analysis

  |
  ↓

Bivariate Analysis

  |
  ↓

Multivariate Analysis

  |
  ↓

Statistics Summary

  |
  ↓

Feature Analysis

  |
  ↓

Insights

  |
  ↓

ML Ready Dataset

END

>   Practice Rule For You

1. Understand Problem
2. Identify Target
3. Identify Features
4. Classify Data Types
5. Check Missing Values
6. Handle Missing Values
7. Check Duplicates
8. Detect Outliers
9. Perform Univariate Analysis
10. Perform Bivariate Analysis
11. Perform Multivariate Analysis
12. Extract Insights
13. Prepare for ML


