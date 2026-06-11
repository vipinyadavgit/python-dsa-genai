#Slicing:-
'''
Definition
Slicing means:  Extracting a portion (part) of a list.
'''
#=============================================================
'''
Basic Syntax:-
            list[start:end]

Remember:
            start = included
            end = excluded
'''
#==============================================================

nums = [10,20,30,40,50]

print(nums[1:4])

#[20,30,40]

#===============================================================

'''Slicing From Beginning'''
print(nums[:4])

#[10, 20, 30, 40]
#===============================================================

'''Slicing To End'''
print(nums[4:])

#Meaning:   nums[2:len(nums)]

#[30,40,50]
#===============================================================

'''Entire List'''
print(nums[:])
#[10, 20, 30, 40, 50]

#Creates a shallow copy.

#=============================================================
#Step Slicing
'''
Step Slicing:-

Syntax:-     list[start:end:step]
'''
nums = [10,20,30,40,50,60]

print(nums[::2])
#Take every 2nd element.

#[10, 30, 50]

#============================================================================
#Reverse Using Slicing
'''
Reverse Using Slicing:-

'''
nums = [10,20,30,40,50,60]
print(nums[::-1])

#[60, 50, 40, 30, 20, 10]

#==============================================================================
#prediction questions
nums = [10,20,30,40,50]
print(nums[1:4])
#[20,30,40]

nums = [10,20,30,40,50]
print(nums[:3])
#[10, 20, 30]


nums = [10,20,30,40,50]
print(nums[2:])
#[30, 40, 50]

nums = [10,20,30,40,50]
print(nums[::2])
#[10, 30, 50]

nums = [10,20,30,40]
print(nums[::-1])
#[40, 30, 20, 10]

#==========================================================================
'''practice questions'''
#P1
nums = [1,2,3,4,5,6]
print(nums[1:4])
#[2, 3, 4]

#p2
fruits = ["apple","banana","mango","orange"]
print(fruits[:2])
#['apple', 'banana']

#p3
tech = ["Python","AI","Git","Linux","Docker"]
print(tech[2:])
#['Git', 'Linux', 'Docker']

#Mini challenge
nums = [10,20,30,40,50,60,70]
print(nums[:3])
print(nums[4:])
print(nums[::2])
print(nums[::-1])

#[10, 20, 30]
#[50, 60, 70]
#[10, 30, 50, 70]
#[70, 60, 50, 40, 30, 20, 10]

#=============================================================================



























































































































































