# 🐼 PANDAS ROADMAP - Complete Learning Guide for GenAI Developers

**Duration:** 4 Weeks | **Level:** Total Beginner → Intermediate  
**Goal:** Master Pandas for data preprocessing, cleaning, and GenAI dataset preparation

---

## 📌 Why Pandas for GenAI Developers?

Pandas is essential for GenAI development because:
- **Data Preprocessing:** Clean and prepare datasets before training LLMs
- **EDA (Exploratory Data Analysis):** Understand your data before feeding to models
- **Feature Engineering:** Transform raw data into ML-ready features
- **Dataset Management:** Handle CSV, JSON, and Parquet files efficiently
- **Interview Ready:** 90% of DS/ML interviews include pandas questions

---

## 🎯 WEEK 1: PANDAS FUNDAMENTALS (BEGINNER)
**Focus:** Understanding core concepts  
**Time:** 15-20 hours  
**Reference:** `pandas/getting_started/intro_tutorials/` & `10min.html`

### Topics to Master:

#### 1. **Installation & Setup** (1 hour)
- Install pandas: `pip install pandas`
- Import: `import pandas as pd`
- Verify installation: `pd.__version__`
- IDE setup (Jupyter Notebook or VS Code)

#### 2. **Series Basics** (2 hours)
- Creating a Series from list, dict, scalar
- Series index and values
- Series data types
- Accessing elements (by index, position)
- Series operations (arithmetic, comparison)

#### 3. **DataFrame Creation** (2 hours)
- Creating DataFrames from dict, list, arrays
- Creating from CSV files
- Creating from JSON
- Understanding rows and columns
- Viewing structure: `shape`, `columns`, `index`

#### 4. **Data Types in Pandas** (1.5 hours)
- int64, float64, object, bool, datetime64
- Checking data types: `dtypes`, `info()`
- Type casting basics

#### 5. **Reading Data Files** (2 hours)
- `pd.read_csv()` - CSV files
- `pd.read_json()` - JSON files
- Parameters: `sep`, `header`, `dtype`, `nrows`
- Handling encoding issues

#### 6. **DataFrame Inspection** (2 hours)
- `head()`, `tail()` - preview data
- `info()` - data types and memory usage
- `describe()` - statistical summary
- `shape` - dimensions
- `columns` - column names
- `dtypes` - data types

#### 7. **Column Selection & Access** (2 hours)
- Accessing single column: `df['col']` or `df.col`
- Accessing multiple columns: `df[['col1', 'col2']]`
- Using dot notation
- DataFrame vs Series

#### 8. **Basic Indexing** (1.5 hours)
- Integer-location based: `df.iloc[0]`
- Label-based: `df.loc[0]`
- Row selection
- Chaining operations

### 📝 Practice Exercises (Week 1):
1. Load a CSV file and explore its structure
2. Create a Series and perform basic operations
3. Create a DataFrame manually and from a dictionary
4. Inspect and describe a real dataset (e.g., movies, weather)
5. Access specific rows and columns

### 🎓 Mini Project - Week 1:
**"Dataset Explorer"**
- Load any CSV dataset (Kaggle)
- Display basic info, summary statistics
- Access specific columns and rows
- Export findings to console

---

## 🎯 WEEK 2: DATA CLEANING & PREPROCESSING
**Focus:** Make messy data clean  
**Time:** 15-20 hours  
**Reference:** `user_guide/missing_data.html`, `duplicates.html`, `basics.html`

### Topics to Master:

#### 1. **Handling Missing Data** (3 hours)
- Understanding NaN (Not a Number)
- Detecting missing values: `isnull()`, `isna()`, `notnull()`
- Counting missing values: `sum()`, `count()`
- Removing missing data: `dropna()`
  - By rows: `dropna(axis=0)`
  - By columns: `dropna(axis=1)`
  - Threshold: `dropna(thresh=n)`
- Filling missing data: `fillna()`
  - Forward fill: `fillna(method='ffill')`
  - Backward fill: `fillna(method='bfill')`
  - Mean/median: `fillna(df['col'].mean())`
  - Custom values: `fillna('Unknown')`

#### 2. **Removing Duplicates** (2 hours)
- Detecting duplicates: `duplicated()`
- Removing duplicates: `drop_duplicates()`
- Keep first/last/all: `keep='first'`, `keep='last'`, `keep=False`
- Subset of columns: `duplicated(subset=['col1', 'col2'])`

#### 3. **Data Type Conversion** (2 hours)
- Checking current types: `dtypes`
- Converting with `astype()`
- String to numeric: `pd.to_numeric()`
- String to datetime: `pd.to_datetime()`
- Categorical conversion: `astype('category')`

#### 4. **String Operations & Text Cleaning** (3 hours)
- `.str` accessor for string methods
- Uppercase/lowercase: `.str.upper()`, `.str.lower()`
- Strip whitespace: `.str.strip()`, `.str.lstrip()`, `.str.rstrip()`
- Replace patterns: `.str.replace()`
- Split strings: `.str.split()`
- Extract patterns: `.str.extract()`
- Contains check: `.str.contains()`

#### 5. **Datetime Parsing & Handling** (2 hours)
- Parsing strings to datetime: `pd.to_datetime()`
- Format specification: `format='%Y-%m-%d'`
- Extracting date components: `.dt.year`, `.dt.month`, `.dt.day`
- Time operations: `.dt.hour`, `.dt.minute`
- Timedeltas: difference between dates

#### 6. **Outlier Detection Basics** (2 hours)
- Statistical outliers: using mean ± std
- IQR method: interquartile range
- Removing/replacing outliers
- Visualization approaches

#### 7. **Data Normalization & Scaling** (1.5 hours)
- Min-Max normalization: `(x - min) / (max - min)`
- Standardization: `(x - mean) / std`
- Using sklearn: `StandardScaler`, `MinMaxScaler`

#### 8. **Reset & Rename Operations** (1.5 hours)
- Renaming columns: `rename()`
- Resetting index: `reset_index()`
- Setting index: `set_index()`
- Renaming axis: `rename(mapper={})`

### 📝 Practice Exercises (Week 2):
1. Load a messy dataset and handle missing values
2. Remove duplicate records
3. Clean text data (spaces, case, special chars)
4. Convert data types appropriately
5. Detect and handle outliers
6. Create a data cleaning pipeline

### 🎓 Mini Project - Week 2:
**"Data Cleaning Pipeline"**
- Load a messy dataset (with missing values, duplicates, bad formats)
- Apply all cleaning techniques learned
- Document before/after statistics
- Export cleaned data to CSV

---

## 🎯 WEEK 3: DATA ANALYSIS & TRANSFORMATION
**Focus:** Extract insights and reshape data  
**Time:** 15-20 hours  
**Reference:** `user_guide/indexing.html`, `groupby.html`, `merging.html`, `reshaping.html`

### Topics to Master:

#### 1. **Indexing Deep Dive** (2.5 hours)
- Label-based: `loc[]` 
  - Single row/column
  - Multiple selections
  - Range selections
  - Boolean indexing
- Integer-location: `iloc[]`
  - Row and column position
  - Slicing: `iloc[0:5, 1:3]`
  - Fancy indexing
- Single item access: `at[]`, `iat[]`

#### 2. **Boolean Indexing & Filtering** (2 hours)
- Creating boolean masks: `df['col'] > 5`
- Multiple conditions: `(df['col1'] > 5) & (df['col2'] == 'A')`
- Using `isin()`: `df['col'].isin([1, 2, 3])`
- Using `query()`: `df.query('col1 > 5 and col2 == "A"')`

#### 3. **GroupBy Operations** (3 hours)
- Basic groupby: `df.groupby('col')`
- Multiple groupby: `df.groupby(['col1', 'col2'])`
- Aggregation functions: `sum()`, `mean()`, `count()`, `min()`, `max()`, `std()`
- Custom aggregation: `agg({'col1': 'sum', 'col2': 'mean'})`
- Named aggregation: `agg(total=('col', 'sum'))`
- Filtering groups: `filter(lambda x: x['col'].sum() > 100)`
- Transformations: `transform()`

#### 4. **Merging DataFrames** (2.5 hours)
- `merge()` - SQL-style joins
  - Inner join (default)
  - Left/right/outer joins
  - Key parameter: `on`, `left_on`, `right_on`
  - Index joining: `left_index=True`
- `join()` - join on index
- `concat()` - concatenate
  - Row-wise: `axis=0` (default)
  - Column-wise: `axis=1`

#### 5. **Reshaping Data** (2.5 hours)
- `pivot()` - reshape with aggregation
- `pivot_table()` - pivot with aggregation functions
- `melt()` - unpivot (wide to long)
- `stack()` / `unstack()` - reshape via index
- Transpose: `.T`

#### 6. **Aggregations** (1.5 hours)
- Basic aggregations: `sum()`, `mean()`, `median()`, `std()`, `var()`
- Count operations: `count()`, `value_counts()`
- Percentiles: `quantile()`
- Custom functions: `agg(lambda x: x.max() - x.min())`

#### 7. **Sorting & Ranking** (1.5 hours)
- Sorting by columns: `sort_values()`
- Sorting by index: `sort_index()`
- Ascending/descending: `ascending=True/False`
- Multiple columns: `sort_values(by=['col1', 'col2'])`
- Ranking: `rank()`

#### 8. **Window Functions** (1.5 hours)
- Rolling windows: `rolling()`
- Expanding windows: `expanding()`
- Moving average: `rolling(window=7).mean()`
- Cumulative operations: `cumsum()`, `cumprod()`

### 📝 Practice Exercises (Week 3):
1. Filter data using multiple conditions
2. Group data and calculate statistics
3. Merge multiple datasets
4. Pivot a table and aggregate data
5. Reshape wide to long format
6. Sort and rank data

### 🎓 Mini Project - Week 3:
**"Sales Analysis Dashboard"** (or similar analytical project)
- Load sales data with dates, categories, amounts
- Filter by date range, category
- GroupBy category and calculate totals
- Create pivot tables
- Merge with product/customer data
- Generate summary statistics and insights
- Export reports

---

## 🎯 WEEK 4: GENAI DATA PREP & ADVANCED TOPICS
**Focus:** Optimize for ML/GenAI workflows  
**Time:** 15-20 hours  
**Reference:** `user_guide/scale.html`, `io.html`, `categorical.html`, `timeseries.html`

### Topics to Master:

#### 1. **Reading Large Datasets** (2 hours)
- Chunked reading: `chunksize` parameter in `read_csv()`
- Specifying dtypes: `dtype={'col': 'int32'}`
- Selecting columns: `usecols=['col1', 'col2']`
- Reading specific rows: `skiprows=[], nrows=1000`
- Memory optimization

#### 2. **Categorical Data Handling** (1.5 hours)
- Converting to categorical: `astype('category')`
- Advantages: memory savings, faster operations
- Removing unused categories: `cat.remove_unused_categories()`
- Ordering categories: `cat.set_categories()`
- Encoding for ML: `cat.codes`

#### 3. **Time Series Basics** (2 hours)
- Datetime index: `set_index(pd.to_datetime(df['date']))`
- Resampling: `resample('D').mean()` (daily aggregation)
- Frequency strings: 'D', 'M', 'Y', 'H', etc.
- Lag/shift: `shift()` for previous values
- Time-based indexing: `df['2023']`, `df['2023-01':'2023-03']`

#### 4. **Apply Functions** (2 hours)
- `apply()` - apply function to rows/columns
- `map()` - apply to Series
- Lambda functions: `df['col'].apply(lambda x: x * 2)`
- Custom functions
- Element-wise with `applymap()`
- Vectorized operations (preferred for performance)

#### 5. **Performance Optimization Tips** (2 hours)
- Use `category` dtype for repeated values
- Use `int32` instead of `int64` when possible
- Chunked processing for large files
- Using `eval()` for complex expressions
- Memory profiling: `memory_usage(deep=True)`
- Avoiding copies: `inplace=True` (carefully)

#### 6. **Export Data** (1.5 hours)
- CSV: `to_csv()`
- JSON: `to_json()`
- Excel: `to_excel()`
- Parquet: `to_parquet()` (efficient for ML)
- HDF5: `to_hdf()`
- Options: index, compression, etc.

#### 7. **Data Pipeline Creation** (2 hours)
- Creating reusable functions
- Chaining operations
- Error handling and logging
- Modular code structure
- Testing data quality

#### 8. **Real-World GenAI Dataset Prep** (2 hours)
- Preparing text data for LLMs
- Handling imbalanced data
- Creating train/test splits
- Data versioning
- Documenting data sources and transformations

### 📝 Practice Exercises (Week 4):
1. Read large CSV in chunks
2. Convert columns to categorical
3. Apply custom functions to data
4. Create time series from data
5. Export data in multiple formats
6. Build a complete data pipeline

### 🎓 Capstone Project - Week 4:
**"End-to-End Data Pipeline for GenAI"**
- Load raw dataset (messy, large)
- Clean and preprocess
- Handle missing/duplicate/outlier values
- Transform and aggregate data
- Create train/test split
- Export to Parquet format
- Document entire process
- Create reusable pipeline functions

---

## 📚 Learning Resources (In Your Zip):

- **Getting Started**: `/pandas/getting_started/`
- **10-Minute Guide**: `/pandas/10min.html`
- **User Guide**: `/pandas/user_guide/` (detailed reference)
- **Cookbook**: `/pandas/user_guide/cookbook.html` (practical examples)
- **API Reference**: `/pandas/reference/` (function documentation)

---

## 🎯 Interview Questions You'll Be Asked:

### Week 1 Level:
- What's the difference between Series and DataFrame?
- How do you read a CSV file?
- How do you access columns in a DataFrame?

### Week 2 Level:
- How do you handle missing values?
- How do you remove duplicates?
- How do you convert data types?

### Week 3 Level:
- How do you group data and aggregate?
- What's the difference between `merge()` and `join()`?
- How do you reshape data with `pivot()`?

### Week 4 Level:
- How do you handle large datasets efficiently?
- What's categorical data and why use it?
- How do you optimize pandas performance?
- How would you prepare data for an ML model?

---

## ✅ Progress Tracking:

Use your HTML tracker to mark topics as completed week by week!

- **Week 1:** Focus on fundamentals
- **Week 2:** Practice cleaning real messy data
- **Week 3:** Work with complex datasets
- **Week 4:** Build complete pipelines

---

## 🚀 Next Steps After Pandas:

1. **NumPy** - Numerical computing (parallel to pandas)
2. **Scikit-learn** - Machine learning (uses pandas)
3. **Data Visualization** - Matplotlib, Seaborn (visualize pandas data)
4. **SQL** - Query databases efficiently
5. **PySpark** - Big data processing (pandas on steroids)

---

## 💡 Pro Tips for Success:

✅ **Practice with real data** - Use Kaggle datasets  
✅ **Type along** - Don't just read, write code  
✅ **Build projects** - Apply learning immediately  
✅ **Refer to docs** - Pandas docs are excellent  
✅ **Join communities** - Stack Overflow, Reddit r/datascience  
✅ **Interview prep** - Practice LeetCode pandas problems  

---

**Happy Learning! 🐼📊**
