matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#Traversing rows
for row in matrix:
    print(row)
#[1, 2, 3]
#[4, 5, 6]
#[7, 8, 9]

#Traversing every element in matrix
for row in matrix:
    for value in row:
        print(value)
'''
1 2 3 4 5 6 7 8 9'''

#==============================================================================
'''Printing Matrix Properly

Instead of vertical output:'''

for row in matrix:
    for value in row:
        print(value,end= ' ')
    print()
#1 2 3
#4 5 6
#7 8 9
#===============================================================================
#Output Prediction Questions

#Q1
matrix = [
    [1,2],
    [3,4]
]

for row in matrix:
    print(row)

#[1,2]
#[3,4]
#=========================================
#Q2
matrix = [
    [1,2],
    [3,4]
]

for row in matrix:
    for value in row:
        print(value)
#1 2 3 4
#==========================================

#Q3
matrix = [
    [10,20],
    [30,40]
]

for row in matrix:
    for value in row:
        print(value,end=" ")
#10 20 30 40
#==========================================
matrix = [
    [1,2,3]
]

for row in matrix:
    for value in row:
        print(value)
#1
#2
#3
#==========================================
matrix = [
    [5],
    [10]
]

for row in matrix:
    print(row)
#[5]
#[10]
#======================================================================================
'''Practice 1'''
matrix = [
    [1,2],
    [3,4]
]
for row in matrix:
    print(row)
#[1, 2]
#[3, 4]
#========================================================================================
'''Practice 2'''
matrix = [
    [1,2],
    [3,4]
]

for row in matrix:
    for value in row:
        print(value)

#========================================================================================
'''Practice 3'''
matrix = [
    [10,20],
    [30,40]
]

for row in matrix:
    for value in row:
        print(value,end=" ")
    print()
#========================================================================================
'''mini chanllenge'''
students = [
    ["Vipin",90],
    ["Rahul",85],
    ["Aman",95]
]
for row in students:
    for value in row:
        print(value)


























































































































