'''
Level 1 — Warm-up (Easy)
Q1 — Find the Largest Number
nums = [10, 45, 23, 99, 12]

Without using max(), print:
#99
'''
from itertools import count

nums = [10, 45, 23, 99, 12]
max_num =   nums[0]
for num in nums:
    if num > max_num:
        max_num = num
print(max_num)
print("===============================================================")
print("===================Another approach============================")
nums = [10, 45, 23, 99, 12]
nums.sort()
print(nums[-1])
print("=================================================================")
#=============================================================================
'''
Q2 — Find the Smallest Number ⭐⭐
nums = [10, 45, 23, 99, 12]

Without using min(), print:
'''

nums = [10, 45, 23, 99, 12]
nums.sort()
print(nums[0])

print("============================Another approach======================================")

nums = [10, 45, 23, 99, 12]
small_num = nums[0]
for num in nums:
    if num < small_num:
        small_num = num
print(small_num)
print("==================================================================================")
#==========================================================================================
'''
Q3 — Count Even Numbers ⭐
nums = [1,2,3,4,5,6,7,8]
'''
nums = [1,2,3,4,5,6,7,8]
count = 0
for num in nums:
    if num % 2 == 0:
        print("even", num)
        count=count+1
print(count)
print("============================================================================")
#===================================================================================

'''
Q4 — Count Odd Numbers ⭐
nums = [1,2,3,4,5,6,7,8]
'''
nums = [1,2,3,4,5,6,7,8]
count = 0
for num in nums:
    if num % 2 != 0:
        print("odd", num)
        count+=1
print(count)
print("=============================================================================")
#=====================================================================================
'''
Q5 — Sum of All Elements ⭐⭐
nums = [10,20,30,40]
'''
nums = [10,20,30,40]
sum =0
for num in nums:
    sum=sum+num
print("sum" ,sum)
print("=============================================================================")
#====================================================================================
'''
Level 2 — Logic Building

Q6 — Find the Second Largest Number ⭐⭐⭐
nums = [10,45,23,99,12]

Output:-45

Rules:-
Don't use sort()
Don't use max()
'''
nums = [10,45,23,99,12]
largest_num = nums[0]
second_largest = nums[0]
for num in nums:
    if num>largest_num:
        largest_num = num
print("Largest number",largest_num)
for num in nums:
    if num>second_largest and num !=largest_num:
        second_largest = num
print("Second largest",second_largest)
print("================================================================================================================")
#===========================================================================================================================
'''
Q7 Remove Duplicates ⭐⭐⭐

nums = [1,2,2,3,4,4,5,1]
Output:-    [1,2,3,4,5]

Rule:-
Don't use set().
'''
nums = [1,2,2,3,4,4,5,1]
new_nums = []
for i in range(len(nums)):
    for j in range(i):
        if nums[i]==nums[j]:
            break
    else:
        new_nums.append(nums[i])
print(new_nums)
print("========================================Another Approach=========================================")
#=======================================================================================================================
nums = [1,2,2,3,4,4,5,1]
new_nums = []
for num in nums:
    if num not in new_nums:
        new_nums.append(num)

print(new_nums)
print("=================================================================================================")
#=======================================================================================================================
'''
Frequency Counter ⭐⭐⭐
nums = [1,2,2,3,3,3,4]

Expected Output:-
1 -> 1
2 -> 2
3 -> 3
4 -> 1
'''
nums = [1,2,2,3,3,3,4]

for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
    if nums[i] not in nums[:i]:
        print(nums[i], "->", count)

nums = [1, 2, 2, 3, 3, 3, 4]
visited = []
for i in range(len(nums)):
    if i not in visited:
        count = 0
        for j in range(len(nums)):
            if i == j:
                count += 1
        print(i, "->", count)
        visited.append(i)

