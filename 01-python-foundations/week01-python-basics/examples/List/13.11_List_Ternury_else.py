'''
Advanced List Comprehension
'''
from reportlab.lib.pagesizes import elevenSeventeen

#Now we'll combine Ternary Operator + List Comprehension.
#This allows us to transform data while creating a list.

'''
Definition:-       Advanced List Comprehension

A list comprehension that uses an if-else expression to decide what value should be added to the list.
'''

#Syntax
'''[value_if_true if condition else value_if_false for item in iterable]'''

#read it as
'''
For each item:
    check condition

    if True:
        add value_if_true

    else:
        add value_if_false
'''

#Example 1:-
'''
Normal way:

result = []

for i in range(1,6):
    if i % 2 == 0:
        result.append("Even")
    else:
        result.append("Odd")

print(result)
'''

#List Comprehension:
'''[value_if_true if condition else value_if_false for item in iterable]'''

result = [i if i%2 == 0 else "odd"
          for i in range(1,11) ]
print(result)
#['odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd', 10]

#=====================================================================================================
'''Example 2 — Pass/Fail'''

marks = [35,80,25,90]

result =["pass" if i>=40 else "fail" for i in marks]
print("results:- ",result)

#=====================================================================================================
'''Example 3 — Uppercase/Lowercase'''
word = "PythON"

result = [ch.lower() if ch.isupper else ch.upper()
          for ch in word ]
print("word:- ",result)

#===================================================================================================
'''Output Prediction Questions'''
#Q1
result = [
    "Even" if i % 2 == 0 else "Odd"
    for i in range(1,4)
]

print(result)
#['Odd', 'Even', 'Odd']
#====================================================================================================
#Q2;-
marks = [20,50,80]

result = [
    "Pass" if m >= 40 else "Fail"
    for m in marks
]

print(result)
#['Fail', 'Pass', 'Pass']
#=====================================================================================================
#Q3
result = [
    i*10 if i > 2 else i
    for i in range(1,5)
]

print(result)
#[1, 2, 30, 40]
#=====================================================================================================
#Q4
word = "AI"

result = [
    ch.lower()
    if ch.isupper()
    else ch.upper()
    for ch in word
]

print(result)
#['a', 'i']
#=====================================================================================================
#Q5
nums = [1,2,3]

result = [
    "Yes" if i == 2 else "No"
    for i in nums
]

print(result)
#['No', 'Yes', 'No']
#====================================================================================================
'''Practice 1'''
#create
'''['Small', 'Small', 'Big', 'Big', 'Big']'''

result = ["Small" if i<=2 else "Big" for i in range (1,6)]
print(result)
#['Small', 'Small', 'Big', 'Big', 'Big']

#==============================================================================================
'''Practice 2'''
'''Expected ['Pass','Pass','Fail','Pass','Fail']'''
marks = [95,60,35,80,20]

result = ["pass" if i>=40 else "fail" for i in marks]
print(result)
#['pass', 'pass', 'fail', 'pass', 'fail']

#==============================================================================================
'''Practice 3'''
word = "python"
result = [ch.upper() if ch.islower() else word.upper() for ch in word]
print(result)
#['P', 'Y', 'T', 'H', 'O', 'N']

#==============================================================================================
'''Mini Challenge'''
nums = [1,2,3,4,5,6]
result = ["even" if i%2==0 else "odd" for i in nums]
print(result)
#['odd', 'even', 'odd', 'even', 'odd', 'even']

#Q6:- "==" assignent operator, actually question is not clear what you are trying to ask.
#Q7:- True
#Q8:- condition check
#Q9:- Yes
#Q10:- advance list comprehension
























































































