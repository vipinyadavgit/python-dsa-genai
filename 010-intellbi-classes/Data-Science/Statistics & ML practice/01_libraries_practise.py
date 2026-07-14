
#1. Basic line plot
print("Basic line plot")
import matplotlib.pyplot as plt

months = ["jan","feb","mar","apr","may","jun","jul"]
sales = [100,200,150,250,200,170,100]
plt.plot(months,sales)

plt.xlabel("months")
plt.ylabel("sales ")
plt.title("sales report")
plt.show()

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

#2. Bar chart: it is used for comparing categories
print("Bar chart: it is used for comparing categories")
products = ["Phone", "Laptop", "Tablet", "TV"]
revenue = [1000, 1500, 800, 1200]

plt.bar(products,revenue)
plt.xlabel("products")
plt.ylabel("revenue ")
plt.title("sales report")

plt.show()
#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

#3. Horizontal bar chart
print("Horizontal Bar chart")
products = ["Phone", "Laptop", "Tablet", "TV"]
revenue = [1000, 1500, 800, 1200]

plt.barh(products,revenue)
plt.xlabel("revenue")
plt.ylabel("products ")
plt.title("sales report")

plt.show()

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

#4.## Scatter plot: It plots the coordinates, and is useful for understanding the relationship between variables

print("Scatter plot: It plots the coordinates, and is useful for understanding the relationship between variables")
study_hours = [10, 12, 8,6, 7]
marks = [40,38,12,16, 20]

plt.scatter(study_hours,marks)
plt.xlabel("study hours")
plt.ylabel("marks")
plt.title("Study Time vs Marks")

plt.show()
#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

#5. # Histogram:- Used for frequency distribution curve of data.
print("Histogram plot:-Used for frequency distribution curve of data.")

age = [20, 12, 16, 17, 19, 20, 21, 24, 16, 17]

plt.hist(age,bins= 5)
plt.xlabel("age")
plt.ylabel("count")
plt.title("age distribution using histogram")

plt.show()

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

#6. ## Pie chart =(shows percentage contribution)
categories = ["food", "rent", "travel", "shopping"]
expenses = [5000, 15000, 20000, 3000]

plt.pie(expenses,labels=categories,autopct="%2.2f%%")
plt.title("expenses distribution using pie")
plt.show()

