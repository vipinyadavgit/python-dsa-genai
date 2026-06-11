'''
Definition
List Comprehension:-

A concise (short) way to create lists using a single line of code.
'''

#syntax
'''[new value for item in itrable]'''

'''
Read it as:

Take item
Create new_value
Put into list
Repeat for all items
'''
#=================================================================================
#Example 1
#Normal loop:

nums = []
for i in range(1,6):
    nums.append(i)
print(nums)

# Output:
# [1,2,3,4,5]

#List Comprehension
num = [i for i in range(1,6)]
print(num)
'''[new value for item in itrable]'''
#================================================================================

#Example 2

squares = []

for i in range(1,6):
    squares.append(i*i)

#List comprehension
squares = [i*i for i in range(1,6)]
print(squares)
#[1, 4, 9, 16, 25]
#==============================================================================

#Example 3
'''[new value for item in itrable]'''
letter = [ch for ch in 'python']
print(letter)
#['p', 'y', 't', 'h', 'o', 'n']

#==============================================================================

'''practice 1'''
list = [i for i in range(1,6)]
print(list)

#or

list=[]
for i in range(1,6):
    list.append(i)
print(list)

#[1, 2, 3, 4, 5]
#==============================================================
'''practice 2'''

list=[i for i in range(10,60,10)]
print(list)

#[10, 20, 30, 40, 50]
#==============================================================
'''practice 3'''


name = "vipin"
list=[ch for ch in name]
print(list)

#===============================================================
'''mini challenge'''

list = [i for i in range(2,11,2)]
print(list)

#=======================================================================================
'''====================================================================================='''

'''List Comprehension with Conditions'''

#syntax
'''[new value for item in iteratble if condition]'''




















































































