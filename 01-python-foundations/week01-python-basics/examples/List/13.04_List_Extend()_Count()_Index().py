#extend()

#Definition:-
"""Adds multiple elements from another iterable to a list."""
from itertools import count

#   Adds MULTIPLE items.
#extend()
nums = [10,20]
nums.extend([30,40,50])
print(nums)

#==============================================================================

#   Interview Favorite
#   append vs extend

#==>    Using Append() we can add single value at a time, and it gets added at the end.
#==>    Using Extend() we can add multiple values.

nums = [10,20]
nums.extend([30,40])
print(nums)

#[10, 20, 30, 40]
#================================================================================

#   count()
'''
count()
Definition:-    Counts how many times a value appears.
'''

#Syntax==>  list_name.count(value)

nums = [10,20,10,30,10]
print(nums.count(10))

#3

#===================================================================================

#index()

'''
Definition:- Returns the position (index) of first occurrence.
'''

#example:-
nums = [10,20,30]
print(nums.index(20))

#1

#example:-
nums = [10,20,10,30]
print(nums.index(10))

#0
'''Returns the index of the first occurrence.'''
#==================================================================================

#Practice 1
nums = [10,20]
#Use extend() to add: Use extend() to add:
nums.extend([30,40,50])
print(nums)

#[10, 20, 30, 40, 50]
#==================================================================================

#Practice 2
marks = [90,80,90,70,90]
#Print how many times:90
print(marks.count(90))

#3
#=================================================================================

# practice 3
fruits = ["apple","banana","mango"]
print(fruits.index("mango"))

#2
#==================================================================================

#Mini Challenge
tech = ["Python","AI"]

tech.extend(["Git","Linux","Docker"])
print(tech)

print(tech.count("Python"))


print(tech.index("Docker"))
print(tech)





















































































