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

'''
Take item
Check condition
If True → add to list
If False → skip
'''

#old way
evens = []

for i in range(1,11):
    if i % 2 == 0:
        evens.append(i)

print(evens)

#List comprehension with condition
'''[new_value for item in iterable if condition]'''
evens= [i for i in range(1,11) if i%2 == 0]
print("print evens",evens)

odds = [i for i in  range(1,11) if i%2 != 0]
print("print odds",odds)

#======================================================================
#long names
names = ["Vipin","AI","Python","ML"]
long_names = [ch for ch in names if len(ch)>3]
print("long_name",long_names)
#======================================================================
'''Output Prediction Questions'''

nums = [i for i in range(1,6) if i > 3]
print(nums)
#[4,5]

nums = [i for i in range(1,11) if i % 2 == 0]
print(nums)
#[2, 4, 6, 8, 10]

nums = [i for i in range(1,11) if i % 2 != 0]
print(nums)
#[1, 3, 5, 7, 9]

names = ["AI","Python","ML","Docker"]
result = [name for name in names if len(name) > 2]
print(result)
#['Python', 'Docker']

letters = [ch for ch in "python" if ch != "o"]
print(letters)
#['p', 'y', 't', 'h', 'n']
'''=========================================================================================='''
#============================================================================================

'''Practice 1:-
Create a list of all even numbers from 1–20 using list comprehension'''

even =[i for i in range(1,20) if i  %  2 ==0]
print("even numbers:- ", even)
#=====================================================================================
'''practice 2:-
Create a list of all odd numbers from 1–15.'''

odd = [i for i in range(1,15) if i % 2 != 0]
print("odd numbers:- ", odd)
#=====================================================================================
''' practice 3:-
Create a new list containing only names whose length is greater than 2.'''

names = ["AI","Python","ML","Docker","Go"]
result = [ch for ch in names if len(ch) > 2]
print(result)
#======================================================================================
'''Mini-challenge'''
'''
Create:     [25,36,49,64,81,100]
using one list comprehension.
'''

result = [i*i for i in range(5,11)]
print(result)
#======================================================================================

#q6:- i  %  2 ==0
#Q7:- if part
#Q8:- True
#Q9:- Filtering Data
#q10 :- List comprehension



































































