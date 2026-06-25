'''
Definition:-

A List is a collection of multiple values stored in a single variable.
'''

#Creating Lists
#Integer List
nums = [10, 20, 30, 40]

#String List
names = ["Vipin", "Rahul", "Aman"]

#Mixed List
data = ["Vipin", 25, True, 99.5]
#========================================================================================

#Visual Understanding
names = ["Vipin", "Rahul", "Aman", "Neha"]

#Memory view:
'''
Index:   0        1        2       3

        --------------------------------
names = | Vipin | Rahul | Aman | Neha |
        --------------------------------
'''
#===========================================================================================

names = ["Vipin", "Rahul", "Aman", "Neha"]

print(names[0])
#Vipin

'''
| Value | Negative Index |
| ----- | -------------- |
| Neha  | -1             |
| Aman  | -2             |
| Rahul | -3             |
| Vipin | -4             |

'''
print(names[-1])
#Neha

List1=["Python", "Java", "C++", "Go"]
print(List1[1],List1[3]) #Java Go
#=============================================================================
#Mini Challenge

#Create a list of your favorite 5 technologies.

tech = ["Python", "Git", "Linux", "Docker", "AI"]
print('First Technology:-',tech[0])
print('Last Technology:-',tech[-1])
#=========================================================================
'''
List Traversal (VERY IMPORTANT)
'''
'''What is Traversal?
Traversal means:

Visiting every element of a list one by one.
'''
nums = [10, 20, 30]

#Traversal means:
'''
Visit 10
Visit 20
Visit 30
'''
#====================================================================================================
'''=========================================Using for Loop==========================================='''
#====================================================================================================

numbers = [10, 20, 30, 40]
for num in numbers:
    print(num)
#10 20 30 40

#====================================================================================================
'''=========================================Using while Loop==========================================='''
#====================================================================================================
numbers = [10, 20, 30, 40]
i=0
while i<len(numbers):
    print(numbers[i])
    i=i+1
#10 20 30 40
#=============================================================================================
#=============================================================================================
#practice

nums = [10,20]
for x in nums:
    print(x * 2)
#20,40

nums = [5,6,7]
for x in nums:
    print(x + 1)

nums = [100,200,300]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1
#100 200 300


nums = [2,4,6]
for x in nums:
    print(x * x)
#4 ,16,36
#==================================================================================
#practice 1
nums = [10,20,30,40,50]
for x in nums:
    print(x)
#10 20 30 40 50

#practice 2
fruits = ["apple","mango","banana"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1
#apple mango banana
#=================================================================================================
#Practice 3
nums = [1,2,3,4,5]
i=0
while i<len(nums):
    result=nums[i]*2
    print(result)
    i=i+1
#2 4 6 8 10
#================================================================================================
#Mini Challenge:-
marks = [70,80,90,60,50]
total =0
for x in marks:
    print(x)
    total= x+total
print("Total:-",total)
#70 80 90 60 50 , Total:-350






























































