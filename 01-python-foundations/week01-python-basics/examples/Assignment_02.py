# ==========================================
# Q1.Given the expression a < b == c < d, what is happening here? Explain with an example.
# a. a, b, c, d = 1, 2, 2, 3
# b. print (a < b == c < d) # Test this code
# ==========================================

a, b, c, d = 1, 2, 2, 3

print(a < b == c < d)

# Explanation:
# a < b == c < d
# becomes:
# (a < b) and (b == c) and (c < d)
#
# (1 < 2) and (2 == 2) and (2 < 3)
# True and True and True
# Output: True


# ==========================================
# Q2.
# ==========================================

a = 10
b = 20
c = 15

maximum = a if a > b and a > c else b if b > c else c

print("Maximum =", maximum)


# ==========================================
# Q3. String to List and List to String
# ==========================================

# String to List

s = "Hello"

lst = list(s)

print(lst)

# Output:
# ['H', 'e', 'l', 'l', 'o']


# List to String

lst = ['H', 'e', 'l', 'l', 'o']

s = ''.join(lst)

print(s)

# Output:
# Hello


# ==========================================
# Q4. Process Mixed Data Type List
# ==========================================

L = [12, 'Python', 90.56, 78, 34, 'Is', 65.90, 'Easy']

sum_numbers = 0
string_concat = ""
sequence_count = 0

for item in L:

    if isinstance(item, (int, float)):
        sum_numbers += item

    elif isinstance(item, str):
        string_concat += item

    elif isinstance(item, (list, tuple, dict)):
        sequence_count += len(item)

print("Sum =", sum_numbers)
print("Strings =", string_concat)
print("Sequence Elements =", sequence_count)


# ==========================================
# Q5.
# ==========================================

num = 5

fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print("Factorial =", fact)


# ==========================================
# Q6. Ignore Empty Strings using Continue
# ==========================================

words = ["hello", " ", "", "world", " ", "python"]

for word in words:

    if word.strip() == "":
        continue

    print(word.capitalize(), end=" ")

print()


# Output:
# Hello World Python


# ==========================================
# Q7.
# ==========================================

while True:

    num = int(input("Enter a positive number: "))

    if num > 0:
        print("Valid Number:", num)
        break

    print("Invalid! Try Again.")


# ==========================================
# Q8.
# ==========================================

num = int(input("Enter Number: "))

if num < 2:
    print("Not Prime")

else:

    for i in range(2, num):

        if num % i == 0:
            print("Not Prime")
            break

    else:
        print("Prime")


# ==========================================
# Q9.
# ==========================================

s = "people"

for ch in s:

    if s.count(ch) == 1:
        print("First Non-Repeating Character =", ch)
        break

# Output:
# o


# ==========================================
# Q10.
# ==========================================

password = input("Enter Password: ")

has_upper = False
has_lower = False
has_digit = False

for ch in password:

    if ch.isupper():
        has_upper = True

    elif ch.islower():
        has_lower = True

    elif ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Valid Password")

else:
    print("Invalid Password")


# Example Valid Password:
# Python123
#==========================second approach=================
import re

password = input("Enter Password: ")

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

if re.match(pattern, password):
    print("Valid Password")

else:
    print("Invalid Password")
# ==========================================
# Q11.
# ==========================================
fruit_list = ["apple", "banana", "cherry", "date", "fig"]

word = input("Enter fruit name: ")

for fruit in fruit_list:

    if fruit == word:
        print(f"Found '{word}' in the Fruit Bucket!")
        break

else:
    print(f"'{word}' not found in the fruit bucket. Try another fruit.")

# ==========================================
# Q12.
# ==========================================

#a) Using For Loop
s = input("Enter String: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

print(reverse)

#b) Using While Loop
s = input("Enter String: ")

i = len(s) - 1

while i >= 0:
    print(s[i], end="")
    i -= 1

#c) Using Slicing
s = input("Enter String: ")

print(s[::-1])

#d) Using Reverse Method
s = input("Enter String: ")

lst = list(s)

lst.reverse()

print("".join(lst))

# ==========================================
# Q13.
# ==========================================

correct_username = "admin"
correct_password = "Admin@1234"

attempt = 1

while attempt <= 3:

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username.lower() == correct_username.lower() and password == correct_password:
        print("Welcome Admin!")
        break

    else:
        print("Invalid Credentials")
        attempt += 1

else:
    print("Account Locked! Maximum attempts exceeded.")

# ==========================================
# Q14.
# ==========================================

s = "Al249ntxrt7879"

letters = ""
digits = ""

for ch in s:

    if ch.isalpha():
        letters += ch

    elif ch.isdigit():
        digits += ch

letters = ''.join(sorted(letters))
digits = ''.join(sorted(digits))

print(letters + digits)

# ==========================================
# Q15.
# ==========================================

s = 'racecar'

s1 = ""

for ch in s:
    if ch.isalnum():
        s1 += ch.lower()

if s1 == s1[::-1]:
    print("string is Palindrome")

else:
    print("Not Palindrome")
#=========================second approach========================
str1 = "racecar"
rev1 = ''
for ch in str1:
    rev1 =  ch.lower() + rev1
print(rev1)
if str1 == rev1:
    print("Palindrome")
else:
    print("Not Palindrome")

# ==========================================
# Q16.
# ==========================================

year = int(input("Enter Year: "))

if year % 4 != 0:
    print("Not Leap Year")

elif year % 100 != 0:
    print("Leap Year")

elif year % 400 == 0:
    print("Leap Year")

else:
    print("Not Leap Year")

# ==========================================
# Q17.
# ==========================================

s = 'Pratibha Pawar'

s = s.lower().replace(" ", "")

max_char = ""
max_count = 0

for ch in s:

    count = s.count(ch)

    if count > max_count:
        max_count = count
        max_char = ch

print(max_char, "Occurred", max_count, "times")

# ==========================================
# Q18.
# ==========================================
s = input("Enter String: ")

result = ""

vowels = "aeiouAEIOU"

for ch in s:

    if ch not in vowels:
        result += ch

print(result)

# ==========================================
# Q19.
# ==========================================
print('s[:]',s[:])#               -> Sachin Patil

print('s[::]',s[::])#                -> Sachin Patil

print('s[1:5]',s[1:5])#              -> achi

print('s[2:5]',s[2:5])#              -> chi

print('s[1:]',s[1:])#               -> achin Patil

print('s[:3]',s[:3])#               -> Sac

print('s[:]',s[:])#                -> Sachin Patil

print('s[-5:-2]',s[-5:-2])#            -> Pat

print('s[-3:]',s[-3:])#              -> til

print('s[:-4]',s[:-4])#              -> Sachin P

print('s[-4:-1]',s[-4:-1])#            -> ati

print('s[1:6:2]',s[1:6:2])#            -> ahi

print('s[::0]',s[::0])#               -> Error

print('s[5:5]',s[5:5])#              -> ''

print('s[3:2]',s[3:2])#              -> ''

print('s[-3:-4]',s[-3:-4])#            -> ''

print('s[:8:3]',s[:8:3])#             -> Sh

print('s[2:10:4]',s[2:10:4])#           -> c

print('s[-10:-2:3]',s[-10:-2:3])#         -> cna

print('s[::3]',s[::3])#             -> Sh t

print('s[::]',s[::])#               -> Sachin Patil

print('s[::-1]',s[::-1])#              -> litaP nihcaS

print('s[0:]',s[0:])#              -> Sachin Patil

print('s[:len(s)]',s[:len(s)])#          -> Sachin Patil

print('s[2:7:2]',s[2:7:2])#            -> ci

print('s[4:-1:1]',s[4:-1:1])#           -> in Pati

print('s[-10:-3:2]',s[-10:-3:2])#         -> ci a

print('s[1:8:3]',s[1:8:3])#            -> aiP

print('s[5:1:-1]',s[5:1:-1])#           -> nihc

print('s[-3:-8:-2]',s[-3:-8:-2])#         -> tPn

print('s[10:2:-3]',s[10:2:-3])#          -> iPi

print('s[::-2]',s[::-2])#             -> lia ihS

print('s[::2]',s[::2])#              -> Sci ai

print('s[::-1]',s[::-1])#             -> litaP nihcaS

print('s[-1:-6:-2]',s[-1:-6:-2])#         -> ltp

print('s[100:200]',s[100:200])#          -> ''

print('s[-100:100]',s[-100:100])#         -> Sachin Patil

print('s[5:100]',s[5:100])#             -> n Patil

print('s[-100:5]',s[-100:5])#           -> Sachi

print('s[1:-1]',s[1:-1])#             -> achin Pati

print('s[-3:3]',s[-3:3])#             -> ''

print('s[2:-2]',s[2:-2])#             -> chin Pat

print('s[-5:5]',s[-5:5])#             -> ''

#==========================================================================================
#Q 20
#=========================================================================================
'''
        * 
      * * * 
    * * * * * 
  * * * * * * *   
    * * * * *   
      * * *  
        *       
'''

n=4
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
# ==========================================
# Q21.
# ==========================================

# List

lst = [1, 2, 3, 4, 5]

if len(lst) > 1:
    lst[0], lst[-1] = lst[-1], lst[0]

print(lst)

# String
s = "hello"

if len(s) > 1:
    s = s[-1] + s[1:-1] + s[0]

print(s)
# ==========================================
# Q22. Fibonacci Series
# ==========================================

n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()


# ==========================================
# Q23. Anagram Number
# ==========================================

str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagram")

else:
    print("Not Anagram")
# ==========================================
# Q24.
# ==========================================

original_list = [1, 2, 3, 4, 5, 6, 7]

mid = (len(original_list) + 1) // 2

lst_first_half = original_list[:mid]
lst_second_half = original_list[mid:]

print(lst_first_half)
print(lst_second_half)
# ==========================================
# Q25.
# ==========================================

original_list = ['a', 'b', 'c', 'd', 'e']

n = 2

shuffled_list = original_list[n:] + original_list[:n]

print(shuffled_list)

# ==========================================
# Q26.
# ==========================================

original_list = [1, 2, 3, 2, 4, 5, 1]

unique_list = [x for x in original_list if original_list.count(x) == 1]

duplicate_list = [x for x in original_list if original_list.count(x) > 1]

print("Unique:", unique_list)
print("Duplicates:", duplicate_list)

# ==========================================
# Q27.
# ==========================================

original_list = [1, 2, 3, 2, 4, 5, 1]

unique_list = [x for x in original_list if original_list.count(x) == 1]

duplicate_list = list({x for x in original_list if original_list.count(x) > 1})

print("Unique:", unique_list)
print("Duplicates:", duplicate_list)

# ==========================================
# Q28. Flatten Nested List
# ==========================================

nested_list = [[1, 2], [3, 4], [5, 6]]

flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print(flat_list)

# Output:
# [1,2,3,4,5,6]


# ==========================================
# Q29.
# ==========================================

employees = [(101, 'Alice', 'HR', 50000),(102, 'Bob', 'IT', 60000),(103, 'Charlie', 'Finance', 70000)]

# Add Employee
employees.append((104, 'David', 'Sales', 65000))

# Remove Employee
emp_id = 102
employees = [emp for emp in employees if emp[0] != emp_id]

# Update Salary
emp_id = 101
new_salary = 55000
updated = []
for emp in employees:

    if emp[0] == emp_id:
        updated.append((emp[0], emp[1], emp[2], new_salary))

    else:
        updated.append(emp)

employees = updated

# Highest Salary

highest = max(employees, key=lambda x: x[3])

print("Highest Salary Employee:", highest)

print(employees)
# ==========================================
# Q30.
# ==========================================

coordinates = [(1, 2), (3, 4), (5, 6)]

for x, y in coordinates:

    print(f"x = {x}, y = {y} - sm = {x+y}")


# ==========================================
# Q31.
# ==========================================

names = ('Alice', 'Bob')

ages = (25, 30)

result = list(zip(names, ages))

print(result)

# Output:
# [('Alice',25), ('Bob',30)]


# ==========================================
# Q32.
# ==========================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union Operator:", A | B)
print("Intersection Operator:", A & B)
print("A-B:", A - B)
print("B-A:", B - A)

print("Union Method:", A.union(B))
print("Intersection Method:", A.intersection(B))
print("Difference Method:", A.difference(B))
print("Difference Method:", B.difference(A))


# ==========================================
# Q33.
# ==========================================

sentence = "apple orange apple banana orange apple"

words = sentence.split()

freq = {}

for word in words:

    if word in freq:
        freq[word] = freq[word] + 1

    else:
        freq[word] = 1

print(freq)

# ==========================================
# Q34. Highest Scoring Student
# ==========================================

score = {
    'Alice': 90,
    'Bob': 85,
    'Charlie': 95
}

highest_student = max(score, key=lambda student: score[student])

print(highest_student)
#======================================================
#Q36:-
#====================================================
with open("File_Data_1.txt", "r") as file1:
    data1 = file1.read()

with open("File_Data_2.txt", "r") as file2:
    data2 = file2.read()

with open("organized_data.txt", "w") as outfile:

    outfile.write("----- Content from File_Data_1.txt -----\n")
    outfile.write(data1)

    outfile.write("\n\n")

    outfile.write("----- Content from File_Data_2.txt -----\n")
    outfile.write(data2)

print("Files merged successfully.")
#=========================================================================
#Q40
#==============================================

'''
ZeroDivisionError
NameError
ValueError
IndexError
FileNotFoundError
OverflowError

Syntax Errors cannot be handled using try-except 
because Python cannot execute the program until the syntax is correct.
'''
#