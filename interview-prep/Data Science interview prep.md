Interview Questions
Basic

### Q1. What is data?

Answer:
Data is a collection of facts, observations, and measurements that can be processed and analyzed to extract meaningful information.
-----------------------------------------------------------------------------------------------
### Q2. Why is data important in machine learning?

Answer:
Machine learning algorithms learn patterns from historical data. Without data, models cannot identify relationships or make predictions.
-----------------------------------------------------------------------------------------------
### Q3. Difference between data and information?

Example:
Raw data:   100, 120, 130

Information:    Average sales = 116 units

### "Data becomes information after processing."
-----------------------------------------------------------------------------------------------
### Q4. Why is data preprocessing required before training ML models?

Because real-world data contains:

Missing values
Outliers
Duplicate records
Incorrect formats
Noise

Models require clean and meaningful data.
-----------------------------------------------------------------------------------------------
                         DATA
                           |
        ----------------------------------
        |                                |
   Qualitative                      Quantitative
   (Categorical)                    (Numerical)
        |                                |
   -------------                 ----------------
   |           |                 |              |
Nominal     Ordinal          Discrete     Continuous
-----------------------------------------------------------------------------------------------

### Question 1
Data:
Customer age

answer: Structured + Quantitative + Discrete + Feature

-----------------------------------------------------------------------------------------------
### Question 2
Data:
Customer Rating:

1 star
2 stars
3 stars
4 stars
5 stars

Answers:- Structured + Qualitative (Categorical)+ Ordinal Data+ Can be Feature OR Label

----------------------------------------------------------------------------------------------

### Question 3
Data:
Email message:  "Your Amazon order has been shipped"

Answer:- Unstructured Data+Qualitative Data
Used in:

NLP (Natural Language Processing)
Spam detection
Sentiment analysis
Email classification
LLM applications

-----------------------------------------------------------------------------------------------
### What is nominal data?

Answer:
Nominal data is categorical data that contains labels or categories without any natural order or ranking.
----------------------------------------------------------------------------------------------
### Is customer ID nominal data?

Because there is no ranking.
We cannot say:
Customer 1003 > Customer 1001

The number does not represent quantity or order.

It is only a name/tag.
Customer ID is: ✅ Nominal data
because it is only an identifier.

Qualitative
+
Nominal

---------------------------------------------------------------------------------------------
### Difference between nominal and ordinal data?

Answer:
Nominal data contains categories without order, while ordinal data contains categories with meaningful ranking.
-----------------------------------------------------------------------------------------------
### Is salary ordinal data?

No.

Salary is:Quantitative & Continuous
Because it is measurable.
-----------------------------------------------------------------------------------------------
### Difference between Discrete and Continuous?

Discrete = Count
Continuous = Measure
------------------------------------------------------------------------------------------------
### Discrete vs Continuous (Very Important Interview Question)
| Discrete                    | Continuous              |
|-----------------------------|-------------------------|
| Count data                  | Measurement data        |
| Whole numbers               | Decimal values possible |
| Finite values               | Infinite values         |
| Example: Number of students | Example: Height         |
| Example: Number of cars     | Example: Weight         |

-----------------------------------------------------------------------------------------------
### Difference between discrete and continuous data?

Answer:
Discrete data represents countable values with finite possibilities, while continuous data represents measurable values that can take infinite possible values.

------------------------------------------------------------------------------------------------
### Descriptive vs Inferential Statistics

| Descriptive              | Inferential                                |
|--------------------------|--------------------------------------------|
| Summarizes existing data | Predicts about larger population           |
| Uses complete dataset    | Uses sample data                           |
| No prediction            | Makes prediction                           |
| "What happened?"         | "What may happen?"                         |
| Example: Average salary  | Example: Predict average salary of country |

-------------------------------------------------------------------------------------------------

### Statistics vs Machine Learning
>Statistics

Focus:
    -   Understanding data
    -   Finding relationships
    -   Making conclusions

Example:    "What is average customer age?"

>Machine Learning

Focus:
    -    Learning patterns
    -    Making predictions
    -    Automating decisions

Example:    "Will this customer buy?"
They overlap.

Relationship:

        Statistics

            +

        Programming

            +

          Data

            ↓

        Machine Learning

---------------------------------------------------------------------------------------------

### What is statistics?
>   Statistics is the branch of mathematics that deals with collecting, analyzing, interpreting,        and presenting data to extract meaningful insights.   
----------------------------------------------------------------------------------------------

### Why is statistics important in machine learning?
>   Statistics helps understand data patterns, handle uncertainty, detect relationships, identify       outliers, and evaluate ML models.
-----------------------------------------------------------------------------------------------

### Difference between descriptive and inferential statistics?
>   Descriptive statistics summarizes existing data, while inferential statistics uses sample data      to make predictions or conclusions about a population.
----------------------------------------------------------------------------------------------

DESCRIBE = DESCRIPTIVE

PREDICT/INFER = INFERENTIAL

-----------------------------------------------------------------------------------------------

### Is Machine Learning descriptive or inferential statistics?
>   Machine Learning uses both. Descriptive statistics helps understand and summarize data, while     inferential statistics helps make predictions and generalizations from samples.
------------------------------------------------------------------------------------------------

### Why do we use samples instead of populations?
>  Samples reduce cost, time, and resources while allowing us to make conclusions about the 
    population.
------------------------------------------------------------------------------------------------

### What makes a good sample?

>   A good sample should accurately represent the characteristics of the population and should be    selected without bias.
>   Sample quality is important because the machine learning model learns patterns from the          sample. If the sample does not represent the population properly, the model may become biased    and give inaccurate predictions for different groups of patients.

------------------------------------------------------------------------------------------------

Population = Entire group

Sample = Small part of population

-----------------------------------------------------------------------------------------------
### What is sampling?

>   Sampling is the process of selecting a subset of observations from a population to perform       analysis and draw conclusions.
-----------------------------------------------------------------------------------------------
### Difference between stratified and cluster sampling?

>   Stratified sampling selects samples from every subgroup, while cluster sampling selects          complete groups from the population.
----------------------------------------------------------------------------------------------
### Which sampling technique reduces bias?

>   Stratified sampling generally reduces bias because it ensures representation from all
    important groups. 
---------------------------------------------------------------------------------------------
### Probability vs Non-Probability Sampling
| Probability Sampling        | Non-Probability Sampling      |
|-----------------------------|-------------------------------|
| Random selection            | Non-random selection          |
| Equal chance                | Unequal chance                |
| Less bias                   | More bias                     |
| More statistically reliable | Less reliable                 |
| Example: Random sampling    | Example: Convenience sampling |

-------------------------------------------------------------------------------------------
### When Do Data Scientists Use Non-Probability Sampling?
>   when
    -   Data is difficult to collect
    -   Time is limited
    -   Expert opinion is required
-------------------------------------------------------------------------------------------
### What is non-probability sampling?

>   Non-probability sampling is a sampling technique where samples are selected using non-random     methods and each population member does not have a known chance of selection.
-------------------------------------------------------------------------------------------
### Difference between convenience and judgment sampling?

| Convenience                     | Judgment                               |
|---------------------------------|----------------------------------------|
| Select easiest available people | Select based on researcher's expertise |
| Example: Nearby customers       | Example: Expert doctors                |
---------------------------------------------------------------------------------------------
### Which sampling method is used for rare populations?

>   Snowball sampling is commonly used because existing participants help identify additional participants.
----------------------------------------------------------------------------------------------
### What is normal distribution?

>   Normal distribution is a probability distribution where data is symmetrically distributed        around the mean, forming a bell-shaped curve.
-----------------------------------------------------------------------------------------------
### What is the relationship between mean, median, and mode in normal distribution?

>   Mean = Median = Mode
-----------------------------------------------------------------------------------------------
### Explain the 68-95-99.7 rule.

>   In a normal distribution, approximately 68% of data falls within one standard deviation, 95% within two standard deviations, and 99.7% within three standard deviations from the mean
-----------------------------------------------------------------------------------------------
### What is uniform distribution?

>   Uniform distribution is a probability distribution where all possible outcomes have equal probability.
------------------------------------------------------------------------------------------------
### Give an example of uniform distribution.

>   Rolling a fair dice is an example of discrete uniform distribution because every number from 1 to 6 has equal probability.
------------------------------------------------------------------------------------------------
### Difference between normal and uniform distribution?

>   Normal distribution has most values concentrated around the mean, while uniform distribution has equal probability for all values.
------------------------------------------------------------------------------------------------
### Why do we care about distribution in Machine Learning?

Good answer:
Understanding distribution helps Data Scientists select appropriate algorithms, detect outliers, transform features, and improve model performance.
------------------------------------------------------------------------------------------------
### Why Skewness Matters in Machine Learning?
>   Detect Data Problems
>   Choose Data Transformation
>   Improve ML Model Performance
-----------------------------------------------------------------------------------------------
### What is skewness?

>Skewness is a statistical measure that describes the asymmetry of data distribution around its mean
-----------------------------------------------------------------------------------------------
### In positively skewed data, what is the relationship between mean, median, and mode?

> Mean > Median > Mode
-----------------------------------------------------------------------------------------------
### Give an example of positively skewed data.

>   Income distribution is usually positively skewed because most people earn average salaries while a few people earn extremely high salaries.
-----------------------------------------------------------------------------------------------
### Why apply log transformation on highly skewed data?

> Data Scientists apply log transformation to reduce the effect of extreme values, make highly skewed data more normally distributed, improve feature relationships, and help ML models perform better.

----------------------------------------------------------------------------------------------
### Skewness vs Kurtosis (Very Important Interview Question)

| Skewness            | Kurtosis         |
|---------------------|------------------|
| Measures asymmetry  | Measures shape   |
| Left/right movement | Peak and tails   |
| Direction of data   | Extreme values   |
| Positive/negative   | Lepto/Meso/Platy |
=============================================================================================
###     Comparison Table

| Type        | Peak   | Tails  | Outliers |
|-------------|--------|--------|----------|
| Mesokurtic  | Medium | Medium | Normal   |
| Leptokurtic | High   | Heavy  | More     |
| Platykurtic | Low    | Thin   | Less     |
----------------------------------------------------------------------------------------------
### What is kurtosis?

>   Kurtosis is a statistical measure that describes the shape of a distribution by analyzing its peak and tail behavior.
----------------------------------------------------------------------------------------------
### Difference between skewness and kurtosis?

> Skewness measures the asymmetry of data, while kurtosis measures the peak and tail behavior of the distribution.
----------------------------------------------------------------------------------------------
### Which kurtosis indicates more outliers?

>   Leptokurtic distribution because it has heavy tails and more extreme values.
----------------------------------------------------------------------------------------------
### A Data Scientist finds very high kurtosis in a feature.What does it indicate and what action might they take?

>Very high kurtosis indicates that the feature may contain heavy tails and more extreme values (outliers). A Data Scientist should investigate these outliers and may apply techniques like log transformation, outlier treatment, or scaling depending on the business problem.
----------------------------------------------------------------------------------------------
### What is EDA?

>   Exploratory Data Analysis is the process of analyzing datasets using statistical methods and visualization techniques to understand patterns, detect anomalies, handle missing values, and prepare data for machine learning.
-----------------------------------------------------------------------------------------------
###  Why is EDA important before ML modeling?

>   EDA helps understand data quality, identify missing values and outliers, discover relationships between variables, and select appropriate features before training models.
-----------------------------------------------------------------------------------------------
### Difference between EDA and Data Cleaning?

| EDA             | Data Cleaning              |
|-----------------|----------------------------|
| Understand data | Fix data problems          |
| Find patterns   | Remove/fix issues          |
| Visualization   | Missing values, duplicates |
----------------------------------------------------------------------------------------------
### Why can't we directly train an ML model without EDA?"

>   Without EDA, we may train a model with poor-quality data containing missing values, outliers, irrelevant features, and hidden patterns. EDA helps us understand and prepare data before modeling, improving model accuracy and reliability.

----------------------------------------------------------------------------------------------
### What is Univariate Analysis?

>   Univariate analysis is the process of analyzing a single variable to understand its distribution, central tendency, spread, and patterns.
----------------------------------------------------------------------------------------------
### What graphs are used for numerical univariate analysis?

Histogram
Box plot
Density plot
-----------------------------------------------------------------------------------------------
### What graphs are used for numerical univariate analysis?

Answer:

Histogram
Box plot
Density plot
-----------------------------------------------------------------------------------------------
### What graphs are used for categorical univariate analysis?

Answer:

Bar chart
Pie chart
Count plot
-----------------------------------------------------------------------------------------------
### Difference between univariate and bivariate analysis?

| Univariate         | Bivariate          |
|--------------------|--------------------|
| One variable       | Two variables      |
| Finds distribution | Finds relationship |
| Age analysis       | Age vs Salary      |
-----------------------------------------------------------------------------------------------
### Types of Univariate Analysis
============================

There are two major types:

                     Univariate Analysis
                             |
              --------------------------------
              |                              |
         Numerical Data              Categorical Data
------------------------------------------------------------------------------------------------
### Numeric Univariate Analysis
Column :- Salary
What will we check?

Mean
Median
Mode
Range
Variance
Standard deviation
IQR
Distribution
        Normal distribution
        Skewness
        Kurtosis
Outliers
Visualization:
            Histogram
            Box plot
------------------------------------------------------------------------------------------
### Categorical univariate analysis
Categorical Univariate Analysis

We check:

Frequency
Percentage
Visualization:- Bar and pie chart
------------------------------------------------------------------------------------------
### What is Bivariate Analysis?

>   Bivariate analysis is the process of analyzing the relationship between two variables to identify patterns, dependencies, and correlations.
------------------------------------------------------------------------------------------
### Which plot is used for numerical vs numerical data?

Answer:
Scatter plot.

Example:
Experience vs Salary.
-------------------------------------------------------------------------------------------
### Which plot is used for numerical vs categorical data?

Answer:
Box plot.

Example:
Salary distribution across departments.
-------------------------------------------------------------------------------------------
### Why is bivariate analysis important before ML?

>   It helps identify relationships between features, understand the target variable, detect useful features, and improve model performance.
-------------------------------------------------------------------------------------------
###  Explain complete process of performing bivariate analysis in real ML project.

>   In a real ML project, I perform bivariate analysis to understand the relationship between two variables. First, I identify the type of variables involved, such as numerical or categorical. Then I use appropriate statistical methods and visualizations like scatter plots, box plots, and bar charts. I analyze correlation between numerical variables, identify important features, understand the relationship with the target variable, and use these insights for feature selection before model building

----------------------------------------------------------------------------------------------
###  Example of bivariate analysis
-   Area vs Price
Type:   Numerical vs Numerical
Graph:  Scatter Plot

-   Location vs Price
Type:   Categorical vs Numerical
Graph:  Box Plot

-   Bedrooms vs Price
Type:   Numerical vs Numerical
Graph:  Scatter Plot
--------------------------------------------------------------------------------------------
###     Important Memory Shortcut

| Variables                 | Example              | Visualization |
|---------------------------|----------------------|---------------|
| Numerical + Numerical     | Age vs Salary        | Scatter Plot  |
| Numerical + Categorical   | Salary vs Department | Box Plot      |
| Categorical + Categorical | Gender vs Purchase   | Bar Chart     |

---------------------------------------------------------------------------------------------
###     What is correlation?

>   Correlation is a statistical measure that shows the strength and direction of the relationship between two variables.
---------------------------------------------------------------------------------------------
###     What is the range of correlation coefficient?

>   The correlation coefficient ranges from -1 to +1.
--------------------------------------------------------------------------------------------
###     Does correlation mean causation?

>   No. Correlation only indicates a relationship between variables, not that one variable causes another.
---------------------------------------------------------------------------------------------
###     Why do we use correlation in ML?

>   We use correlation for feature selection, detecting redundant features, handling multicollinearity, and improving model performance.
----------------------------------------------------------------------------------------------
###     Why should we not blindly remove features with high correlation?

>   We should not blindly remove highly correlated features because correlation only shows the relationship between variables, not their importance. Two highly correlated features may both provide useful information depending on the business problem and model type. We should analyze feature importance, domain knowledge, and multicollinearity before removing any feature.

-----------------------------------------------------------------------------------------------

Raw Data
   |
   ↓
Data Understanding
   |
   ↓
Data Cleaning
   |
   ↓
Univariate Analysis
   |
   ↓
Bivariate Analysis
   |
   ↓
Correlation Analysis
   |
   ↓
Feature Selection
   |
   ↓
ML Model
-----------------------------------------------------------------------------------------
###     What is Matplotlib?

>   Matplotlib is a Python visualization library used to create graphs and charts for data analysis and visualization.
------------------------------------------------------------------------------------------
###     Why do Data Scientists use visualization?

>   Visualization helps identify patterns, trends, relationships, outliers, and communicate insights effectively.
------------------------------------------------------------------------------------------
###     Difference between Histogram and Bar Chart?

Histogram	            Bar Chart
----------------------------------------
Numerical data	        Categorical data
Shows distribution	    Shows comparison
Continuous values	    Categories

Example:    Histogram:  Age distribution

Bar:    Department count

------------------------------------------------------------------------------------------
### Which graph is used for correlation analysis?

>   Scatter plot is used to visualize relationships between two numerical variables.
------------------------------------------------------------------------------------------
###     Explain how visualization helps a Data Scientist during EDA.

>   Visualization helps Data Scientists understand patterns, trends, relationships, distributions,
     and outliers in data. It makes complex data easier to interpret and helps in making better 
    decisions during data cleaning, feature selection, and model building
------------------------------------------------------------------------------------------
### Important Visualization Shortcut

| Data Problem                               | Best Graph   |
|--------------------------------------------|--------------|
| Trend over time                            | Line Chart   |
| Compare categories                         | Bar Chart    |
| Distribution of numerical data             | Histogram    |
| Relationship between 2 numerical variables | Scatter Plot |
| Detect outliers                            | Box Plot     |

------------------------------------------------------------------------------------------
### What is Multivariate Analysis?

>   Multivariate analysis is a statistical technique used to analyze relationships among three or more variables simultaneously to identify patterns, dependencies, and relationships.
------------------------------------------------------------------------------------------
### Difference between Bivariate and Multivariate Analysis?

>   Bivariate analysis studies the relationship between two variables, whereas multivariate analysis studies relationships among multiple variables simultaneously.
-------------------------------------------------------------------------------------------
### Why is multivariate analysis important in Machine Learning?

>   Real-world predictions depend on multiple factors. Multivariate analysis helps understand feature interactions, select important features, and improve model performance
--------------------------------------------------------------------------------------------
### Give an example of multivariate analysis.

>   In house price prediction, we analyze area, location, number of bedrooms, and age together to understand their combined impact on price.
--------------------------------------------------------------------------------------------
### Explain where multivariate analysis fits in ML workflow

>   Multivariate analysis is performed during the EDA phase after univariate and bivariate analysis. It helps analyze relationships among multiple features, identify feature interactions, understand patterns, select important features, and prepare data before building a machine learning model
----------------------------------------------------------------------------------------------

### What is descriptive statistics?

>   Descriptive statistics summarizes and describes the main characteristics of a dataset using measures like mean, median, mode, range, variance, and standard deviation.
----------------------------------------------------------------------------------------------
### Difference between mean and median?

>   Mean calculates the average of all values, while median represents the middle value after sorting. Median is preferred when data contains outliers.
----------------------------------------------------------------------------------------------
### Why is median preferred over mean for salary data?

>   Salary data often contains extreme values such as CEO salaries, which can significantly affect the mean. Median provides a better representation of typical salary.
----------------------------------------------------------------------------------------------
### When do we use mode?

>   Mode is used to find the most frequently occurring value and is commonly used for categorical data and missing value replacement.
-----------------------------------------------------------------------------------------------
###             Mean vs Median vs Mode

| Measure | Meaning             | Best Used For                     |
|---------|---------------------|-----------------------------------|
| Mean    | Average value       | Normally distributed data         |
| Median  | Middle value        | Data with outliers/skewed data    |
| Mode    | Most frequent value | Categorical data & Numerical data |

>   If data is normal:
        Use:    Mean

>   If data has outliers:
        Use:    Median

>   For categorical data:
        Use:    Mode
-----------------------------------------------------------------------------------------
###             Dataset
                   |
                   ↓
        Is data numerical?
              /       \
            Yes        No
            |          |
            ↓          ↓
    Check distribution  Mode
            |
     ----------------
     |              |
 Normal        Outliers/Skewed
     |              |
   Mean          Median
---------------------------------------------------------------------------------------
### Why do we need to handle missing values?

>   Missing values can reduce data quality, introduce bias, and negatively impact machine learning model performance.
---------------------------------------------------------------------------------------
### When would you use median instead of mean?

>   We use median when numerical data contains outliers or is skewed because median is less affected by extreme values.
---------------------------------------------------------------------------------------
### Why is mode used for categorical variables?

>   Categorical variables represent categories, and mode gives the most frequently occurring category, making it suitable for replacement.
----------------------------------------------------------------------------------------
### Can we always replace missing values?

>   No. The replacement method depends on the data type, distribution, percentage of missing values, and business context.
-----------------------------------------------------------------------------------------
###  Industry decision flow

Missing Value
      |
      ↓
What type of data?
      |
 ---------------------
 |                   |
Numeric          Categorical
 |
 ↓
Check distribution
 |
 -----------------
 |               |
Normal       Outliers
 |               |
Mean        Median


Categorical
 |
Mode

-------------------------------------------------------------------------------------------
###     What are measures of spread?

>   Measures of spread describe how much data values vary or scatter around the central tendency. Common measures include range, IQR, variance, and standard deviation.
------------------------------------------------------------------------------------------
###     What is range?

>   Range is the difference between the maximum and minimum values in a dataset.
Formula:

Range = Max - Min
-------------------------------------------------------------------------------------------
###     What is the limitation of range?

>   Range considers only the minimum and maximum values and is highly affected by outliers.
-------------------------------------------------------------------------------------------
###     Two datasets have the same mean but different spread. What does it mean?

>   It means both datasets have the same average value but different variability or distribution patterns.
-------------------------------------------------------------------------------------------
###     What is IQR?

>   IQR is a measure of spread that represents the range of the middle 50% of data values. It is calculated as Q3 minus Q1.
-------------------------------------------------------------------------------------------
###  Why is IQR preferred over Range?

>   IQR is preferred because it is less affected by outliers and focuses on the central portion of the dataset.
------------------------------------------------------------------------------------------
###  What are quartiles?

>   Quartiles divide sorted data into four equal parts. Q1 represents the 25th percentile, Q2 represents the median, and Q3 represents the 75th percentile.
--------------------------------------------------------------------------------------------
### How is IQR used for outlier detection?

>   Values below Q1 - 1.5×IQR or above Q3 + 1.5×IQR are considered outliers.
--------------------------------------------------------------------------------------------
### IQR memory trick

Q1 = 25%
Q2 = 50% = Median
Q3 = 75%

IQR = Q3 - Q1

Outlier:

Below:
Q1 - 1.5×IQR

Above:
Q3 + 1.5×IQR
----------------------------------------------------------------------------------------------------
###    What is variance?

>   Answer: Variance is a statistical measure that represents how much data points 
    are spread around the mean.
----------------------------------------------------------------------------------------------------
###    Why do we square the difference in variance calculation?

>   Answer: We square differences to remove negative values and give more importance to larger 
            deviations.
---------------------------------------------------------------------------------------------------
###    What happens to variance when outliers are present?

>   Answer: Variance increases because outliers create large deviations from the mean.
---------------------------------------------------------------------------------------------------
###    Can two datasets have the same mean but different variance?

>   Answer: Yes. Mean only represents the center of data, while variance represents the spread 
            around the mean.
--------------------------------------------------------------------------------------------------
###    Why is variance sensitive to outliers?
>   Variance squares the distance between each value and the mean. Since outliers have a very large    distance, squaring makes their impact extremely large.
--------------------------------------------------------------------------------------------------
###     Difference between Range and Variance
>   Range measures the total spread between minimum and maximum values, whereas variance measures   how much each data point deviates from the mean.

| Range                                        | Variance                           |
|----------------------------------------------|------------------------------------|
| Difference between maximum and minimum value | Average squared distance from mean |
| Uses only two values                         | Uses all values                    |
| Less mathematical                            | More statistically meaningful      |
| Affected by extreme values                   | Highly affected by outliers        |
| Unit remains same                            | Unit becomes squared               |

-----------------------------------------------------------------------------------------------

### Important Memory Trick 🧠

Remember:

>   Range:
Only looks at:
Minimum + Maximum

>Variance:
Looks at:
Every value + Mean
-------------------------------------------------------------------------------------------------
### Standard Deviation
>   Definition:
        Standard deviation measures how much individual data points are spread around the mean, using the same unit as the original data.

>   Simple words:
        It tells the average distance of data points from the mean.
--------------------------------------------------------------------------------------------------
###     Relationship Between Variance and Standard Deviation

>   Standard deviation is simply the square root of variance.
Formula:

Standard Deviation  = √ Variance
SD=     √25 =   5

or

Variance    =   (Standard Deviation)^2

| Variance                            | Standard Deviation            |
|-------------------------------------|-------------------------------|
| Average squared deviation from mean | Square root of variance       |
| Unit becomes squared                | Same unit as original data    |
| Harder to interpret                 | Easier to interpret           |
| Used in mathematical calculations   | Used for understanding spread |
| Sensitive to outliers               | Sensitive to outliers         |

----------------------------------------------------------------------------------------------------

### What is Standard Deviation?

>   Answer: Standard deviation is a measure of spread that indicates how far data points are from the mean. It is the square root of variance.
-----------------------------------------------------------------------------------------------------
### Why do we use Standard Deviation instead of Variance?

>   Answer: Standard deviation is preferred because it is expressed in the same unit as the original data, making it easier to interpret.
-----------------------------------------------------------------------------------------------------
### What happens to standard deviation when data points are more spread out?

>   Answer: Standard deviation increases because data points have larger deviations from the mean.
-----------------------------------------------------------------------------------------------------
### Can standard deviation be zero?

>   Answer: Yes. If all values in a dataset are identical, standard deviation is zero because there is no variation.

>   Example:    5,5,5,5,5
-----------------------------------------------------------------------------------------------------
### Why is standard deviation more interpretable than variance?

>   Interview-ready answer: Standard deviation is easier to interpret because it is expressed in the same unit as the original data, whereas variance is expressed in squared units.
----------------------------------------------------------------------------------------------------
### Relationship between Variance and Standard Deviation.

>Interview answer:  Standard deviation is the square root of variance. Variance represents squared deviations from the mean, while standard deviation converts it back into the original measurement unit.
----------------------------------------------------------------------------------------------------
### ### Important Concept Summary 🧠

>Remember this:
Mean
 |
 |  (Where is the center?)
 ↓

>Variance
 |
 |  (How much spread? But squared unit)
 ↓

>Standard Deviation
 |
 |  (How much spread? Same unit)
 ↓

--------------------------------------------------------------------------------------------------
###     Variance vs Standard Deviation Quick Memory

| Concept            | Question it answers                     |
|--------------------|-----------------------------------------|
| Mean               | Where is the center?                    |
| Range              | How far are minimum and maximum?        |
| IQR                | How spread is the middle 50%?           |
| Variance           | How much is data spread from mean?      |
| Standard Deviation | What is the average distance from mean? |

###     Main Difference
| Variance                                           | Standard Deviation                    |
|----------------------------------------------------|---------------------------------------|
| Square of standard deviation                       | Square root of variance               |
| Measures spread using squared units                | Measures spread using original units  |
| Harder to interpret                                | Easier to interpret                   |
| Used more in mathematical/statistical calculations | Used more for practical understanding |
| More sensitive to large deviations                 | Also sensitive to outliers            |
| Symbol: σ²                                         | Symbol: σ                             |

---------------------------------------------------------------------------------------------------
### Relationship Between Variance and Standard Deviation

          Square
Standard Deviation  ─────────→  Variance


          Square Root
Standard Deviation  ←─────────  Variance

---------------------------------------------------------------------------------------------------
###     What is the relationship between variance and standard deviation?

>   Answer: Standard deviation is the square root of variance. Variance is the squared measure of deviation from the mean.
---------------------------------------------------------------------------------------------------
###     Why is standard deviation preferred over variance?

>   Answer: Standard deviation is preferred because it is expressed in the same unit as the original data, making interpretation easier.
---------------------------------------------------------------------------------------------------
###     Which is more affected by outliers?

>   Answer:Both variance and standard deviation are affected by outliers because both depend on squared deviations from the mean.
--------------------------------------------------------------------------------------------------
###     Difference Between Population and Sample Variance

| Population Variance             | Sample Variance                 |
|---------------------------------|---------------------------------|
| Uses complete data              | Uses subset of data             |
| Denominator = N                 | Denominator = n-1               |
| Mean = population mean          | Mean = sample mean              |
| Used when all data is available | Used when estimating population |
| Symbol σ²                       | Symbol s²                       |

-------------------------------------------------------------------------------------------------
###     What is the difference between population variance and sample variance?

>Answer:    Population variance calculates variance using the complete population and divides by N, whereas sample variance estimates population variance from a sample and divides by N-1.
-------------------------------------------------------------------------------------------------
###     Why do we use N-1 instead of N in sample variance?

>   Answer: Because sample variance tends to underestimate population variance. Dividing by N-1 corrects this bias. This is called Bessel's correction.
--------------------------------------------------------------------------------------------------
###     When do we use population variance?

>   Answer: When we have complete information about the entire population.
--------------------------------------------------------------------------------------------------
###  When do we use sample variance?

>   Answer: When we only have a subset of data and want to estimate population behavior.
--------------------------------------------------------------------------------------------------
###  Which variance is usually used in Data Science?

>   Answer:Sample variance is commonly used because real-world datasets usually represent samples of a larger population.
--------------------------------------------------------------------------------------------------
###     Why is sample variance usually greater than population variance?

>   Interview answer:   Sample variance is usually greater because dividing by n-1 instead of n compensates for the fact that samples generally underestimate the true population variation.
--------------------------------------------------------------------------------------------------
###     Explain N vs N-1.

>   interview-ready: In population variance, we divide by N because we have complete population data. In sample variance, we divide by n-1 because the sample is used to estimate the population, and n-1 corrects the bias caused by using sample data.
-------------------------------------------------------------------------------------------------