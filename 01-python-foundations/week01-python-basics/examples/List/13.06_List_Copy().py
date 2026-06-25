#copy()

'''
copy() uses =
'''

#   "=" Assigns variables point to the SAME list.

a = [10,20,30]
b = a
b[0] = 999

print(a)
print(b)

#[999, 20, 30]
#[999, 20, 30]
#========================================================================================

#copy()
'''
copy()
Definition:-    Creates a NEW list.
'''

#Syntax:-    new_list = old_list.copy()

a   = [10,20,30,40,50]
b   = a.copy()

b[0] = 999

print(a)
print(b)

#[10, 20, 30, 40, 50]
#[999, 20, 30, 40, 50]

'''
Shallow Copy:- it used to make a new object, but it does not create a copy of items inside it.
instead of that, it keeps the reference to the original item. this means only outer structure is copied,
while nested structure is shared. Due to this , if nested item changed in the copied object ,same change
will be reflected in the original object.
'''
'''
Real-Life Example
You photocopied notebook.Now both people have separate notebooks.
Changes do not affect each other.
'''
'''
SHALLOW COPY
Meaning:
surface copied
inside shared
'''

nL1=[[10,20],[30,40],[50,60]]
nL2=nL1.copy()

print("nL1",nL1)
print("nL2",nL2)

nL2[0][0]=101
print("appended nL1",nL1)
print("appended nL2",nL2)

#=============================================================================================
#
a = [1,2,3]
b = a.copy()
b[0] = 100

print(a)
print(b)
#==============================================================================================

nums = [10,20]
copy_nums = nums.copy()
print(copy_nums)

#=============================================================================================

#practice 1

marks=[80,90,100]
marks1=marks
marks1[0]=999
print(marks)
print(marks1)

# [999, 90, 100]
# [999, 90, 100]
#==================================================================================
#practice 2

marks = [80,90,100]
marks2=marks.copy()
marks2[0]=999
print(marks)
print(marks2)
#[80, 90, 100]
# [999, 90, 100]

#=================================================================================
#practise 3

tech = ["Python","AI","Git"]
tech1=tech.copy()
tech.append("Docker")

print(tech)
print(tech1)

#['Python', 'AI', 'Git', 'Docker']
#['Python', 'AI', 'Git']
#===================================================================================

#Mini Challenge

original = [10,20,30]
backup = original.copy()
original.append(40)

print("original",original)
print("backup",backup)

#original [10, 20, 30, 40]
#backup [10, 20, 30]

#=====================================================================================
#Deep copy
'''
Deep Copy:-
Now we want EVERYTHING separate.
'''
import copy

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

b[0][0] = 100

print(a)
print(b)
'''
[[1, 2], [3, 4]]
[[100, 2], [3, 4]]

WHY?

Because deep copy copies:
✅ outer list
✅ inner lists ALSO
Everything becomes independent.
'''
import copy

a = [[10,20]]

b = copy.deepcopy(a)

a[0].append(30)

print(b)
print(a)
#[[10,20]]
#[[10, 20, 30]]
#========================================================================================
'''
GOLDEN RULE
If you do:

append()
remove()
sort()
You MODIFY shared object.


Replacement
a[0] = [100]  #changes reference.

Modification
append() #==>   changes actual shared object.


If you do:
=
You REPLACE reference.
Huge difference.
'''
#===================================================================================================

a = [1, 2, 3]

b = a

b[0] = 100

print('Test',a)
print('Test',b)
#[100,2,3]
#[100,2,3]
#=====================================================
a = [10, 20, 30]

b = a.copy()

b[1] = 99

print(a)
print(b)
#[10, 20, 30]
#[10, 99, 30]
#==========================================================
a = [1, 2, 3]

b = a[:]

a.append(4)

print(a)
print(b)
#[1, 2, 3, 4]
#[1, 2, 3]
#==============================================
a = [[1, 2], [3, 4]]

b = a

b[0][1] = 99

print("test1 ",a)
print("test2",b)
#=============================================
a = [[1, 2], [3, 4]]

b = a.copy()

b[1][0] = 100

print(a)
print(b)
#[[1, 2], [100, 4]]
#[[1, 2], [100, 4]]
#=============================================MEDIUM LEVEL
import copy

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

b[0][0] = 50

print(a)
print(b)
#[[1, 2], [3, 4]]
# [[50, 2], [3, 4]]
#=============================================
a = [1, 2, [3, 4]]

b = a.copy()

a[2].append(5)

print(b)
print(a)
# [1, 2, [3, 4, 5]]
# [1, 2, [3, 4, 5]]
#=================================================
import copy

a = [1, 2, [3, 4]]

b = copy.deepcopy(a)

a[2][0] = 100

print(a)
print(b)
# [1, 2, [100, 4]]
# [1, 2, [3, 4]]
#================================================
a = [[10], [20]]

b = a.copy()

c = b

a[0].append(99)

print(a)
print(b)
print(c)
# [[10, 99], [20]]
# [[10, 99], [20]]
# [[10, 99], [20]]
#=====================================================
a = [1, 2, [3, 4]]

b = a[:]

b[2] = [100, 200]

print("nested:",a)
print("nested:",b)
# nested: [1, 2, [3, 4]]
# nested: [1, 2, [100, 200]]
#======================================================TOUGH LEVEL
import copy

a = [[1, 2], [3, 4]]

b = a.copy()

c = copy.deepcopy(a)

a[0].append(99)

print(a)
print(b)
print(c)
# [[1, 2, 99], [3, 4]]
# [[1, 2, 99], [3, 4]]
# [[1, 2], [3, 4]]
#-==================================================================
#12 explain
a = [[1], [2]]

b = a.copy()

b[0] = [100]

print(a)
print(b)
# [[1], [2]]
# [[100], [2]]
#====================================================================
a = [[1, 2], [3, 4]]

b = a.copy()

# b.append([5, 6])

b[0][0] = 99

print(a)
print(b)
# [[99, 2], [3, 4]]
# [[99, 2], [3, 4]]
#=========================================================
import copy

a = [1, [2, [3, 4]]]

b = a.copy()

c = copy.deepcopy(a)

a[1][1][0] = 100

print(a)
print(b)
print(c)
# [1, [2, [100, 4]]]
# [1, [2, [100, 4]]]
# [1, [2, [3, 4]]]
#=====================================(VERY IMPORTANT)
a = [[1, 2], [3, 4]]

b = a[:]

a[0] = [100, 200]

print(a)
print(b)
print(b)
# [[100, 200], [3, 4]]
# [[1, 2], [3, 4]]
#===================================
#explain 16
import copy

a = [[1], [2]]

b = a.copy()

c = copy.deepcopy(a)

b[0].append(100)

a.append([999])

print(a)
print(b)
print(c)
# [[1, 100], [2], [999]]
# [[1, 100], [2]]
# [[1], [2]]
#==========================================
a = [1, 2, [3, 4]]

b = a.copy()

c = b.copy()

a[2][1] = 999

print(a)
print(b)
print(c)
#==============================================
import copy

a = [[1, 2], [3, 4]]

b = copy.copy(a)

c = copy.deepcopy(a)

b[1].append(100)

print(a)
print(b)
print(c)
#==============================================
a = [[1], [2]]

b = a[:]

b[0] += [100]

print(a)
print(b)
#=================================================(INTERVIEW LEVEL)
import copy

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

a[0] = [100]

a[1].append(5)

print(a)
print(b)
#==============================================================================
'''
Replacement
a[0] = [100]  #changes reference.

Modification
append() #==>changes actual shared object.
'''






















































































































































