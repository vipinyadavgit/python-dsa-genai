for i in range(2):
    for j in range(3):
        print(i, j)
#===============================
for i in range(3):
    for j in range(2):
        print("*")


#==================================
for i in range(2):
    print("Outer")

    for j in range(2):
        print("Inner")
#==================================
for i in range(3):
    for j in range(1):
        print(i)
        print("=================")
#==========================================
for i in range(2):
    for j in range(2):
        print(i+j)
#==========================================
'''
*
*
*
'''
for i in range(3):
    print("*")
print("===============================")
#==============================================
for i in range(3):
    for j in range(1):
        print("*")
#+=============================================
'''
* * *
* * *
'''
for i in range(2):
    for j in range(3):
        print("*",end="  ")
    print()
print("=================================")
#================================
'''
1 1 1
2 2 2
3 3 3
'''
for i in range(3):
    for j in range(3):
        print(i+1,end="  ")
    print()
print("=================================")
#======================================
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
n= 5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
print("\nPattern 1: SQUARE")

print("====================================")
#=========================================
#Another approach
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
n=5
#outer loop for rows
for i in range(1,n+1):
    #inner loop for columns
    for j in range(1,n+1):
        print("*",end=" ")
    print()
print("================================")
#======================================
print("\nPattern 2: Increasing triangle")
'''Increasing triange any side will have inner loop condition as (i+1)'''
'''
*
**
***
****
*****
'''

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
print("\nPattern 2: Increasing triangle")
print("===============main===================================")

'''Increasing triange any side will have inner loop condition as (i+1)'''
'''
*
**
***
****
*****
'''
# print("\nPattern 2: Right Triangle")
# for i in range(1, 6):
#     print("* " * i)
#======================================
'''
*
**
***
****
*****
'''
#another approach
# n= int(input("Enter a number: "))
#
# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
#=======================================================

#===================================================
'''
Pattern 3: Inverted Right Triangle
* * * * * 
* * * * 
* * * 
* * 
* 
'''
n=5
#for rows
for i in range(n):
    #for col
    for j in range(i,n):
        print("*",end="")
    print()
print("=======Inverted Right Triangle==============")
'''Decreasing triange ,any side, will have inner loop condition as (i,n)'''
#=====================================
#another approach
'''
Pattern 3: Inverted Right Triangle
* * * * * 
* * * * 
* * * 
* * 
* 
'''
n=5
#for rows
for i in range(n+1):
    #for col
    for j in range(i,n+1):
        print("*",end=" ")
    print()
print("====================================")
#==================================================
'''
1 1 1 1 * 
1 1 1 * * 
1 1 * * * 
1 * * * * 
* * * * *  
'''
n=5
for i in range(n):
    for j in range(i,n-1):
        print("1",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
print("=============================")
#===============================================================
'''
1 1 1 1 1 * 
1 1 1 1 * * 
1 1 1 * * * 
1 1 * * * * 
1 * * * * *
'''
n=5
for i in range(n):
    for j in range(i,n):
        print("1",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
print("=============================")
#=================================================================
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''
n=5
#for row
for i in range(n):
    #for col
    for j in range(i):
        print(" ",end=" ")
    for k in range(i,n ):
        print("*",end=" ")
    print()
print("=============================")
#=====================================
#another approach
'''
1 * * * * * 
1 1 * * * * 
1 1 1 * * * 
1 1 1 1 * * 
1 1 1 1 1 *
'''
n=5
#for row
for i in range(n):
    #for col
    for j in range(i+1):
        print("1",end=" ")
    for k in range(i,n ):
        print("*",end=" ")
    print()
print("=============================")
#==========================================
'''pyramid'''
'''
Enter the row size for the pattern: 5
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

'''
n=5
for i in range(n):
    for j in range(i,n-1):
        print("  ",end=" ")
    for k in range(i+1):
        print("* ", end=' ')
    for l in range(i):
        print("* ",end=" ")
    print()
print("============check==================")
#Another approach
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()
print("==============================")
#=============================================================
'''reverse pyramid'''
'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
n=5
#for rows
for i in range(n):
    #for column
    for j in range (i):
        print(" ",end=" ")
    for k in range(i,n):
        print("*",end=" ")
    for l in range(i,n-1):
        print("*",end=" ")
    print()
print('======test========================')
#Another approach
n=5
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()
print("==============================")
#=====================================================
'''Diamond'''
'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * *  
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''
n=5
for i in range(n-1):
    for j in range(i,n-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*", end=' ')
    for l in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    #for column
    for j in range (i):
        print(" ",end=" ")
    for k in range(i,n):
        print("*",end=" ")
    for l in range(i,n-1):
        print("*",end=" ")
    print()
print("===============================================")
#======================================
#Another approach
n = 5

# top half
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()
# bottom half
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()
print("=======================================")
#=========================================================
'''Left pascals triangle'''
'''
* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
n=5
for i in range(n-1):
    for j in range(i+1):
        print("*",end=" ")
    print()
for k in range(n):
    #for col
    for l in range(k,n):
        print("*",end=" ")
    print()
print("===================================")
#====================================================
'''Left pascals triangle'''
'''
        *
     *  *
  *  *  *
* *  *  *
  *  *  *
     *  *
        *
'''
n=4
for i in range(n-1):
    for j in range(i,n-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
for l in range(n):
    for m in range(l):
        print(" ",end=" ")
    for o in range(l,n):
        print("*",end=" ")
    print()
print("============================")
#========================================================
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
        i=i+1
    print()
print("==============================")
#=====================================================
'''
1
12
123
1234
12345
'''
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print("==============================")
#==============================================
'''
#
##
###
####
#####
'''
n=5
for i in range(n):
    for j in range(i+1):
        print("#",end="")
    print()
print("==============================")
#===========================================
'''
A
AA
AAA
AAAA
AAAAA
'''
n=5
for i in range(n):
    for j in range(i+1):
        print("A",end="")
    print()
print("==============================")
#===========================================
'''
Practice 3

12345
1234
123
12
1
'''
n=5

for i in range(n):
    p = 1
    for j in range(i,n):
        print(p,end="")
        p=p+1
    print()
print("==============================")
#==============================================
'''
1
12
123
1234
12345
'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("==============================")
#=======================================
'''
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''
for i in range(1,n+1):
    for j in range(i,n+1):
        print(i,end="")
    print()
print("==============================")
#=======================================
'''
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
'''
n=5
for i in range(n):
    p=0
    for j in range(i,n+1):
        print(p,end="")
        p=p+1
    print()
print("==============================")
#==================================================
'''
1
12
123
1234
12345
'''
#how many rows
for i in range(1,6):
    #What is printed in each row
    for j in range(1,i+1):
        #incrementing number
        print(j,end="")
    print()
print("==============================")
#======================================
'''
1
22
333
4444
55555
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
print("==============================")
#======================================
'''
54321
5432
543
54
5
'''
for i in range(5,0,-1):
    for j in range(i):
        print(5-j,end="")
    print()
print("==============================")
#========================================
'''
12345
1234
123
12
1
'''
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("==============================")
#=========================================
'''
1
21
321
4321
54321
'''
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end="")
    print()
print("==============================")
#===========================================
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
print("==============================")
