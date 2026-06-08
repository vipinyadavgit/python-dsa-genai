#Updating Lists + append() + insert()
'''
Updating Existing Values
'''

nums = [10,20,30]
#updating
nums[0] = 100
nums[1] = 200
nums[2] = 300

print(nums)
#[100, 200, 300]
#==================================================================================
'''
append()
=========
Definition:-
Adds a new element at the end of the list.
'''
#==========================================================================================
'''
Syntax:-
list_name.append(value)
'''

nums = [10,20,30]
nums.append(40)
print(nums)
#[10,20,30,40]
#===========================================================================================
'''
insert()
Definition:-
Inserts a new element at the end of the list.
Adds an element at a specific position.
'''
'''
Syntax:-
list_name.insert(index, value)
'''
nums = [10,30,40]
nums.insert(1,20)
print(nums)
#[10, 20, 30, 40]
#============================================================================================
'''
| Method   | Where Adds? |
| -------- | ----------- |
| append() | End         |
| insert() | Any Index   |
'''
#============================================================================================
'''Practice 1'''
nums = [10,20,30]
nums.append(40)
print(nums)
'''=========================================================================================='''
'''Practice 2'''
names = ["Vipin","Aman"]
names.insert(1,"Rahul")
print(names)
'''============================================================================================='''
'''Practice 3'''
prices = [100,200,300]
prices[1]=250
print(prices)
#=================================================================================================
#Mini Challenge
#tech = ["Python","Git","Linux"]
'''
Perform all:-
Append "Docker"
Insert "AI" at index 1
Update "Linux" to "Ubuntu"
'''
tech = ["Python","Git","Linux"]
#Append "Docker"
tech.append("Docker")
print(tech)

tech.insert(1,"AI")
print(tech)

tech[3]="Ubuntu"
print(tech)
'''========================================================================================='''
#==============================================================================================

















