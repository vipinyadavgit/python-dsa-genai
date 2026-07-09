
1. Understand the problem statement in detail. On the basis of this, you will able to identify which are the input variables and what is the output variable.
2. Import the libraries
3. Load the dataset
4. EDA (these arent the fixed series of steps to be followed, it can vary)
	a. Basic dataset check:
		i. df.shape - dimension of rows and columns
		ii. df.info() - it will print the information of the dataset i.e. datatypes, column names, number of not null values
		iii. df.describe() - Generate descriptive statistics.
		iv. print df.head() - gives first 5 rows / df.tail() - gives last 5 rows.
	b. Delete all the columns that have all the values in it as unique or all the values in it as same.- 
		because it doesnt add any value in the data science- 
          drop it using df.drop("column name")
	c. Handling null values:
		i. Check if the are null values - df.isnull().sum()
		ii. Ways to handle null values:
	    		- Delete the rows that have null value using dropna() (When there are small number of missing rows)
      			- Delete columns using df.drop() when there are more than 50% of the values in a particular column as null
     			- If the column has categorical datatype: Impute/Replace with mode
			- if the column has continuous numerical dataype: Impute/replace with mean
			- if the column has discrete numerical dataype: Impute/replace with median
	d. Handling duplicates:
		i. Check the duplicate rows in dataset - df.duplicated().sum()
		ii. Ways to handle duplicate values:
			- Remove duplicate using df.drop_duplicates()
	e. Split the dataset into categorical and numerical columns
		i. cat = df.select_dtypes(include = "object").columns
		ii. num = df.select_dtypes(exclude= "object").columns
	f. Handling error values: Error values can be anything (?, @, etc)
		i. Replace the error value with null using df.replace("?", np.NaN). 
		ii. Once all the errors are converted into Null, apply step c.
	g. Handling Outliers:
		i. Detect outliers using IQR method:
			- Find Q1 = df.quantile(0.25), Q3= df.quantile(0.75)
			- Find IQR =  Q3 - Q1
			- LB = Q1 - 1.5*IQR, UB = Q3 + 1.5*IQR
			- Remove all the values less than LB and greater than UB
	h. Univariate analysis (analysis done on single variable)and bivariate analysis (analysis done on 2 variables)