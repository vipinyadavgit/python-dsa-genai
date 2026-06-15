'''
Definition

A list that contains other lists.
'''
#Example
students = [
    ["Vipin", 90],
    ["Rahul", 85],
    ["Aman", 95]
]

print(students[0])
#['Vipin', 90]

'''accessing inner element'''
print(students[0][0])
#Vipin
print(students[0][1])
#90

#==========================================================

#Nested List as Matrix

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0])
#[1, 2, 3]
print(matrix[1])
#[4, 5, 6]
print(matrix[0][0])
# 1
print(matrix[0][1])
#   2
print(matrix[2][1])
# 8

#============================================================================
#prediction questions
students = [
    ["Vipin",90],
    ["Rahul",85]
]
print(students[0])
#   ['Vipin', 90]


students = [
    ["Vipin",90],
    ["Rahul",85]
]
print(students[1][0])
#Rahul


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][2])
#   6

matrix = [
    [1,2],
    [3,4]
]
print(matrix[0][1])
#   2

data = [
    ["Python",100],
    ["Java",200]
]
print(data[1][1])
#   200

#================================================================================
'''Practice 1'''
students = [
    ["Vipin",90],
    ["Rahul",85],
    ["Aman",95]
]
#print:- vipin
print(students[0][0])
#Vipin
#========================================================================
'''Practice 2'''
matrix = [
    [10,20],
    [30,40]
]
print(matrix[1][1])
#40
#=======================================================================
'''practice 3'''
languages = [
    ["Python","AI"],
    ["Java","Spring"]
]

print(languages[1][1])
#Spring
#=======================================================================
#Mini challenge
employees = [
    [101,"Vipin",50000],
    [102,"Rahul",60000],
    [103,"Aman",70000]
]

print(employees[0][1])
print(employees[1][2])
print(employees[2][0])

#Vipin
#60000
#103

























































































































































































