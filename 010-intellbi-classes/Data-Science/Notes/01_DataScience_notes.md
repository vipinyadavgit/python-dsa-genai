### What is data?
Answer:
Data is a collection of facts, observations, and measurements that can be processed and analyzed to extract meaningful information.
-----------------------------------------------------------------------------------------------

### Data Science lifecycle:
              DATA
                |
                ↓
        Data Collection
                |
                ↓
        Data Cleaning
                |
                ↓
          Data Analysis
                |
                ↓
        Feature Engineering
                |
                ↓
       Machine Learning Model
                |
                ↓
           Prediction
-----------------------------------------------------------------------------------------
### Example:

Netflix:

Raw Data:

User:
- Age
- Location
- Watch history
- Likes
- Search history

↓

AI Model

↓

Recommendation:

"Because you watched X, you may like Y"
------------------------------------------------------------------------------------------
### Type of Data

                 DATA
                   |
        ----------------------
        |                    |
   Qualitative          Quantitative
   (Categorical)        (Numerical)
        |                    |
   -----------          -------------
   |         |          |           |
Nominal   Ordinal   Discrete   Continuous

-------------------------------------------------------------------------------------------
### Data in Machine Learning

In ML, data is usually divided into:

### Input Data (Features) Also called:
Independent variables
X variables

Example:
Predict house price:

Input:Area,Bedrooms,Location,Age of house
        ↓
ML Model

### Output Data (Target)Also called:
Label
Dependent variable
Y variable

Example:
Input:
Area = 2000 sq ft
Bedrooms = 3
----------------------------------------------------------------------------------------------
### Structured vs Unstructured Data

This is very important for AI Engineers.

### Structured Data:-   Data stored in rows and columns.
Example:- 
ID | Name | Age | Salary
------------------------
1  | Amit | 30  | 80000

Used in: Data Science,Machine Learning, Analytics

### Unstructured Data

No fixed format.
Example:- Images, Customer reviews,Emails,Documents,Voice recordings, YouTube videos.

Used heavily in: Computer Vision,NLP,Generative AI

------------------------------------------------------------------------------------------
###     Why Data Quality Matters?

"Garbage In, Garbage Out"

Meaning:
Bad data → Bad AI model
------------------------------------------------------------------------------------------
### Important Data Quality Characteristics
Accuracy:- Age = 250 years ❌
Completeness:- missing any column
Consistency:- India,IND,Indian ❌
Timeliness:- Example:   Stock price from 2010 is not useful for today's trading prediction.

---------------------------------------------------------------------------------------

### Why do we need to understand Data Types?

Before training any Machine Learning model, the first question an AI Engineer asks is:
"What type of data do I have?"
Because different data types require different processing.

---------------------------------------------------------------------------------------

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

------------------------------------------------------------------------------------

### Qualitative Data (Categorical Data)

Your PPT defines:

Qualitative data deals with characteristics and descriptors that cannot be easily measured but can be observed subjectively.

In simple words:
### Qualitative data describes qualities, categories, or labels.

It answers:
"What type?"
"What category?"
"What group?"

Example 3: Customer Feedback
Excellent
Good
Average
Poor

This is also categorical.

### Example:-
In Machine Learning
Suppose Amazon has:

Customer	Product Category
A	Electronics
B	Clothing
C	Grocery

A model cannot understand:
Electronics
Clothing
Grocery

So we convert:
Electronics → 1
Clothing    → 2
Grocery     → 3

This process is called:
### Encoding

-----------------------------------------------------------------------------------------------

### Types of Qualitative Data

There are two types:

Qualitative Data

        |
 ----------------
 |              |
Nominal       Ordinal

----------------------------------------------------------------------------------------------
### Nominal Data
Definition
Your PPT:   Data with no inherent order or ranking is called Nominal Data.

Simple meaning:
Nominal = Names only

### There is no ranking.

### Examples
Gender
Country
Religion 
color


### Nominal Data Characteristics
| Property               | Answer |
|------------------------|--------|
| Numeric?               | No     |
| Order exists?          | No     |
| Can calculate average? | No     |
| Ranking possible?      | No     |

--------------------------------------------------------------------------------------------

### Ordinal Data

Definition:-    Data with an ordered series is called Ordinal Data.

Simple meaning:     Ordinal = Order exists.
Categories have ranking.

### Example
Customer Satisfaction:-
Order exists:   Poor < Average < Good < Excellent

Star Rating
1 ⭐
2 ⭐⭐
3 ⭐⭐⭐
4 ⭐⭐⭐⭐
5 ⭐⭐⭐⭐⭐

Order exists.
---------------------------------------------------------------------------------------------
### Nominal vs Ordinal

Very important interview question.

| Feature  | Nominal | Ordinal |
|----------|---------|---------|
| Category | Yes     | Yes     |
| Order    | No      | Yes     |
| Ranking  | No      | Yes     |
| Example  | Color   | Rating  |

-----------------------------------------------------------------------------------------------
### Nominal:
No order
Example:Gender Color City CustomerID


### Ordinal:
Order exists
Example:    Rating Education Satisfaction


### Discrete:
Countable numbers
Example:Number of students

### Continuous:
Measurable values
Example:    Height Weight Temperature Salary
----------------------------------------------------------------------------------------------
### Quantitative Data (Numerical Data)

⇒ Quantitative data deals with numbers and things you can measure objectively.

### What is Quantitative Data?
Simple Explanation

⇒ Quantitative data is data that represents:

Numbers
Measurements
Counts
Quantities
--------------------------------------------------------------------------------------------
### Types of Quantitative Data
             Quantitative Data
                    |
          ---------------------
          |                   |
     Discrete Data       Continuous Data
--------------------------------------------------------------------------------------------
### Discrete Data
> Discrete data can hold a finite number of possible values
> Discrete = Data that can be counted.(WHOLE NUMBER)

### Example
Number of Students
Number of Cars
Number of Orders
-------------------------------------------------------------------------------------------
### Continuous Data
> Continuous data can hold infinite number of possible values.
> Continuous = Data that can be measured.

### Example
Height-> 174.5
Weight-> 80.90
Temperature->35.5
-------------------------------------------------------------------------------------------
### Discrete vs Continuous (Very Important Interview Question)

| Discrete                    | Continuous              |
|-----------------------------|-------------------------|
| Count data                  | Measurement data        |
| Whole numbers               | Decimal values possible |
| Finite values               | Infinite values         |
| Example: Number of students | Example: Height         |
| Example: Number of cars     | Example: Weight         |

============================================================================================
--------------------------------------------------------------------------------------------
### Statistics:- (Module 2)
--------------------------------------------------------------------------------------------
### Definition:-

→ Statistics is an area of applied mathematics concerned with data collection, analysis, interpretation, and presentation.

>   Statistics is the science of:
### Collecting data → Understanding data → Finding patterns → Making decisions

>   Real-Life Example 1: Netflix

Netflix has millions of users. They want to know:
"Will users like a new movie?"

They analyze:User Data
User Data

 |
 |-- Watching history
 |-- Ratings
 |-- Likes
 |-- Search history
          ↓
      Statistics
          ↓
      Prediction

Statistics helps find patterns:
>   People who watched A also watched B
>   Users of age group 20-30 prefer certain movies
-------------------------------------------------------------------------------------------
### Why Do Data Scientists Need Statistics?

Because ML algorithms are built on statistical concepts.

-----------------------------------------------------------------------------------------
###    Statistics in Data Science Lifecycle

                 Raw Data

                    |
                    ↓

              Statistics

                    |
     --------------------------------
     |                              |

Understand Data              Find Patterns

     |                              |

     ↓                              ↓

        Machine Learning Model

                    |

                    ↓

              Prediction

---------------------------------------------------------------------------------------------
### Types of Statistics
                 Statistics

                     |
        ----------------------------
        |                          |
 Descriptive Statistics       Inferential Statistics

--------------------------------------------------------------------------------------------- 
### Descriptive Statistics:- 
        1. Describes and summarizes the data we already have.
        2. It uses the data to provide description of population either through numerical calculation or Graph and Tables.
It answers: "What happened?"

Example:-   
Suppose we have student marks: 50 60 70 80 90

Descriptive statistics tells:

Average marks:  70
Highest:        90
Lowest:         50

### Common Descriptive Statistics Techniques

>   1.  Central Tendency (Measure of central tendency)

Finding the center value:

Mean    >   Statistical average of data
Median  >   Middle value of data after sorting data.
Mode    >   Most frequent occurring value. 

Example:    10,20,30,40,50
Mean:   30

>   2).  Measure of Spread (Measure of Dispersion)

Understanding data variation:
        >   Range
        >   Variance
        >   Standard deviation
        >   IQR

---------------------------------------------------------------------------------------------

### Inferential Statistics

Definition:-
            1. Inferential statistics makes predictions about a population based on a sample of data taken from the population.
            2. Using a small amount of data to make conclusions about a larger group.

Asks:- "What may happen?" 

Example:- Exit poll(So a survey company asks:50,000 people,This is a sample.They predict:Possible           election result)

------------------------------------------------------------------------------------------------

### Descriptive vs Inferential Statistics

| Descriptive              | Inferential                                |
|--------------------------|--------------------------------------------|
| Summarizes existing data | Predicts about larger population           |
| Uses complete dataset    | Uses sample data                           |
| No prediction            | Makes prediction                           |
| "What happened?"         | "What may happen?"                         |
| Example: Average salary  | Example: Predict average salary of country |

-----------------------------------------------------------------------------------------------

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

-------------------------------------------------------------------------------------------------

### Where Statistics is Used in AI?
Computer Vision

1.  Example:    Face recognition:

Statistics helps understand:
Pixel distributions
Feature patterns

2).  Example:   ChatGPT-like systems:

Statistics helps with:
Probability of next word
Language patterns

Example:
Sentence:
The sky is ______

Probability:

blue → 80%
green → 5%
red → 2%


>3:- Recommendation Systems
Example:

Amazon:
"Customers who bought this also bought..."
Based on statistical patterns.
-------------------------------------------------------------------------------------------------

DESCRIBE = DESCRIPTIVE ("What happened?").Average salary of employees, Total sales last month

PREDICT/INFER = INFERENTIAL("What can we conclude about a larger group?"). Election prediction 

-------------------------------------------------------------------------------------------------
=================================================================================================
### Population and Sample
-------------------------------------------------------------------------------------------------

### What is Population?

Simple Explanation
>   Population means the complete set of all items, people, or observations that we want to study.

In simple words:
>   Population = Everything we are interested in.

Example:- Total number of Employees 10000, so population is 10000.

Example;-    Amazon has: 500 million customers
Question:   "What is the average amount spent by customers?"
Population:  All 500 million customers

### Real-Life Example 3: Machine Learning

Suppose we build a fraud detection model for banking.
Population:     All bank transactions
Example:    10 years of transactions    = Population

-------------------------------------------------------------------------------------------

###     What is Sample?
>   Simple Explanation :-
        A sample is a smaller subset selected from the population for analysis.

In simple words:
Sample = A small group representing the entire population.

### Example

Company:    Population: 10,000 employees

But collecting data from everyone may be difficult.

So we select:   500 employees,  This 500 employees group is:    Sample

-----------------------------------------------------------------------------------------

### Why Do We Need Samples?
Because studying the complete population can be
>   Expensive
>   time Consuming
>   Sometimes Impossible
----------------------------------------------------------------------------------------

### Population vs Sample
| Population     | Sample        |
|----------------|---------------|
| Entire group   | Part of group |
| Larger         | Smaller       |
| More accurate  | Less accurate |
| Expensive      | Cheaper       |
| Time-consuming | Faster        |
| Symbol: N      | Symbol: n     |

----------------------------------------------------------------------------------------

### Population Parameter vs Sample Statistic

Population Parameter:- μ (mu)   (Average salary of all employees.)
Sample Statistic    :- x̄ (x-bar)   (Average salary of selected employees.)

------------------------------------------------------------------------------------------
Population
     |
     |
 Calculate
     |
     ↓
 Parameter


Sample
     |
     |
 Calculate
     |
     ↓
 Statistic

-------------------------------------------------------------------------------------------
Population = Entire group

Sample = Small part of population

-------------------------------------------------------------------------------------------
==========================================================================================
###   Sampling Techniques
==========================================================================================
-------------------------------------------------------------------------------------------
### Sampling

>   The process of selecting a sample from a population.

### Why Do We Need Sampling?
>   Saves Time
>   Reduces Cost
>   Makes Analysis Possible
-------------------------------------------------------------------------------------------

### Types of Sampling
                                    Sampling
                                        |
        -----------------------------------------------------------------
        |                                                               |
 Probability Sampling                                           Non-Probability Sampling
        |                                                                |
 -------------------------                                       -------------------------
 |           |            |                                      |           |            |
Simple    Stratified   Cluster                                 Purposive    Quota       Convenience
Random
-------------------------------------------------------------------------------------------

### Probability Sampling:-
In probability sampling:
>   Every member of the population has a known chance of being selected.
>   Simple meaning:     Everyone has a fair opportunity.

Example:
A company has 10,000 employees;A computer randomly selects  500 employees
so
Every employee had a chance.

### Probability Sampling Types

>   Simple Random Sampling
>   Stratified Sampling
>   Cluster Sampling

#   Simple Random Sampling:-    
        Every individual has an equal chance of being selected.

#   Stratified Sampling:-
        - Stratified sampling divides the population into groups called strata, then selects samples from each group.
        - Divide into categories first, then randomly select from each category.

#    Cluster Sampling:-
        Cluster sampling divides the population into groups called clusters, then randomly selects entire clusters.
            Population


### Non-Probability Sampling
>   Everyone does not have a known chance of selection.
Selection depends on:
    
Convenience
Researcher's choice
Availability

------------------------------------------------------------------------------------
### Stratified vs Cluster (Very Important Interview Question)
Stratified	                                        Cluster
Divide into groups	                            Divide into groups
Select from every group                     	Select complete group
Groups are internally different             	Groups are usually similar
Better accuracy	                                Cheaper
------------------------------------------------------------------------------------

                 Probability Sampling
                         |
        ----------------------------------
        |               |                |
 Simple Random      Stratified         Cluster


Simple Random:
----------------
Random selection
Everyone equal chance


Stratified:
----------------
Divide into groups
Take samples from every group


Cluster:
----------------
Divide into groups
Select complete groups

----------------------------------------------------------------------------------------------
==============================================================================================
### Non-Probability Sampling
----------------------------------------------------------------------------------------------
>   Non-Probability Sampling:
           Every member of the population does NOT have a known chance of being selected.

Selection depends on:
Availability
Researcher's choice
Easy access
Existing connections

>   Non-Probability Sampling is a sampling method where samples are selected based on non-random     criteria instead of equal probability.

          Non-Probability Sampling

                    |
       ----------------------------------
       |            |                   |
 Convenience      Judgment            Snowball
 Sampling         Sampling            Sampling
                 (Purposive 
                    Sampling)                      
 
>   Convenience Sampling:-  "Who is easily available?"
>   Judgment Sampling (Purposive Sampling):- Their own knowledge and judgment.
>   Snowball Sampling :- Existing participants help find new participants.Like a snowball growing       bigger.
------------------------------------------------------------------------------------------------

### Probability vs Non-Probability Sampling
| Probability Sampling        | Non-Probability Sampling      |
|-----------------------------|-------------------------------|
| Random selection            | Non-random selection          |
| Equal chance                | Unequal chance                |
| Less bias                   | More bias                     |
| More statistically reliable | Less reliable                 |
| Example: Random sampling    | Example: Convenience sampling |

---------------------------------------------------------------------------------------------
=============================================================================================
### Data Distribution
---------------------------------------------------------------------------------------------
>   What is Data Distribution?

Data distribution describes how values in a dataset are spread or arranged.

>   In simple words:    Distribution tells us how frequently different values occur in our data.

Imagine a classroom:- 100 students' marks:

Marks:
0-20       → 5 students
21-40      → 15 students
41-60      → 40 students
61-80      → 30 students
81-100     → 10 students

We can represent this as a distribution:

Number
of
Students

 ^
 |
 |              *
 |              *
 |        *     *
 |        *     *
 |   *    *     *
 |_________________________

 0-20  21-40 41-60 61-80 81-100

          Marks
-------------------------------------------------------------------------------------------

### Types of Data Distribution

              Data Distribution

                     |
        ---------------------------
        |            |            |
    Normal       Uniform      Other(Binomial and Bernoli)
 Distribution   Distributions.         Distributions
 (Gaussian)


### What is Normal Distribution?
Normal distribution is a distribution where:

    -   Most values are around the average
    -   Fewer values appear as we move away from average

It creates a **bell-shaped curve**.

              *
            *   *
          *       *
        *           *
      *               *
____*___________________*____

       Average Height

### Properties of Normal Distribution
1. Bell-shaped Curve
2. Left side and right side are mirror images.
3. Mean = Median = Mode
--------------------------------------------------------------------------------------------
### Real-World Examples of Normal Distribution
1. Human Height
Most people average height.
Few very tall/short people.

2. Exam Scores
If exam is well-designed,
Most students score around average.
Few score extremely high or low.

3. Measurement Errors
Scientific measurements often follow normal distribution.
---------------------------------------------------------------------------------------------
### Normal Distribution in Machine Learning

Formula:
z   =  x−μ      /σ

Where:
μ = Mean
σ = Standard deviation

---------------------------------------------------------------------------------------------
=============================================================================================
### Uniform Distribution

>   In a Uniform Distribution, every possible value has an equal chance of occurring.

Real-Life Example 1: Dice Roll 🎲
A normal dice has:
1  2  3  4  5  6

Probability:

1 → 1/6
2 → 1/6
3 → 1/6
4 → 1/6
5 → 1/6
6 → 1/6

Every number has the same chance

-----------------------------------------------------------------------------------------

## Uniform Distribution:-

*  *  *  *  *  *  *  *

----------------------

All values have equal frequency

-----------------------------------------------------------------------------------------

### Types of Uniform Distribution
There are two types:

             Uniform Distribution
                    |
          -------------------
          |                 |
     Discrete           Continuous

`Discrete`:- When the possible outcomes are separate/countable value
like 1,2,3,4,5

`Continuous`:- When every value within a range has equal probability
Between:    0 to 1

Possible values:
0.1
0.25
0.56
0.99
---------------------------------------------------------------------------------------------

### Normal vs Uniform Distribution
| Normal Distribution            | Uniform Distribution      |
|--------------------------------|---------------------------|
| Values concentrate around mean | All values equally likely |
| Bell-shaped curve              | Rectangle-shaped curve    |
| Mean = Median = Mode           | Mean is center of range   |
| Example: Human height          | Example: Dice roll        |
| Most values near center        | Equal spread              |

-------------------------------------------------------------------------------------------
==========================================================================================
### Skewness
------------------------------------------------------------------------------------------
>   Skewness is the measure of asymmetry  of distribution.
>   How much a dataset is tilted or not symmetrical
>   Data is asymmetric when its left and right side are not mirror image.

In simple words:
It tells us whether data is:

-   Balanced around the center
-   More spread on the left side
-   More spread on the right side
-----------------------------------------------------------------------------------------
### Types of Skewness

              Skewness

                  |
       -----------------------
       |          |          |
   Positive     Zero     Negative
    Skew       Skew       Skew

###   Positive Skewness (Right Skewed)
>   Definition:-    When the tail of the distribution is longer on the right side.

## Relationship Between Mean, Median, Mode
>   For positive skew:
-   Mean > Median > Mode

### Negative Skewness (Left Skewed)
>   Definition:-    When the tail is longer on the left side.

## Relationship Between Mean, Median, Mode
>   For Negative skew:
-   Mean < Median < Mode

---------------------------------------------------------------------------------------
### Summary Table

| Type          | Tail Direction | Relationship         |
|---------------|----------------|----------------------|
| Positive Skew | Right          | Mean > Median > Mode |
| Zero Skew     | None           | Mean = Median = Mode |
| Negative Skew | Left           | Mean < Median < Mode |

--------------------------------------------------------------------------------------

### Why Skewness Matters in Machine Learning?
>   Detect Data Problems
>   Choose Data Transformation
>   Improve ML Model Performance

--------------------------------------------------------------------------------------

Distribution → How data is spread

Skewness → Whether data is tilted left or right

------------------------------------------------------------------------------------------
==========================================================================================
------------------------------------------------------------------------------------------
### Kurtosis
------------------------------------------------------------------------------------------
##      Definition
>   Kurtosis tells us how much data is concentrated in the center and how extreme values (outliers) are present.
  
>   Kurtosis measures the shape of a distribution, especially the behavior of its tails and peak.

Peakness → Height/sharpness of the curve
Taildness → Thickness/length of tails

### Visual Understanding
1.  Normal Distribution
              *
            *   *
          *       *
        *           *
_______*_____________*_______
⇒ Balanced peak and tails.

2.  High Kurtosis
               *
              ***
             *****
            *******
___________*_______*___________
⇒ Very high concentration near mean
⇒ More extreme values

3.  Low Kurtosis
Flat peak + lighter tails

          *****
        *********
      *************
_____________________

⇒ Data is more spread out
⇒ Fewer extreme values
--------------------------------------------------------------------------------------------
### Components of Kurtosis
    >   Peakness

    Peakness means:
How tall or sharp the center of the distribution is.

Example:
High peak:
          *
         ***
        *****

Low peak:
       *****
     *********
---------------------------------------------------------------------------------------------
    >   Taildness

    Taildness means:
How much data exists at extreme ends.

Example:
Heavy tails:
*                       *
 \                     /
  \_______*___________/

Light tails:
        *
      *   *
_____*_____*_____
----------------------------------------------------------------------------------------------
###         Types of Kurtosis

There are three types:

                 Kurtosis
                    |
        ---------------------------
        |            |            |
   Leptokurtic   Mesokurtic   Platykurtic

1.  Mesokurtic
##  Definition:-    A distribution with kurtosis similar to normal distribution.

It has:
Medium peak
Medium tails

>   Normal distribution is: Mesokurtic
Visual:
              *
            *   *
          *       *
_________*_________*________
Kurtosis value: 3
(or excess kurtosis = 0)

Real-Life Example
Many natural measurements:  Height, Weight, Measurement errors

2. `Leptokurtic`
##   Definition:-
        Most values are close to mean, but extreme values occur more frequently.  

A distribution with:
High peak
Heavy tails

Visual:
              *
             ***
            *****
           *******
__________*_______*__________

Characteristics:
✅ Sharp peak
✅ Heavy tails
✅ More outliers

Real-Life Example:-
Financial market returns:- sometimes:+20%,-30%
Extreme events occur.

3.  Platykurtic
>   Definition:-    Data is more evenly spread.

A distribution with:
Low peak
Thin tails

Visual:
        ********
      ************
    ****************
____________________

Characteristics:
✅ Flat curve
✅ Less extreme values
✅ More distributed data

--------------------------------------------------------------------------------
###     Comparison Table

| Type        | Peak   | Tails  | Outliers |
|-------------|--------|--------|----------|
| Mesokurtic  | Medium | Medium | Normal   |
| Leptokurtic | High   | Heavy  | More     |
| Platykurtic | Low    | Thin   | Less     |

-----------------------------------------------------------------------------------

### Skewness vs Kurtosis (Very Important Interview Question)

| Skewness            | Kurtosis         |
|---------------------|------------------|
| Measures asymmetry  | Measures shape   |
| Left/right movement | Peak and tails   |
| Direction of data   | Extreme values   |
| Positive/negative   | Lepto/Meso/Platy |

------------------------------------------------------------------------------------
### Example:

Salary data:30000 40000 50000 60000 5000000

>   Skewness tells:     Data is shifted to the right.

>   Kurtosis tells:     There is an extreme value with heavy tail.
-----------------------------------------------------------------------------------
### Leptokurtic

Think:
"LEPTO = Large Extremes"

High peak
+
Heavy tails
+
More outliers

Example:    Stock market crashes

### Mesokurtic

Think:  "Normal"
Normal distribution

### Platykurtic

Think:  "Plate = Flat"

Flat peak
+
Less extreme values

--------------------------------------------------------------------------------------------------
==================================================================================================
###     What is EDA?
-------------------------------------------------------------------------------------------------

#   EDA:- 
>   EDA is like getting to know your data before teaching a machine learning model.

EDA stands for: Exploratory Data Analysis

It is the process of:
-   Understanding data
-   Finding patterns
-   Detecting problems
-   Discovering relationships
-   Preparing data before building ML models

###     Real-Life Analogy

Imagine you are hiring an employee. Before hiring, you check:

Name
Experience
Skills
Education
Background

You don't directly hire without knowing anything.
Similarly, before building an ML model:

You inspect:
Data types
Missing values
Outliers
Distribution
Relationships

>   This process is EDA
-------------------------------------------------------------------------------------------

###     Why is EDA Important?
>   Understand Data Structure
>   Find Missing Values
>   Detect Outliers
>   Understand Distribution 
>   Find Relationships Between Features
>   Select Important Features

------------------------------------------------------------------------------------------
### EDA Workflow
              Raw Dataset

                    |
                    ↓

        1. Understand Data

                    |
                    ↓

        2. Data Cleaning

                    |
                    ↓

        3. Statistical Analysis

                    |
                    ↓

        4. Visualization

                    |
                    ↓

        5. Feature Analysis

                    |
                    ↓

          ML Model Building
--------------------------------------------------------------------------------------------
###     Step 1: Understand Dataset

First questions:
-   How big is the data?
-   What are column names?
-   What are data types?

-   df.shape (How many rows and column)
-   df.info() (what all datatype)
-   df.describe() (Check Statistics)

-------------------------------------------------------------------------------------------
###     Types of EDA

-   Univariate Analysis
-   Bivariate Analysis
-   Correlation Analysis
-------------------------------------------------------------------------------------------

###     Univariate Analysis
>   "Uni" means one.
Analysis of:        Single variable

Example:    Age column only
Visualization:

Histogram:
Age

     *
    ***
   *****
 *********
____________

20 30 40 50
---------------------------------------------------------------------------------------------
###     Bivariate Analysis

"Bi" means two. Analysis between:

>   Two variables

Example:
Experience vs Salary

Question:
Does experience affect salary?

Experience ↑
Salary ↑

Visualization:
Scatter plot:

Salary

 ^
 |
 |          *
 |       *
 |    *
 | *
 |______________

   Experience

--------------------------------------------------------------------------------------------

###     Multivariate Analysis

More than two variables.

Example:
House price prediction:

Area
Bedrooms
Location
Age
Price

All together.

------------------------------------------------------------------------------------------

###         EDA in Real ML Project

Example:    Predict house prices.
Dataset:
Area
Bedrooms
Location
Age
Price

>   EDA process:

Step 1
Check missing values:

Step 2
Check outliers: House price = 100 crore

Step 3
Check distribution: Price distribution

Step 4
Check relationship: Area vs Price

Step 5
Select features:
-   Keep:Area Bedrooms Location
-   Remove: House_ID
--------------------------------------------------------------------------------------------
### What is Univariate Analysis?
>   We study a single column independently.

Example :-
| Age | Salary | City      | Purchased |
| --- | ------ | --------- | --------- |
| 25  | 50000  | Bangalore | Yes       |
| 30  | 70000  | Pune      | No        |
| 35  | 90000  | Delhi     | Yes       |

If we analyze only: Age, we are doing:  Univariate Analysis;
We are not checking relationship with Salary or Purchase.

-------------------------------------------------------------------------------------
### Why Do We Perform Univariate Analysis?
>   Data Distribution:- How are values spread?
>   Central Tendency:-  We find: Mean, Median, Mode
>   Spread of Data :-   We measure:
                                    **Range
                                    Variance
                                    Standard deviation
                                    IQR**
>   Detect Outliers
--------------------------------------------------------------------------------------
### Types of Univariate Analysis

There are two major types:

                 Univariate Analysis
                         |
          --------------------------------
          |                              |
     Numerical Data              Categorical Data

###   A) Numerical Univariate Analysis
Used for:   Quantitative data

Examples:   Age Salary Height Weight Experience

>We analyze:

1. Descriptive Statistics:-
    Using:  Mean, Median, Mode, Minimum, Maximum, Standard, Deviation, Variance

2. Distribution:-
    Is data: Normal? Skewed? Uniform?

3. Visualization:-
    Histogram:- Used to see distribution.

###   B) Categorical Univariate Analysis
Used for:   Qualitative data

Examples:   Gender City Department Product category

We analyze:

1. Frequency Count:-
    Gender:
        Male       600
        Female     400
    >   df["Gender"].value_counts()

2. Proportion / Percentage
    Example:
           Male: 600/1000    = 60%

3. Visualization
    Bar Chart
      Example: City:
                 Bangalore  *****
                 Delhi      ***
                 Mumbai     ****

    Pie Chart
      Example: Gender:
                   Male     60%
                   Female   40%
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
###     Bivariate Analysis
This is even more important because it helps us understand:

>   Relationship between features
>   Correlation
>   Feature selection for ML models

-   Bivariate Analysis → Study relationship between two variables

### What is Bivariate Analysis.
Bi means:   Two

Variate means:  Variables / Features

>   So: Bivariate Analysis means analyzing the relationship between two variables.
example :- High experience High Salary
----------------------------------------------------------------------------------------------
### Why Do We Perform Bivariate Analysis?
>   Find Relationships Between Features
>   Find Correlation.(How strongly two numerical variables are related.)
>   Feature Selection(Experience , salary)
>   Understand Target Variable

In ML:
>Target variable = output we want to predict.

Example:    Customer churn:
Target:     Churn
-----------------------------------------------------------------------------------------------
###         Types of Bivariate Analysis

There are mainly three combinations:

              Bivariate Analysis
                      |
       --------------------------------
       |              |               |
Numerical        Numerical        Categorical
    vs              vs                vs
Numerical       Categorical       Categorical

### TYPE 1:-    Numerical vs Numerical
Example:
                Experience
                     +
                Salary
Both are numerical.

Common Visualization:   Scatter Plot

### Real life example
| Variable 1       | Variable 2  |
|------------------|-------------|
| Height           | Weight      |
| Experience       | Salary      |
| Area             | House Price |
| Advertising Cost | Sales       |
-------------------------------------------------------------------------------------------------

###     TYPE 2:- Numerical vs Categorical
Example:    Salary according to Department:

Department	    Salary
IT	            80000
HR	            50000
Finance	        70000

Here:
Department → Categorical
Salary → Numerical

Visualization:  Box Plot

#   Real-life examples:

| Categorical | Numerical   |
|-------------|-------------|
| Gender      | Height      |
| City        | House Price |
| Department  | Salary      |
----------------------------------------------------------------------------------------------
###     Categorical vs Categorical
Example:

Gender      vs      Purchased
Male	                Yes
Female	                No
Male	                Yes

Both are categorical.

Visualization:  Count Plot / Bar Chart

#   Real-life examples:

Category1	            Category2
Gender	                Purchase
Education	            Job Status
City	                Product Choice

--------------------------------------------------------------------------------------------------
### Bivariate vs Univariate

| Univariate            | Bivariate              |
|-----------------------|------------------------|
| One variable          | Two variables          |
| Distribution analysis | Relationship analysis  |
| Mean, median, mode    | Correlation            |
| Histogram             | Scatter plot           |
| Box plot              | Box plot, scatter plot |
-------------------------------------------------------------------------------------------------
###     Important Memory Shortcut

| Variables                 | Example              | Visualization |
|---------------------------|----------------------|---------------|
| Numerical + Numerical     | Age vs Salary        | Scatter Plot  |
| Numerical + Categorical   | Salary vs Department | Box Plot      |
| Categorical + Categorical | Gender vs Purchase   | Bar Chart     |
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
### Correlation Analysis
-----------------------------------------------------------------------------------------------
###     What is Correlation?

Simple Explanation
>   Correlation means: A statistical measure that tells how strongly two variables are related to each other.

In simple words: Correlation tells us whether two variables move together or not.

### Real-Life Example 1: Height and Weight

Data:

Height	    Weight
150 cm	    45 kg
160 cm	    55 kg
170 cm	    65 kg
180 cm	    75 kg

Observation:    When height increases:

Height ↑
Weight ↑

Both move in the same direction.
>   Therefore:  Positive Correlation
-------------------------------------------------------------------------------------------------
### Why Do We Need Correlation Analysis?

-   Understand Relationships Between Features
-   Feature Selection
-   Remove Multicollinearity
-   Improve Model Performance
------------------------------------------------------------------------------------------------
###     Types of Correlation

There are three main types:

                 Correlation
                      |
        --------------------------------
        |              |              |
    Positive      Negative          Zero

### Positive Correlation
>   When one variable increases, another variable also increases

### Negative Correlation
>   When one variable increases, another variable decreases.

### Zero Correlation
>   No relationship between variables

------------------------------------------------------------------------------------------------
###         Correlation Coefficient

Correlation is represented by:      "r"

Range:
-1  --------  0  -------- +1

Meaning:
Value	                    Meaning
+1	                   Perfect positive correlation
0.8 to 1	           Strong positive
0.5 to 0.8	           Moderate positive
0	                   No relationship
-0.5 to -1	           Negative relationship

-------------------------------------------------------------------------------------
### Correlation Matrix

A correlation matrix shows relationships between all numerical features.

Example:
Dataset:
Age
Salary
Experience
Purchase

Matrix:

              Age Salary Exp

Age            1    0.5  0.6

Salary        0.5    1   0.9

Experience    0.6   0.9   1

--------------------------------------------------------------------------------------

###     Heatmap Visualization

A heatmap represents correlation visually.

Example:

        Age Salary Exp

Age      1   .5   .6

Salary  .5   1   .9

Exp     .6  .9    1

Color intensity shows strength.

------------------------------------------------------------------------------------------------
###     Correlation vs Causation (Very Important)

Interviewers love this question.

Correlation means:  Two variables move together.

It does NOT mean:   One variable causes the other.

----------------------------------------------------------------------------------------------

### Important Visualization Shortcut

| Data Problem                               | Best Graph   |
|--------------------------------------------|--------------|
| Trend over time                            | Line Chart   |
| Compare categories                         | Bar Chart    |
| Distribution of numerical data             | Histogram    |
| Relationship between 2 numerical variables | Scatter Plot |
| Detect outliers                            | Box Plot     |

------------------------------------------------------------------------------------
### Multivariate Analysis
-------------------------------------------------------------------------------------
### What is Multivariate Analysis?

Let's first understand the word.
Multi = Many
Variate = Variables / Features

So:
>   Multivariate Analysis means analyzing the relationship between three or more variables simultaneously.

In simple words:

Univariate → One variable
Bivariate → Two variables
Multivariate → Multiple variables
-----------------------------------------------------------------------------------------------
###     Difference Between Univariate, Bivariate and Multivariate

| Analysis Type | Number of Variables     | Example                                |
|---------------|-------------------------|----------------------------------------|
| Univariate    | One variable            | Salary analysis                        |
| Bivariate     | Two variables           | Experience vs Salary                   |
| Multivariate  | Three or more variables | Experience + Education + Age vs Salary |

-----------------------------------------------------------------------------------------------

###     Multivariate Analysis

Multiple columns:

Example:

Age
+
Experience
+
Education
+
Salary

Questions:
-   Does experience affect salary?
-   Does education level impact salary?
-   Does age influence salary along with experience?
----------------------------------------------------------------------------------------
###     Importance of Multivariate Analysis in ML
-   Understand Complex Relationships
-   Feature Selection
-   Detect Feature Interactions
           Sometimes two features together have more impact.

           Example:

                 Individually:
                              Education → Salary
                              Experience → Salary
    
                 But together:
                             Education + Experience → Salary
may give stronger prediction.
--------------------------------------------------------------------------------------------
### What is Descriptive Statistics?

Simple Explanation
Descriptive Statistics means:

>   Techniques used to summarize, organize, and describe the important characteristics of a dataset.

In simple words:

>   Instead of looking at thousands or millions of data points, descriptive statistics gives us a short summary of the data.
------------------------------------------------------------------------------------------------
### Why Do We Use Descriptive Statistics?
-   Understand Data Distribution
-   Detect Data Problems
-   Prepare Data for ML
------------------------------------------------------------------------------------------------
###         Categories of Descriptive Statistics

Descriptive statistics mainly has two parts:

              Descriptive Statistics
                     |
        --------------------------------
        |                              |
Central Tendency                Measures of Spread
        |                              |
 Mean Median Mode              Range IQR Variance
                               Standard Deviation
-----------------------------------------------------------------------------------------------
###     Measures of Central Tendency

Central tendency means:
>   A value that represents the center or typical value of a dataset.

>   The three main methods are:

-   Mean    (Average) ->    Mean is highly affected by outliers
-   Median  (middle value of data after sorting)
-   Mode    (most frequently occurring value)
------------------------------------------------------------------------------------------
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
--------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------
###     Missing Value Replacement (Missing Data Handling)
-------------------------------------------------------------------------------------------
### What are Missing Values?

A missing value means:

>   A value that is not available or not recorded in a dataset.

It is usually represented as:

-   NaN
-   NULL
-   None
-   Blank
-   ?
---------------------------------------------------------------------------------------------
### Impact of Missing Values

-   Reduces Data Quality
-   Creates Bias
-   Reduces Model Performance
----------------------------------------------------------------------------------------------
### How Do We Handle Missing Values?

             Missing Values
                    |
        ----------------------------
        |                          |
     Remove                    Replace
        |                          |
 Delete rows              Mean/Median/Mode
 Delete columns
 
    >   Remove

A) Remove Row:-
    When Use:- 
        Very few missing values exist
        Large dataset available
    When not use:-
        Small dataset

B)Remove Column:-
        when has many missing values
----------------------------------------------------------------------------------------------
    > Replace

#   Mean Replacement
>   Definition: Replace missing values with the average value of that column.
Use mean when:

✅ Numerical data
✅ Data is normally distributed
✅ No extreme outliers

#   Median Replacement
>   Definition: Replace missing values with the middle value of sorted data.
Use median when:

✅ Numerical data
✅ Data contains outliers
✅ Data is skewed

#   Mode Replacement
>   Definition: Replace missing values with the most frequently occurring value
Use mode for:

✅ Categorical data

Examples:

Gender
City
Department
Product Category
------------------------------------------------------------------------------------------------
###         Mean vs Median vs Mode Decision Table

| Data Type   | Condition           | Method |
|-------------|---------------------|--------|
| Numerical   | Normal distribution | Mean   |
| Numerical   | Outliers/Skewed     | Median |
| Categorical | Any distribution    | Mode   |

------------------------------------------------------------------------------------------------
### Measures of Spread (Dispersion)
-----------------------------------------------------------------------------------------------
### Measures of Spread

>   Definition:
        Measures of spread describe how much the values in a dataset are scattered or spread around the central value (mean/median).

In simple words:
>   It tells us how far data points are from each other.

---------------------------------------------------------------------------------------------
### Why Do We Need Measures of Spread?

-   Understand Data Variability
-   Detect Outliers
-   Compare Data Stability
-------------------------------------------------------------------------------------------

###         Types of Measures of Spread

                Measures of Spread
                       |
        --------------------------------
        |              |              |
      Range           IQR          Variance
                                      |
                                      ↓
                            Standard Deviation
----------------------------------------------------------------------------------------------
### Topic 1: Range

Definition:
>   Range is the difference between the maximum and minimum value in a dataset.

Formula:
>   Range = Maximum Value - Minimum Value

### Limitations of Range
-   Highly affected by Outliers
-   Does not consider all values

-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
###             IQR
-------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
###     What is IQR?

Definition:
>   Interquartile Range measures the spread of the middle 50% of data values.

In simple words:
>   IQR tells us how much the central half of the data is spread.

----------------------------------------------------------------------------------------------
###     Quartile means:

>   Dividing sorted data into four equal parts.

Imagine a dataset:
0% -------------------- 100%

Divide into:
0% ---- 25% ---- 50% ---- 75% ----100%

These points are:
Q1
Q2
Q3
Q4

>   Q1 (First Quartile); Also called: 25th Percentile

Meaning:
25% of data is below Q1.

>   Q2 (Second Quartile); Also called: 50th Percentile

Meaning:
50% of data is below Q2.

>   Q3 (Third Quartile); Also called: 75th Percentile

Meaning:
75% of data is below Q3.
-----------------------------------------------------------------------------------------------
###     Visual representation:

Sorted Data:

|---------|---------|---------|---------|
          Q1        Q2        Q3
          |         |         |
         25%       50%       75%
------------------------------------------------------------------------------------------------
###     IQR Formula

     >  IQR = Q3 - Q1
-----------------------------------------------------------------------------------------------

###         Step-by-Step IQR Calculation

Dataset:    10,20,30,40,50,60,70,80,90  (Already sorted.)

>   Step 1: Find Median (Q2) = Middle value:

10,20,30,40,50,60,70,80,90
             ↑
             Q2
Q2:= 50
---------------------------
>   Step 2: Find Q1

Lower half: 10,20,30,40

Middle of lower half:   Q1=(20+30)/2

Q1: 25
----------------------------
>   Step 3: Find Q3

Upper half: 60,70,80,90

Middle of upper half:   Q3=(70+80)/2

Q3:75
-----------------------------
>Step 4: Calculate IQR

    Formula:    IQR=Q3−Q1

Therefore:      IQR=75−25

IQR:50
-------------------------------------------------------------------------------------
### 7. Understanding IQR Visually

Dataset:

10 20 30 40 50 60 70 80 90

|--------|================|--------|

        Q1              Q3
        25              75

The middle 50% data lies between:       25 to 75

Spread:     50
-------------------------------------------------------------------------------------------------
###     IQR vs Range

Very important interview question.

Range	                                                IQR
----------------------------------------------------------------------
Uses minimum and maximum	                            Uses Q1 and Q3
Affected by outliers	                                Less affected by outliers
Uses extreme values	                                    Uses middle 50% data
Less reliable with skewed data	                        Better for skewed data

------------------------------------------------------------------------------------------------
================================================================================================
###         IQR for Outlier Detection
------------------------------------------------------------------------------------------------
>   Formula

Lower Boundary:-         Q1−1.5×IQR

Upper boundary:-         Q3+1.5×IQR

> Any value outside this boundary is outlier.

>   Example
    
Suppose:

Q1 = 25
Q3 = 75
IQR = 50

>   Lower limit:    25−(1.5×50)     =   25−75   =   -50

>   Upper limit:    75+(1.5×50)     =   75+75   =   150

Therefore:
>   Normal range:           -50 to 150

Any value:  >150
>   is an outlier.
----------------------------------------------------------------------------------------------
### IQR memory trick

Q1 = 25%    (half of lower values of upper half/lower value)
Q2 = 50% = Median
Q3 = 75%    (half of middle values of upper half/middle value)

IQR = Q3 - Q1

>   Outlier:

Below:
Q1 - 1.5×IQR

Above:
Q3 + 1.5×IQR
------------------------------------------------------------------------------------------------
================================================================================================
### Variance
------------------------------------------------------------------------------------------------
### What is Variance?

>   Definition:
Variance measures how much individual data points differ from the mean value of the dataset.

>In simple words:
Variance tells us the amount of spread in data.
OR
> How far data points are spread from the mean.

##  Example
Dataset B:  10,30,50,70,90

Mean:   50

Difference:     -40,-20,0,20,40

Values are far from mean.
Variance will be high
-------------------------------------------------------------------------------------------------
### Why Do We Need Variance?
>   Understand Data Spread

Example:
Two investment funds:
Fund A
10%
11%
10%
9%

>Returns are stable.

Fund B
-20%
10%
30%
50%

>Returns fluctuate.

Both may have similar average return.

>Variance tells:    Risk level

Higher variance:    More fluctuation,   More risk
------------------------------------------------------------------------------------------
### 3. Variance Calculation Intuition

Let's calculate manually.

Dataset:2,4,6,8,10
Step 1: Find Mean

Formula:
>   Mean=Number of values/Sum of values

Calculation:
(2+4+6+8+10)/5
30/5

Mean:   6

Step 2: Find Difference from Mean

>   Formula:    Value - Mean

Table:
Value	    Value - Mean
2	        2-6 = -4
4	        4-6 = -2
6	        6-6 = 0
8	        8-6 = 2
10	        10-6 = 4

>   Step 3: Square the Differences

Why square? = Because negative and positive differences would cancel.

Example:    -4 + (-2) + 0 + 2 + 4 = 0

That would incorrectly show no variation.

So we square.

>   Difference	    Square
    -4	            16
    -2	            4
    0	            0
    2	            4
    4	            16

Step 4: Find Average of Squared Differences

Sum:    16+4+0+4+16 =   40

Divide by number of values: 40/5

Variance:   8

>   Formula of Variance:- 

Population Variance
>   Variance =
                       Sum of   (Value - Mean)²
                        ---------------------
                         Number of values

| Symbol | Meaning          |
|--------|------------------|
| σ²     | Variance         |
| x      | Individual value |
| μ      | Population mean  |
| N      | Number of values |

###### σ2 = ∑(x−μ)2/N

Meaning:

Find distance from mean
Square distance
Average those distances
-------------------------------------------------------------------------------------------------

### Limitations of Variance
1. Unit Problem

Example:    Salary: ₹

Variance:   ₹²

Squared unit is difficult to interpret.
>   This is why we use:     Standard Deviation
--------------------------------------------------------------------------------------------------

### Sensitive to Outliers
>   Extreme values increase variance.

----------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------
### Standard Deviation
>   Definition:
        Standard deviation measures how much individual data points are spread around the mean, using the same unit as the original data.

>   Simple words:
        It tells the average distance of data points from the mean.
------------------------------------------------------------------------------------------------------
### Relationship Between Variance and Standard Deviation

>   Standard deviation is simply the square root of variance.
Formula:

Standard Deviation  = √ Variance
SD=     √25 =   5

or

Variance    =   (Standard Deviation)^2
-------------------------------------------------------------------------------------------------
### How to calculate standard variation

>   Dataset:    2,4,6,8,10
mean :- 6

>Step 1: Calculate deviation
    Value	Value-Mean
    2	    -4
    4	    -2
    6	    0
    8	    2
    10	    4


>Step 2: Square deviation
    Deviation	Square
    -4	        16
    -2	        4
    0	        0
    2	        4
    4	        16


>Step 3: Calculate Variance

    Sum:    16+4+0+4+16=40
    Divide by number of values: 40/5=8
    Variance:   8

>Step 4: Take Square Root

SD= √ 8

SD= 2.82

>   Therefore:  Standard Deviation = 2.82
------------------------------------------------------------------------------------------
###     Standard Deviation and Normal Distribution

#   Approximately:  
    Mean ± 1 SD

#   contains:   68% data
    Mean ± 2 SD

#   contains:   95% data
    Mean ± 3 SD

#   contains:   99.7% data

Example:    Average height: 170 cm

SD: 10 cm

Then:   68% people:     160 - 180 cm
----------------------------------------------------------------------------------------

###     Variance vs Standard Deviation

| Variance                            | Standard Deviation            |
|-------------------------------------|-------------------------------|
| Average squared deviation from mean | Square root of variance       |
| Unit becomes squared                | Same unit as original data    |
| Harder to interpret                 | Easier to interpret           |
| Used in mathematical calculations   | Used for understanding spread |
| Sensitive to outliers               | Sensitive to outliers         |

------------------------------------------------------------------------------------------
### Important Concept Summary 🧠

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

-------------------------------------------------------------------------------------------------
###     Variance vs Standard Deviation

>   Variance

>   Definition:Variance measures how much data points are spread around the mean by calculating the              average squared deviation.

Formula:

Variance=   ∑(x−μ)^2
            ---------
                N
Example:    Dataset:    10,20,30,40,50

Mean:   30

Variance tells: How much the values are scattered from 30.
------------------------------------------------------------------------------------------------
### Standard Deviation

>   Definition: Standard deviation is the square root of variance and represents spread in the original unit.

Formula:    SD= √ Variance

Example:    If: Variance = 100  Then:

SD  =     √ 100   = 10
---------------------------------------------------------------------------------------------
###     Why Do We Need Both?

#   Variance
>   Variance is useful for mathematical calculations
>   Many statistical algorithms use variance internally.

Examples:

ANOVA
Regression analysis
Probability models
Feature selection techniques
>   Because squaring removes negative values and highlights large deviations.

#  Standard Deviation
>   Standard Deviation is useful for human interpretation   Because it comes back to original units. 

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
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

###   Population Variance vs Sample Variance

>The main interview confusion is:
                Why does population variance divide by N, but sample variance divide by N-1?

##  Population
>Definition: Population means the complete set of all observations we are interested in studying.

##  Sample
>Definition:Sample is a smaller subset selected from the population to analyze and make conclusions.

--------------------------------------------------------------------------------------------------
###     Population Variance

>   When we have all data points, we calculate population variance.

    σ2  =   ∑(x−μ)^2/N

| Symbol | Meaning               |
|--------|-----------------------|
| σ²     | Population variance   |
| x      | Individual value      |
| μ      | Population mean       |
| N      | Total population size |


###     Sample Variance
Now imagine:    Those 5 values are only a sample from a bigger population.

Example:    Population:     Millions of customers

Sample: 5 customers ,   Now we calculate sample variance.

Formula:- 
s^2     = ∑(x−xˉ)^2 /   n−1

###     Why n-1?
This is the most important concept.

>   The reason:     Sample mean is already calculated from the sample.

Because we estimate population variance using a sample, our sample usually has less variation than the real population.

>   Example:    Population: All students in India
    Sample:     100 students

The sample may accidentally select similar students. So sample variance tends to underestimate the true population variance.

>   To correct this:    We divide by:   n-1  instead of:    n

This is called: Bessel's Correction
------------------------------------------------------------------------------------------------
###     Difference Between Population and Sample Variance

| Population Variance             | Sample Variance                 |
|---------------------------------|---------------------------------|
| Uses complete data              | Uses subset of data             |
| Denominator = N                 | Denominator = n-1               |
| Mean = population mean          | Mean = sample mean              |
| Used when all data is available | Used when estimating population |
| Symbol σ²                       | Symbol s²                       |

