'''
in
not in
index()
count()
membership testing
manual search using loops
'''
from unittest import result

from pip._internal.commands import index

#==========================================================================
'''
index()
↓
Where is it?

count()
↓
How many are there?
'''
#==========================================================================
'''
In real projects, interviews, DSA, APIs, and AI work, you constantly need to answer questions like:

Is this value present?
How many times is it present?
Where is it present?
'''
#=========================================================================

#   in

nums = [10,20,30,40]
print(20 in nums)
#true

nums = [10,20,30,40]
print(50 in nums)
#False
#===========================================================================

#   not in
nums = [10,20,30]
print(50 not in nums)
#true
#===========================================================================

#   index()
#Returns the position (index) of a value.

nums = [10,20,30,40]
print(nums.index(30))
#2
#===========================================================================

#   count()
#Counts how many times a value appears.

nums = [10,20,20,30,20]
print(nums.count(20))
#3
#==========================================================================

#Manual Search Using Loop
#Very important for DSA.

nums = [10,20,30,40]
found = False

for i in nums:
    if i == 20:
        found = True
print(found)
#True
#==============================================================================

'''Output Prediction Questions'''

nums = [10,20,30]
print(20 in nums)
#True

nums = [10,20,30]
print(50 in nums)
#False

nums = [10,20,30]
print(20 not in nums)
#False

nums = [5,10,15,20]
print(nums.index(15))
#2

nums = [1,2,2,2,3]
print(nums.count(2))
#3
#========================================================================
'''Practice 1'''
skills = ["Python","Git","Linux"]
print("Git" in skills)
#True

'''Practice 2'''
nums = [10,20,30,40]
print(nums.index(40))
#3

'''Practice 3'''
marks = [90,80,90,70,90]
print(marks.count(90))
#3

# '''Mini Challenge'''
# employees = ["Vipin","Rahul","Aman","Neha"]
# employee= input("Enter employee name: ")
# if employee in employees:
#         print(employee,"Employee found")
# else:
#         print(employee,"Employee not found")

#2nd approach
employees = ["Vipin","Rahul","Aman","Neha"]
employee= input("Enter employee name: ")
for i in employees:
    if i == employee:
        print(employee,"Employee found")
        break
    else:
        print(employee,"Employee not found")
#==============================================================================
#Q6:- in
#Q7:- not in
#Q8:- how many times 10 is present
#Q9:- Loop




































































































































































































