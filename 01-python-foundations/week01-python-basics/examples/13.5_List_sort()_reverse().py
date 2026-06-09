"""sort() and reverse()"""

#sort()
#Definition:-    Sorts a list in ascending order by default

nums = [40,10,30,20]
nums.sort()

print(nums)
#10, 20, 30, 40]
#===========================================================

'''Descending Order'''

nums = [40,10,30,20]
nums.reverse()
print(nums)

#[20, 30, 10, 40] it will just reverse the list but not ordered in descending order
#OR

nums = [40,10,30,20]
nums.sort(reverse=True)
print(nums)

#[40, 30, 20, 10]

#========================================================================================

'''Sorting Strings'''

fruits = ["mango","apple","banana"]
fruits.sort()
print(fruits)

#['apple', 'banana', 'mango']

#=======================================================================================
#reverse()

'''
reverse()
Definition:-    Reverses current order of list.
'''

nums = [10,20,30,40,50,60,70,80]
nums.reverse()

print(nums)
#[80, 70, 60, 50, 40, 30, 20, 10]
#=======================================================================================

#<==>   sort(reverse=True):- This will return sorted descending order of a list

#<==>   reverse():-     it just simply reverse the list,(unsorted)

#=======================================================================================

fruits = ["mango","apple","banana"]
fruits.sort()

print(fruits)
#
#=======================================================================================
#practice 1
nums = [50,10,40,20,30]
nums.sort()
print(nums)

#[10, 20, 30, 40, 50]

#=======================================================================================
#practice 2
nums = [50,10,40,20,30]
nums.sort(reverse=True)
print(nums)

#[50, 40, 30, 20, 10]
#=======================================================================================

#practice 3
colors = ["Red","Blue","Green"]
colors.reverse()
print(colors)

#['Green', 'Blue', 'Red']
#=======================================================================================

#Mini Challenge
marks = [78,92,65,88,70]
'''
Sort ascending
Print list
Sort descending
Print list
Reverse current list
Print list
'''
marks.sort()
print("ascending sorted list",marks)

marks.sort(reverse=True)
print("descending sorted list",marks)

marks.reverse()
print("reversed list",marks)

#=======================================================================================























































































































