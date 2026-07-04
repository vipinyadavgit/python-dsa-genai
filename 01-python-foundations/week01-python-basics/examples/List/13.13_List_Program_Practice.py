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
new_nums = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
    if nums[i] not in new_nums:
        new_nums.append(nums[i])
        print(nums[i], "->", count)

print("================================================================================================================")
print("========================================================Another Approach========================================")

nums = [1,2,2,3,3,3,4]
new_nums= []
count=0
for num in nums:
    if num not in new_nums:
        new_nums.append(num)
        count=count+1
        print(num, "->", nums.count(num))
print("================================================================================================================")
#=======================================================================================================================
'''
Q9 — Find Missing Number ⭐⭐⭐
nums = [1,2,3,5]

Numbers should be from 1 to 5

Output

4
'''
nums = [1,2,3,5]
smallest_num = nums[0]
largest_num = nums[0]
for num in nums:
    if num<smallest_num:
        smallest_num = num
print("smallest_num", "->", smallest_num)
for num in nums:
    if num > largest_num:
        largest_num = num
print("largest_num", "->", largest_num)
for i in range (smallest_num,largest_num+1):
    if i  not in nums:
        print("missing number ->",i)
print("================================================================================================================")
#=======================================================================================================================

'''
Q10 — Linear Search

Take input from the user.
If found:- Element Found
Otherwise:- Element Not Found
❌ Don't use: in , index()
Use a loop.
'''

# nums = [10,20,30,40,50]
# number=int(input("Please enter a number:-"))
#
# for num in nums:
#     if num == number:
#         print("Element Found at position:-",nums)
#         #print("Element Found at position:-", nums.index(number))
#         break
# else:
#     print("Element Not Found")
print("===========================================================================================")
#=================================================================================================
'''
Level 3 — DSA Foundation
Q11 — Separate Even and Odd Numbers ⭐⭐⭐
nums = [1,2,3,4,5,6]

Expected

Even = [2,4,6]

Odd = [1,3,5]
'''

nums = [1,2,3,4,5,6]
even_nums = []
odd_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
    if num % 2 == 1:
        odd_nums.append(num)
print("even_nums", "->", even_nums)
print("odd_nums", "->", odd_nums)

print("============================================================================================")
#====================================================================================================
'''
Q12 — Reverse a List Without reverse() ⭐⭐⭐
nums = [10,20,30,40]

Expected:- [40,30,20,10]

❌ Don't use
reverse()
[::-1]
'''

nums = [10,20,30,40]
reversed_nums = []

for i in range(len(nums)-1,-1,-1):
    reversed_nums.append(nums[i])
print("reversed_nums", "->", reversed_nums)
print("===========================================================================================")
print("=================================Another Approach==========================================")

nums = [10,20,30,40]
reversed_nums = []

left = 0
right = len(nums)-1
while left < right:
    if nums[left] < nums[right]:
        nums[left] , nums[right] = nums[right] , nums[left]
        left += 1
        right -= 1
print("reversed_nums", "->", reversed_nums)
print("===========================================================================================")
#===================================================================================================
'''
Q13 — Largest Difference ⭐⭐⭐⭐
nums = [10,25,5,40]
Output:-    35

(Hint: Largest − Smallest)
Don't use max() or min().
'''

nums = [10,25,5,40]
smallest_num = nums[0]
largest_num = nums[0]
Largest_Difference= []

for num in nums:
    if num<smallest_num:
        smallest_num = num
print("smallest_num", "->", smallest_num)

for num in nums:
    if num>largest_num:
        largest_num = num
print("largest_num", "->", largest_num)

Largest_Difference = largest_num - smallest_num
print("Largest_Difference", "->", Largest_Difference)

print("=====================================================================================")
#=============================================================================================
'''
Q14 — Find Common Elements ⭐⭐⭐⭐
a = [1,2,3,4,5]
b = [3,4,5,6,7]

Expected:- [3,4,5]

Don't use set().
'''
a = [1,2,3,4,5]
b = [3,4,5,6,7]
common_elements = []
for num in a:
    if num in b:
        common_elements.append(num)
    if num not in b:
        print("no common element")
print("common_elements", "->", common_elements)
print("=======================================================================================")
#===============================================================================================
'''
Q15 — Rotate List Left by One ⭐⭐⭐⭐
nums = [10,20,30,40,50]

Expected:- [20,30,40,50,10]
'''
nums = [10,20,30,40,50]
nums = nums[1:]+[nums[0]]
print("nums", "->", nums)
print("=======================================================================================")
print("=================================2nd approach==========================================")

nums = [10,20,30,40,50]
first = nums[0]

for i in range(len(nums) - 1):
    nums[i]=nums[i+1]
nums[-1] = first
print("nums", "->", nums)

print("=======================================================================================")
#=============================================================================================

'''
🔥 Bonus Challenge (Mini Project)
Student Marks Analyzer ⭐⭐⭐⭐
marks = [85,72,91,68,95,72,88]

Without using max(), min(), or sum():

Find the highest mark.
Find the lowest mark.
Calculate the total marks.
Calculate the average.
Count students scoring 80 or above.
Count students who failed (pass mark = 40).
Sort the list in ascending order (you may use sort() here).
Print the topper's mark.
Print all marks greater than the average.
'''
#===========================================================================================================
marks = [85,72,91,68,95,72,88]

print("=================approach one===============")
print("Find the highest mark.")

marks.sort()
print("Highest marks", "->", marks[-1])
print("=============================================")
#===========================================================================================================
print("=================approach two================")
print("Find the highest mark.")
marks = [85,72,91,68,95,72,88]
highest_mark= marks[0]

for mark in marks:
    if mark>highest_mark:
        highest_mark = mark
print("highest_mark", "->", highest_mark)
#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

print("=================approach one===================")
print("Find the lowest mark.")

marks = [85,72,91,68,95,72,88]
marks.sort()
print("Lowest mark", "->", marks[0])
print("=====================================================================================================")

print("=================approach two===================")
marks = [85,72,91,68,95,72,88]
lowest_mark= marks[0]

for mark in marks:
    if mark<lowest_mark:
        lowest_mark = mark
print("lowest_mark", "->", lowest_mark)
#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================
print("Calculate the total marks.")

marks = [85,72,91,68,95,72,88]
total_marks = 0

for mark in marks:
    total_marks = total_marks + mark
print("total_marks", "->", total_marks)
#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

print("Calculate the average.")

marks = [85,72,91,68,95,72,88]
total_marks= 0
count = 0

for i in range(len(marks)):
    count+=1
    total_marks = total_marks + marks[i]
print("total_marks", "->", total_marks)
print("count", "->", count)
average = total_marks/count
print("average", "->", average)

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

print("Count students scoring 80 or above.")
marks = [85,72,91,68,95,72,88,80]
marks_80 = []
count = 0
for i in range(len(marks)):
    if marks[i]>=80:
        marks_80.append(marks[i])
        count+=1
print("students scoring 80 or above", "->", count)
print("marks above 80", "->", marks_80)

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================
'''
Count students who failed (pass mark = 40).
'''
print("Count students who failed (pass mark = 40)")
marks = [85,72,91,68,95,72,88,80,32,24,8,19,36,18]
marks_failed = []
count = 0

for i in range(len(marks)):
    if marks[i]<40:
        marks_failed.append(marks[i])
        count+=1
print("Failed students scoring 40 or less", "->", count)
print("marks less than 40", "->", marks_failed)

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================
'''
Sort the list in ascending order (you may use sort() here).
'''
print("Sort the list in ascending order (you may use sort() here")

marks = [85,72,91,68,95,72,88,80,32,24,8,19,36,18]
marks.sort()
print("Sorted list", "->", marks)

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================
'''
Print the topper's mark.
'''
print("Printing the topper's mark.")
marks = [85,72,91,68,95,72,88,80,32,24,8,19,36,18]
marks.sort()
print("Topper's mark", "->", marks[-1])

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================
'''Print all marks greater than the average.'''
print("Printing all marks greater than the average.")
marks = [85,72,91,68,95,72,88,80,32,24,8,19,36,18,57]
count=0
total_marks=0

for mark in marks:
    count+=1
    total_marks = total_marks + mark
print("total_marks", "->", total_marks)
print("count", "->", count)

average = total_marks/count
print("average", "->", average)

new_marks = []
for mark in marks:
    if mark>average:
        new_marks.append(mark)
print("marks", "->", new_marks)
#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================
'''
Q16 — Check if a List is Sorted
'''
print("Check if a List is Sorted==>approach one")
nums = [10,20,30,40]
if nums == sorted(nums):
    print("list is sorted")
else:
    print("list is not sorted")

print("=======================approach two======================")
nums = [10,20,30,40]
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        print("list is not sorted")
        break
else:
        print("list is sorted")

#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

'''
Q17 — Move All Zeros to the End
nums = [1,0,2,0,3,0,4]
'''

nums = [1,0,2,0,3,0,4,0,5,0,6,0,7,0,8]
new_nums = []
new_nums1=[]
# nums.sort()
# print(nums)
for num in nums:
    if num==0:
        new_nums.append(num)
    if num!=0:
        new_nums1.append(num)
print("new_nums", "->", new_nums)
print("new_nums1", "->", new_nums1)
final_list =new_nums1+new_nums
print("final_list", "->", final_list)
#==================================================================================================
print("=======================approach two======================")
nums = [1,0,2,0,3,0,4,0,5,0,6,0,7,0,8]
final_list=[]

for num in nums:
    if num != 0:
        final_list.append(num)

for num in nums:
    if num==0:
        final_list.append(num)
print("final_list", "->", final_list)
#==================================================================================================
print("=======================approach three======================")

nums = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8]

zeros = nums.count(0)
result = [num for num in nums if num != 0] + [0] * zeros

print(result)
#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

'''
Q18 — Find the First Duplicate
nums = [10,20,30,20,40]

Output:20
'''
nums = [10,20,30,20,40]
new_nums = []

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            print("first duplicate number is ", "->", nums[i])
            break

#==================================================================================================
print("=======================approach two======================")

nums = [10,20,30,20,40]
new_nums = []

for num in nums:
    if num in new_nums:
        print("duplicate number",num)
        break
    new_nums.append(num)
#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================
'''
Q19 — Merge Two Lists Without extend()
a = [1,2,3]
b = [4,5,6]

Expected: [1,2,3,4,5,6]
'''
a = [1,2,3]
b = [4,5,6]

new_list = a+b
print("new_list", "->", new_list)
#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================
'''
Q20 — Find All Pairs with Sum = 10
nums = [1,9,2,8,3,7,4,6,5]

Expected output:
1 9
2 8
3 7
4 6
'''
nums = [1,9,2,8,3,7,4,6,5]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==10:
            print("All Pairs with sum 10", "->", nums[i], nums[j])
#===========================================================================================================
print("=====================================================================================================")
#===========================================================================================================

































































































































