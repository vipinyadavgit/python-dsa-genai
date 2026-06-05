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
        print(j,end=" ")
    print()
print("===================================")
print("=========USING RANGE==========================")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("=============USING P=====================")
n=5

for i in range(n):
    p = 1
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()
print("=========================")

#============================================================================
'''
12345
1234
123
12
1
'''
n=5
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("=========Another approach==============")
n=5
for i in range(n):
    p=1
    for j in range(i,n):
        print(p,end=" ")
        p+=1
    print()
print("==================================")
#==========================================================
'''
1
22
333
4444
55555
'''
n=5
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
print("===================================")
n=5
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
print("===================================")
n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()
print("====================================")

#===========================================================
'''
55555
4444
333
22
1
'''
n=5
p=5
for i in range(n):
    for j in range(i,n):
        print(p,end=" ")
    p-=1
    print()
print("==========Another approach==============")
n=5
for i in range(n,0,-1):
    for j in range(i): #for j in range(1,i+1)
        print(i,end=" ")
    print()
print("=========================================")
#=============================================================
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
        p += 1
    print()
print("========================")
#============================================

'''
12345
678910
1112131415
1617181920
'''
n=4
p=1
for i in range(n):
    for j in range(n+1):
        print(p,end=" ")
        p+=1
    print()
print("=========================")
#================================================
'''
1
21
321
4321
54321
'''
n=5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print("=========================")
#===========================================
print("=========Another approach======================")

n=5
for i in range(1,n+1):
    p=i
    for j in range(i):
        print(p,end=" ")
        p-=1
    print()
print("=========================================")
#=================================================
'''
54321
4321
321
21
1
'''
n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print("==============================")
#==================================================
'''
    1
   121
  12321
 1234321
123454321
'''
#=================================================
'''
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
'''
#================================================
'''
1
13
135
1357
13579
'''
'''
==>how many rows
==>how many values per row
==>what we are printing?
'''
n=5

for i in range(1,n+1):
    p = 1
    for j in range(1,i+1):
        print(p,end=" ")
        p+=2
    print()
print("=============Test2===========================")
#===============================================================
'''
11111
22222
33333
44444
55555
'''
#========================================================
'''
12345
12345
12345
12345
12345
'''
'''
==>how many rows
==>how many values per row
==>what we are printing?
'''
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end='')
    print()
print("==============test1====================")
#====================================================
'''
1
12
123
1234
'''
'''
How many rows?
How many values per row?
What should be printed?
'''

n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("=============================================")
#=================================================
'''
1
22
333
4444
'''
'''
==>how many rows
==>how many values per row
==>what we are printing?
'''
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print("===================================")
#============================================
'''
1
12
123
1234
12345
'''
'''
==>how many rows=5
==>how many values per row=>equal to row number
==>what we are printing?=j
'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("===========================================")
#=========================================================
'''
12345
1234
123
12
1
'''
'''
==>how many rows=5
==>how many values per row=>equal to row number but decreasing
==>what we are printing? j
'''
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("====================================")
#================================================================
'''
1
22
333
4444
55555
'''
'''
==>how many rows=5
==>how many values per row=>equal to row number and increasing
==>what we are printing? i
'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print("===============================")
#===============================================================
'''
55555
4444
333
22
1
'''
'''
==>how many rows=5
==>how many values per row=>equal to row number and decreasing
==>what we are printing? i
'''
n=5
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print("================================")
#===================================================
'''
1
21
321
4321
54321
'''
'''
==>how many rows=5
==>how many values per row=>equal to row number and decreasing
==>what we are printing? j
Values in Row 4? =4
Increasing or decreasing? =decrasing
Print i or j?=j
'''
n=5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print("===================================")
#==============================================================
'''
54321
4321
321
21
1
'''
'''
==>how many rows=5
==>how many values per row=>equal to row number and decreasing
==>what we are printing? j
Values in Row 3? 3
What should i be? 5
Print i or j? j
'''
n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print("===================================")
#==============================================================
'''
11111
22222
33333
44444
55555
'''
'''
==>how many rows=5
==>how many values per row=>equal to row number of rows
==>what we are printing? i
Does row length change? no
Inner loop depend on i or n?n
Print i or j?i
'''
n=5
for i in range(1,n+1):
    for j in range(n):
        print(i,end=" ")
    print()
print("====================================")
for i in range(1, 6):   # numbers from 1 to 5
    print(str(i) * 5)   # repeat the digit 5 times
'''
| Row | How many values? | What values? |
| --- | ---------------- | ------------ |
| 1   | ?                | ?            |
| 2   | ?                | ?            |
| 3   | ?                | ?            |

'''