import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pyparsing import col

'''
colab file link
https://colab.research.google.com/drive/1_Oh02nSPk8lwXI60OhefrUCuzZD9VHJG?usp=sharing'''

#df  =   pd.read_csv(r"C:\Users\deeks\Desktop\python\python-repo\010-intellbi-classes\Data-Science\Dataset_DS\Advertisement_Dataset.csv")
print("Loading data...")
df = pd.read_csv("../Dataset_DS/Advertisement_Dataset.csv")
print("Data Loaded")

print("\nPrint top 5 rows")
print(df.head())

print("\nPrint bottom 5 rows")
print(df.tail())

print("\nTotal  number of rows and columns")
print(df.shape)

print(''' \n Info() :-
Index range → e.g., RangeIndex: 100 entries, 0 to 99
Column names → all columns in the DataFrame
Non‑null counts → how many values are present (helps spot missing data)
Data types → int64, float64, object (strings), etc.
Memory usage → how much memory the DataFrame consumes''')
df.info()

print('''\n generates summary statistics for numeric columns in your DataFrame,
      means transpose.It flips the rows and columns.
      So instead of statistics being rows and columns being features, 
      you get features as rows and statistics as columns''')
print(df.describe().T)

print('''\n Drop the column which has all unique value or has all same values
         because it does not adds any value''')

#df.dropna(subset=['NO'], inplace=True)
df.drop('No',axis=1,inplace=True)

print(df.head())

print('''\n check null values''')
print(df.isnull().sum())
#print(df.isnull().sum().sort_values(ascending=False))

print("\nSplit the dataset into categorical and numerical columns")
cat = df.select_dtypes(include='object').columns
num = df.select_dtypes(exclude='object').columns

print(cat)
print(num)

print(df.isnull().sum())

print("\nHandling outliers")
print("\n Outlier count using IQR:")
outlier_col = ["TV","Radio","Newspaper","Sales"]

for col in outlier_col:

    q1=df[col].quantile(0.25)
    q3=df[col].quantile(0.75)
    iqr = q3 - q1
    lb= q1-1.5*iqr
    ub= q3+1.5*iqr
    print(col,"iqr", ":", iqr)

    outliers = df[(df[col] < lb) | (df[col] > ub)]
    print("lower band",lb)
    print("upper band",ub)
    print(col,"outliers", ":", len(outliers))

    print("removing outliers from dataframe")
    df = df[(df[col] >= lb) & (df[col] <= ub)]
    print("\n")


print(df.head())

print(df.shape)

print("\n univariate analysis")
'''
What standard things are usually checked in univariate analysis

For numeric columns:
•minimum
•maximum
•mean
•median
•spread
•outliers
•histogram
•boxplot

For categorical columns:
•unique values
•most common category
•count of each category
'''
#("to check one veriable at a time or check unique value of each column")

plt.hist(df['TV'],bins=12)
plt.show()


##print for all values
for i in df:
  print(i)
  plt.hist(df[i])
  plt.show()










# 4i. Bivariate analysis
'''
Bivariate analysis
Correlation analyis - it is a statistical method used to evaluate the strength and direction of the relationship between 2 continuous variables.

It is calcuated using person correalation coefficient. and takes value between -1 to +1

if the value is +1: it means the 2 variables have perfect positive linear relationship if the value is 0: it means there is no linear correlation if the value is -1: it means the 2 variables have perfect negative linear relationship
'''

print("\n bivariate analysis")
print(df.corr())

'''========================================================================================='''

'''  ML Model building   '''

from sklearn.model_selection import train_test_split
##used to split the data into 4 parts: X_train, X_test, y_train, y_test

from sklearn.metrics import mean_squared_error , mean_absolute_error,root_mean_squared_error,r2_score

from sklearn.linear_model import LinearRegression




'''Divide the dataset into X (input), y (output) variables. X will have all the input data, y will have all the output data points
'''

X = df['TV']
y = df['Sales']

print("\n print X :\n" , X)
print("\n print y :\n" , y)



''' 3.
Further divide into X_train, X_test, y_train, y_test
'''

X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=0.2)


'''check using shape'''
print(X_train.shape,X_test.shape,y_train.shape, y_test.shape)

'''making X_train as 2D array'''
X_train = X_train.values.reshape(-1,1)

''' # Save the model into a variable    '''
lr = LinearRegression()

''' ## Model building   '''
lr.fit(X_train,y_train)

'''     ## Model parameters: C (intercept), m (coeff)       '''
print("intercept : ", lr.intercept_)
print("coefficient : ", lr.coef_)

# intercept :  7.137739830603478
# coefficient :  [0.04678405]

'''Therefore, the equation of best fit line is:'''
# y = 0.046X + 7.13

'''predict y value but before that we need to make X_test as 2d array'''
y_pred = lr.predict(X_test.values.reshape(-1, 1))

print("print y_pred",y_pred)


'''     Model Evaluation       '''
print("Mean squared error: ", mean_squared_error(y_test, y_pred))
print("Mean absolute error: ", mean_absolute_error(y_test, y_pred))
print("Root mean squared error: ", root_mean_squared_error(y_test, y_pred))
print("R2 score: ", r2_score(y_test, y_pred))

# Mean squared error:  7.783062942280791
# Mean absolute error:  2.011068218980129
# Root mean squared error:  2.789814141171557
# R2 score:  0.6652532432590647

''' Which means that the model is trained with 66.52% accuracy '''

''' As the problem suggests, we have to predict the output (Sales), when input is 50 Cr '''

print(lr.predict([[50]]))