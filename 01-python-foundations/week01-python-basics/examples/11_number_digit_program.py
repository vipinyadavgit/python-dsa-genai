# number = int(input("Enter a number: "))
# print(number%10)
# print("==============================================================")
# #======================================================================
# number = int(input("Enter a 4 digit number: "))
# print(number//10)
# print("==============================================================")
#=====================================================================

#Extract All Digits
# number = int(input("Enter a number: "))
#
# while number > 0:
#     digit=number%10
#     print("digit",digit)
#     number=number//10
#
# print("==============================================================")
# number = 9876
#
# while number > 0:
#     digit = number % 10
#     print(digit)
#     number=number//10
# print("===============================================================")
# #=================================================================================
# num = 99
#
# count = 0
#
# while num > 0:
#     count += 1
#     num = num // 10
#
# print(count)
# print("========================================================================")
# #===============================================================================
'''
Practice 1
Count digits in a user-entered number.
'''
num = int(input("Enter a number: "))
count = 0
while num>0:
    num = num // 10
    count += 1
print(count)
# print("===========================================================================")
#===================================================================================
'''
Practice 2
Print:
The number has X digits
'''
num = int(input("Enter a number: "))
count = 0
while num>0:
    num = num // 10
    count = count + 1

print("total digits",count)
print("=============================================================================")
#=====================================================================================
#Mini Challenge

num = 987654321
count = 0
while num>0:
    num=num//10
    count=count+1
print("total digits",count)
print("===========================================================================")
#=====================================================================================
'''Sum of Digits'''

num = int(input("Enter a number: "))
sum=0
while num>0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print(sum)
print("==============================================================================")
#======================================================================================
num = 567
sum=0
while num>0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print(sum)
print("==============================================================================")
#======================================================================================
'''
Reverse Number  :-
'''
num = int(input("Enter a number: "))
rev=''
while num>0:
    digit = num % 10
    rev = rev + str(digit)
    num = num // 10
print(rev)
print("=========================================================================")
#==================================================================================
'''
Reverse Number  :-
'''
num = int(input("Enter a number: "))
rev=0
while num>0:
    digit = num % 10
    rev = rev*10 + digit
    num = num // 10
print(rev)
print("=========================================================================")
#=================================================================================
num =121
rev = ''
temp = num
while num>0:
    digit = num % 10
    rev = rev + str(digit)
    num = num // 10
print(rev)
if temp==int(rev):
   print("palindrom Number")
else:
   print("Not palindrom")
print("==========================================")
#============================================================================
num = 121
rev = ""

for digit in str(num)[::-1]:
    rev += digit

print(rev)
if str(num) == rev:
    print("Palindrome Number")
else:
    print("Not Palindrome")
print("==========================================")
#=======================================================
num= 121
rev =0
temp = num
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)
if temp==rev:
    print("Palindrome Number")
else:
    print("Not Palindrome")
print("=============================================")
#==============================================================
'''
🧪 Practice 1
Reverse a number without using string.
'''
num = int(input("Enter a number: "))
rev=0
while num>0:
    digit= num%10
    rev= rev*10+digit
    num = num//10
print("reversed number",rev)
print("====================================================")
#===============================================================
num=987
rev= 0
while num>0:
    digit = num%10
    rev = rev*10+digit
    num = num//10
print("reversed number",rev)
print("=============================================================")
#=====================================================================
'''
🎯 Mini Challenge
'''
num =1200
rev=0
while num>0:
    digit = num % 10
    rev = rev*10+digit
    num = num//10
print("reversed number",rev)
print("================================================")