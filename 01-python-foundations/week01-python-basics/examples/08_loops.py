"""
08 - Loops in Python
Learn about for loops and while loops

Topics covered:
- for loop
- while loop
- range() function
- break and continue
- Nested loops
- Loop patterns
"""

# ============================================
# 1. FOR LOOP - Iterate over sequences
# ============================================
print("=" * 60)
print("FOR LOOP BASICS")
print("=" * 60)

# Loop through a list
print("\nLoop through a list:")
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(f"  🍎 {fruit}")

# Loop through a string
print("\nLoop through a string:")
for char in "Python":
    print(f"  → {char}")

# Loop with index using enumerate
print("\nLoop with index:")
languages = ["Python", "Java", "JavaScript"]
for index, lang in enumerate(languages):
    print(f"  {index + 1}. {lang}")

# ============================================
# 2. RANGE() FUNCTION
# ============================================
print("\n" + "=" * 60)
print("RANGE() FUNCTION")
print("=" * 60)

# range(stop) - From 0 to stop-1
print("\nrange(5) - Numbers from 0 to 4:")
for i in range(5):
    print(f"  {i}", end=" ")
print()

# range(start, stop) - From start to stop-1
print("\nrange(1, 6) - Numbers from 1 to 5:")
for i in range(1, 6):
    print(f"  {i}", end=" ")
print()

# range(start, stop, step) - With custom step
print("\nrange(0, 10, 2) - Even numbers 0 to 10:")
for i in range(0, 11, 2):
    print(f"  {i}", end=" ")
print()

# Reverse range
print("\nrange(10, 0, -1) - Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(f"  {i}", end=" ")
print()

# ============================================
# 3. WHILE LOOP - Loop based on condition
# ============================================
print("\n" + "=" * 60)
print("WHILE LOOP")
print("=" * 60)

# Basic while loop
print("\nCount from 1 to 5:")
count = 1
while count <= 5:
    print(f"  Count: {count}")
    count += 1

# While loop with condition
print("\nDouble until > 100:")
number = 1
while number <= 100:
    print(f"  {number}", end=" ")
    number *= 2
print()

# User simulation (in real scenario, use input())
print("\nPassword checker simulation:")
attempts = 0
max_attempts = 3
correct_password = "python123"
entered_password = "wrong"  # Simulating wrong password

while entered_password != correct_password and attempts < max_attempts:
    attempts += 1
    print(f"  Attempt {attempts}/{max_attempts}")
    # In real: entered_password = input("Enter password: ")
    if attempts == 2:
        entered_password = "python123"  # Simulate correct on 2nd try

if entered_password == correct_password:
    print("  ✅ Access granted!")
else:
    print("  ❌ Access denied!")

# ============================================
# 4. BREAK STATEMENT - Exit loop early
# ============================================
print("\n" + "=" * 60)
print("BREAK STATEMENT")
print("=" * 60)

# Break when condition is met
print("\nFind first number divisible by 7:")
for num in range(1, 50):
    if num % 7 == 0:
        print(f"  Found: {num}")
        break  # Exit loop
print("  Loop exited")

# Break in while loop
print("\nSum until total > 100:")
total = 0
num = 1
while True:  # Infinite loop
    total += num
    print(f"  Adding {num}, Total: {total}")
    if total > 100:
        print(f"  Breaking! Total exceeded 100")
        break
    num += 1

# ============================================
# 5. CONTINUE STATEMENT - Skip iteration
# ============================================
print("\n" + "=" * 60)
print("CONTINUE STATEMENT")
print("=" * 60)

# Skip even numbers
print("\nPrint only odd numbers (1-10):")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  {i}", end=" ")
print()

# Skip specific values
print("\nSkip multiples of 3:")
for i in range(1, 16):
    if i % 3 == 0:
        continue  # Skip multiples of 3
    print(f"  {i}", end=" ")
print()

# ============================================
# 6. NESTED LOOPS
# ============================================
print("\n" + "=" * 60)
print("NESTED LOOPS")
print("=" * 60)

# Multiplication table
print("\nMultiplication Table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:3}", end=" ")
    print()  # New line after each row

# Pattern printing
print("\nPattern 1 - Right triangle:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nPattern 2 - Number pyramid:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# ============================================
# 7. LOOP WITH ELSE
# ============================================
print("\n" + "=" * 60)
print("LOOP WITH ELSE (runs if no break)")
print("=" * 60)

# Example 1: Search for item
print("\nSearch for 'grape' in list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "grape":
        print("  Found grape!")
        break
else:
    print("  Grape not found in list")

# Example 2: Prime number check
print("\nCheck if 17 is prime:")
num = 17
for i in range(2, num):
    if num % i == 0:
        print(f"  {num} is NOT prime (divisible by {i})")
        break
else:
    print(f"  {num} is PRIME ✅")

# ============================================
# 8. PRACTICAL EXAMPLES
# ============================================
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Sum of numbers
print("\nExample 1: Sum of numbers 1 to 10")
total = 0
for i in range(1, 11):
    total += i
print(f"  Sum: {total}")

# Example 2: Factorial
print("\nExample 2: Factorial of 5")
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"  {number}! = {factorial}")

# Example 3: Count vowels
print("\nExample 3: Count vowels in string")
text = "Python Programming"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"  Text: '{text}'")
print(f"  Vowels count: {count}")

# Example 4: Reverse a string
print("\nExample 4: Reverse a string")
text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(f"  Original: {text}")
print(f"  Reversed: {reversed_text}")

# Example 5: Fibonacci sequence
print("\nExample 5: Fibonacci sequence (first 10 numbers)")
a, b = 0, 1
count = 0
print("  ", end="")
while count < 10:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()

# Example 6: Print even and odd separately
print("\nExample 6: Separate even and odd numbers")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(f"  Even numbers: {even}")
print(f"  Odd numbers: {odd}")

# Example 7: Find maximum in list
print("\nExample 7: Find maximum in list")
numbers = [45, 23, 89, 12, 67, 91, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"  Numbers: {numbers}")
print(f"  Maximum: {max_num}")

# ============================================
# 9. LOOP PATTERNS
# ============================================
print("\n" + "=" * 60)
print("COMMON LOOP PATTERNS")
print("=" * 60)

# Pattern 1: Square
print("\nPattern 1: 5×5 Square")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

# Pattern 2: Right triangle
print("\nPattern 2: Right Triangle")
for i in range(1, 6):
    print("* " * i)

# Pattern 3: Inverted right triangle
print("\nPattern 3: Inverted Right Triangle")
for i in range(5, 0, -1):
    print("* " * i)

# Pattern 4: Pyramid
print("\nPattern 4: Pyramid")
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "* " * i
    print(spaces + stars)

# Pattern 5: Diamond
print("\nPattern 5: Diamond")
# Upper half
for i in range(1, 5):
    print(" " * (5 - i) + "* " * i)
# Lower half
for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)

print("\n✅ Loops completed successfully!")
print("🎯 Practice these patterns and examples!")
#===========================================
#practice problems
#===========================================
#Q1. Print each character of a string on a new line
text = "python"
for char in text:
    print(char)
#============================================
#Q2. Count Characters
text = "vipin"
count = 0
for char in text:
    print(char)
    count += 1
print(f"  Total characters: {count}")
#============================================
#Q3. Count Characters
text = "python"
i=0
while i < len(text):
    print(text[i])
    i += 1
print(f"  Total characters: {i}")
#============================================
#Q3. Count Vowels
text = "education"
count = 0
for char in text:
    if char in "aeiouAEIOU":
        count += 1
        print(f"  Vowel: {char}")
        continue
    print(f"  Consonant: {char}")
print(f"  Total vowels: {count}")
#============================================
#Q5 Reverse String
text = "python"
reversed_text = ""
i=len(text) - 1
while i>=0:
    reversed_text += text[i]
    i = i- 1
print(f"  Original: {text}")
print(f"  Reversed: {reversed_text}")
#============================================
#Q6 Palindrome String Check
text = "madam"
new_text = ""
for ch in text:
    new_text = ch + new_text
    if new_text == text:
        print(f"  '{text}' is a palindrome")
print(f"  Original: {text}")
print(f"  Reversed: {new_text}")
#============================================
#Q7 PyThOn Count Uppercase Letters

text = "PyThOn"
count = 0
for i in range(len(text)):
 if text[i].isupper():
    print("Uppercase letter:", text[i])
 count = count + 1
print("count", count)
#============================================
# #Count Uppercase Letters (without len function)

text1 = "PyThOn"
count = 0
for ch in text1:
 if ch.isupper():
     print("Uppercase letter:",ch)
 count = count + 1
print("count", count)

# #=====================================
# # Count Uppercase Letters

text2 = "PyThOn"
i = 0
count = 0
while i < len(text):
 if text[i].isupper():
    print("Uppercase letter:",text[i])
    count +=1
    i +=1
print("count",count)

#=======================================
#Q7 Remove Spaces
text = "vipin yadav"
new_text = ""
i = 0
while i < len(text):
 if text[i] != " ":
     new_text += text[i]
 i += 1
print("Original:", text)
print("Without spaces:", new_text)
#=======================================
#Q8 Print Characters at Even Index
text = "vipinyadav"
i =0
while i < len(text):
 #print(text[i])
 if i%2 ==0 :
     print(text[i])
 i+=1
print("count",i)
#=======================================
#using FOR loop
text = "vipinyadav"
for i in range(len(text)):
 if i % 2 ==0:
    print("using for loop",text[i])
#=======================================
#using FOR loop
str1 = 'vipinyadav'
for x in range(0,len(str1),2):
 print("using range slicing", str1[x])
#=======================================
#=======================================
# Practice 2 - Skip Multiples of 3
for i in range(1, 16):
 if i % 3 == 0:
     continue
 print(i)
#=======================================
#Practice 3 — Username Checker
# username = ""
# while username != "vipin":
# username = input("Enter username: ")
# print("Welcome, vipin!")

# #======================================
# #second approach
# while True:
# username = input("Enter username: ")
# if username == "vipin":
# print("Welcome, vipin!")
# break
# print("Wrong username, try again...")
#=======================================
# Mini Challenge
# 🎯 Secret Number Game


# while true :
# number = int(input("enter a number"))
# if number == 7:
# print("correct")
# break
# print("enter number again")

num = ""
while num != 7:
 num = int(input("enter a number : "))
print("number is 7")

#===========================================
#second approach

secret = 7
while True:
 guess = int(input("Enter a number: "))
 if guess == secret:
     print("Correct Guess")
 break
#===============================================