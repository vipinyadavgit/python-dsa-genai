# Python Notes (Lessons 1–12)

## 1. Variables

### Definition

A variable is a container used to store data.

```python
name = "Vipin"
age = 25
```

---

## 2. Data Types

### String (str)

Stores text.

```python
name = "Vipin"
```

### Integer (int)

Stores whole numbers.

```python
age = 25
```

### Float (float)

Stores decimal numbers.

```python
price = 99.99
```

### Boolean (bool)

Stores True or False.

```python
is_logged_in = True
```

---

## 3. Type Checking

### Syntax

```python
# type(variable)
```

### Example

```python
x = 10
print(type(x))
```

Output:

```python
# <class 'int'>
```

---

## 4. Type Casting

### Definition

Converting one data type into another.

### Examples

```python
int("10")
float("10")
str(10)
```

### Common Usage

```python
num = int(input("Enter a number: "))
```

---

## 5. Input and Output

### Input

```python
name = input("Enter your name: ")
```

### Output

```python
# print(name)
```

### f-string

```python
name = "Vipin"
age = 25

print(f"My name is {name} and I am {age} years old")
```

---

# Operators

## 6. Arithmetic Operators

| Operator | Meaning        |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| //       | Floor Division |
| %        | Modulus        |
| **       | Power          |

### Examples

```python
10 + 5
10 - 5
10 * 5
10 / 5
10 // 3
10 % 3
10 ** 2
```

---

## 7. Comparison Operators

| Operator | Meaning            |
| -------- | ------------------ |
| ==       | Equal              |
| !=       | Not Equal          |
| >        | Greater Than       |
| <        | Less Than          |
| >=       | Greater Than Equal |
| <=       | Less Than Equal    |

### Example

```python
10 > 5
```

Output:

```python
True
```

---

## 8. Logical Operators

### and

```python
# age >= 18 and has_id == "yes"
```

Both conditions must be True.

### or

```python
# marks >= 90 or sports_quota == "yes"
```

Any one condition can be True.

### not

```python
not True
```

Output:

```python
False
```

---

## 9. Ternary Operator

### Definition

Short form of if-else.

### Syntax

```python
# value_if_true if condition else value_if_false
```

### Example

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

---

# Conditional Statements

## 10. if-else

### Syntax

```python
'''
if condition:
    statement
else:
    statement
    '''
```

### Example

```python
'''
if age >= 18:
    print("Adult")
else:
    print("Minor")
'''
```

---

## 11. Nested if

### Example

```python
'''if card_inserted == "yes":
    if pin == "1234":
        print("Access Granted")
'''
```

---

# Loops

## 12. for Loop

### Syntax

```python
#for i in range(start, stop, step):
#    print(i)
```

### Example

```python
for i in range(1, 6):
    print(i)
```

---

### Common range() Usage

```python
range(5)
range(1, 6)
range(1, 11, 2)
range(10, 0, -1)
```

---

## 13. while Loop

### Syntax

```python
'''
while condition:
    statement
'''
```

### Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

## 14. break

Stops loop immediately.

```python
for i in range(10):
    if i == 5:
        break
```

---

## 15. continue

Skips current iteration.

```python
for i in range(10):
    if i == 5:
        continue
```

---

# Strings

## 16. String Basics

### Definition

A string is a collection of characters.

```python
name = "Python"
```

---

## 17. String Traversal

### Using for Loop

```python
for ch in "Python":
    print(ch)
```

### Using while Loop

```python
text = "Python"

i = 0

while i < len(text):
    print(text[i])
    i += 1
```

---

## 18. len()

Returns length of a string.

```python
len("Python")
```

Output:

```python
6
```

---

## 19. Useful String Methods

### Lowercase

```python
# text.lower()
```

### Uppercase

```python
# text.upper()
```

### Check Alphabet

```python
# text.isalpha()
```

### Check Digit

```python
# text.isdigit()
```

### Check Uppercase

```python
# text.isupper()
```

### Check Lowercase

```python
# text.islower()
```

---

## 20. String Practice Problems Covered

* Count characters
* Count vowels
* Count uppercase letters
* Reverse string
* Palindrome string
* Remove spaces
* Print alternate characters

---

# Nested Loops

## 21. Nested Loop Syntax

```python
'''
for i in range(rows):
    for j in range(cols):
        print("*")
'''
```

---

# Pattern Programming

## Pattern 1

```text
*
**
***
****
*****
```

```python
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()
```

---

## Pattern 2

```text
1
12
123
1234
12345
```

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

---

## Pattern 3

```text
*****
****
***
**
*
```

```python
for i in range(5):
    for j in range(i, 5):
        print("*", end="")
    print()
```

---

## Pattern 4

```text
1
22
333
4444
55555
```

```python
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()
```

---

# Number Logic

## 22. Digit Extraction

### Get Last Digit

```python
# digit = num % 10
```

### Example

```python
1234 % 10
```

Output:

```python
4
```

---

## 23. Remove Last Digit

```python
# num = num // 10
```

### Example

```python
1234 // 10
```

Output:

```python
123
```

---

## 24. Count Digits

```python
num = 12345

count = 0

while num > 0:
    count += 1
    num = num // 10

print(count)
```

Output:

```python
5
```

---

## 25. Sum of Digits

```python
num = 1234

sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print(sum_digits)
```

Output:

```python
10
```

---

## 26. Reverse Number

```python
num = 1234

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)
```

Output:

```python
4321
```

---

## 27. Palindrome Number

### Definition

A number that remains same after reversing.

Examples:

```text
121
1331
12321
```

### Program

```python
num = 121

temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
```

---

# Important Concepts Learned

✅ Variables

✅ Data Types

✅ Type Casting

✅ Input / Output

✅ Arithmetic Operators

✅ Comparison Operators

✅ Logical Operators

✅ Ternary Operator

✅ if-else

✅ Nested if

✅ for Loop

✅ while Loop

✅ break

✅ continue

✅ Strings

✅ String Traversal

✅ Nested Loops

✅ Pattern Programming

✅ Digit Extraction

✅ Count Digits

✅ Sum of Digits

✅ Reverse Number

✅ Palindrome Number

---

# Current Level

You can now:

* Write basic Python programs
* Use conditions effectively
* Work with loops confidently
* Solve beginner logic problems
* Solve basic number-based DSA problems
* Work with strings
* Create simple pattern programs
* Debug simple syntax and logic errors

Current Stage:

```text
Python Beginner → Beginner+
```

Next Topic:

```text
Lesson 13: Lists
```
