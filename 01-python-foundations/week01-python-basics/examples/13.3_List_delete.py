"""
remove()
pop()
clear()
del
"""
#================================================================

#remove()   :- 'Removes a specific value from a list.'
'''works with VALUE. Not index.'''

#Syntax:-    '''list_name.remove(value)'''

fruits = ["apple", "banana", "mango"]
fruits.remove("banana")
print(fruits)

#['apple', 'mango']
#================================================================

#pop():-

'''
Definition:-
Removes element using INDEX. Also returns the removed value.
'''

#Syntax :-  list_name.pop(index)

nums = [10,20,30,40]
nums.pop(1)
print(nums)

#[10, 30, 40]
#=================================================================

#pop():-

'''
pop() Without Index:- If index is omitted:
removes the LAST element.
'''

nums = [10,20,30]
nums.pop()
print(nums)
#[10, 20]
#=================================================================

# clear()

'''
Definition:- Removes ALL elements.
'''
nums = [10,20,30]
nums.clear()
print(nums)

#[]
#==================================================================

#del function
'''
Definition:- Deletes element OR whole list.
'''

#   you can delete an element using index value.
#   you can delete entire list also.

#Delete One Element
nums = [10,20,30,40]
del nums[1]
print(nums)

#Delete Entire List
nums = [10,20,30]
del nums

'''
Interview Question
remove()                    vs              pop()
remove()	                                pop()
Uses Value	                                Uses Index
Doesn't return removed value	            Returns removed value
remove("apple")	                            pop(2)
'''
#=================================================================================

#Output Prediction Questions
#Q1

nums = [10,20,30]
nums.remove(20)
print(nums)

#[10,30]
#==============================================================
#Q2
nums = [10,20,30]
nums.pop()
print(nums)

#[10,20]
#==============================================================
#Q3
nums = [1,2,3,4]
nums.pop(2)
print(nums)

#[1,2,4]
#==============================================================

#Q4:-
nums = [100,200]
nums.clear()
print(nums)
#==============================================================
#Q5:-

fruits = ["apple","banana","mango"]
removed = fruits.pop(1)
print(removed)

#["apple",'mango']
#==============================================================

#practice 1

nums = [10,20,30,40]
nums.remove(30)
print(nums)

#==================================================================
#practice 2

names = ["Vipin","Rahul","Aman"]
names.pop(1)
print(names)
#==================================================================
#practice 3

colors = ["Red","Blue","Green"]
colors.clear()
print(colors)
#===================================================================

#mini challenge

tasks = ["Study","Exercise","Coding","Sleep"]

#Remove "Exercise" using remove()
tasks.remove(tasks[1])
print(tasks)

#Remove last item using pop() AND Print removed item
remove = tasks.pop()
print(remove)

#Print final list
print(tasks)

nums = [10]
nums.pop()
print(nums)

















