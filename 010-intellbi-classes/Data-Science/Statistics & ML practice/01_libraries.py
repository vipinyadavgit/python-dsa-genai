## Basic line plot

print("Basic line plot")
import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "June"]
sales = [100, 120, 80, 95, 110]

plt.plot(months, sales)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Report")
plt.show()
#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

## Bar chart: it is used for comparing categories
print("Bar chart: it is used for comparing categories")
products = ["Phone", "Laptop", "Tablet", "TV"]
revenue = [1000, 1500, 800, 1200]

plt.bar(products, revenue)
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.title("Quarterly Revenue Report")
plt.show()

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

## Bar chart(Horizontal): it is used for comparing categories
print("Bar chart(Horizontal): it is used for comparing categories")

products = ["Phone", "Laptop", "Tablet", "TV"]
revenue = [1000, 1500, 800, 1200]

plt.barh(products, revenue)
# barh for horizontal

plt.xlabel("Products")
plt.ylabel("Revenue")
plt.title("Quarterly Revenue Report")
plt.show()

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

## Scatter plot: It plots the coordinates, and is useful for understanding the relationship between variables

print("Scatter plot: It plots the coordinates, and is useful for understanding the relationship between variables")
study_hours = [10, 12, 8,6, 7]
marks = [40,38,12,16, 20]

plt.scatter(study_hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Time vs Marks")
plt.show()

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

# Histogram:- Used for frequency distribution curve of data.

age = [20, 12, 16, 17, 19, 20, 21, 24, 16, 17]
plt.hist(age, bins= 8)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution using Histogram")
plt.show()

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================
## Pie chart

categories = ["food", "rent", "travel", "shopping"]
expenses = [5000, 15000, 20000, 3000]
plt.pie(expenses,labels=categories,autopct='%2.2f%%')
plt.title("Expenses of category")


























































