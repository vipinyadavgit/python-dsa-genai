"""
07 - if-else Statements in Python
Learn conditional statements and decision making

Topics covered:
- if statement
- if-else statement
- if-elif-else statement
- Nested if statements
- Ternary operator
"""

# ============================================
# 1. BASIC IF STATEMENT
# ============================================
print("=" * 60)
print("BASIC IF STATEMENT")
print("=" * 60)

age = 20

if age >= 18:
    print(f"Age is {age}")
    print("You are an adult! ✅")

print("This line always executes\n")

# Another example
temperature = 35

if temperature > 30:
    print(f"Temperature: {temperature}°C")
    print("It's hot outside! 🌡️")

# ============================================
# 2. IF-ELSE STATEMENT
# ============================================
print("\n" + "=" * 60)
print("IF-ELSE STATEMENT")
print("=" * 60)

score = 75

if score >= 40:
    print(f"Score: {score}")
    print("Result: PASS ✅")
else:
    print(f"Score: {score}")
    print("Result: FAIL ❌")

# Another example
number = 7

if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")

# ============================================
# 3. IF-ELIF-ELSE STATEMENT (Multiple conditions)
# ============================================
print("\n" + "=" * 60)
print("IF-ELIF-ELSE STATEMENT")
print("=" * 60)

marks = 85

if marks >= 90:
    grade = "A+"
    print(f"Marks: {marks} → Grade: {grade} (Excellent!)")
elif marks >= 80:
    grade = "A"
    print(f"Marks: {marks} → Grade: {grade} (Very Good!)")
elif marks >= 70:
    grade = "B"
    print(f"Marks: {marks} → Grade: {grade} (Good!)")
elif marks >= 60:
    grade = "C"
    print(f"Marks: {marks} → Grade: {grade} (Average)")
elif marks >= 40:
    grade = "D"
    print(f"Marks: {marks} → Grade: {grade} (Pass)")
else:
    grade = "F"
    print(f"Marks: {marks} → Grade: {grade} (Fail)")

# Another example: Days of week
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number!")

# ============================================
# 4. NESTED IF STATEMENTS
# ============================================
print("\n" + "=" * 60)
print("NESTED IF STATEMENTS")
print("=" * 60)

age = 25
has_license = True

if age >= 18:
    print(f"Age: {age} - You are an adult")
    
    if has_license:
        print("You have a license")
        print("✅ You can drive!")
    else:
        print("You don't have a license")
        print("❌ Get a license first!")
else:
    print(f"Age: {age} - You are a minor")
    print("❌ Too young to drive!")

# Another example: Login system
username = "admin"
password = "pass123"

if username == "admin":
    print("Username is correct ✅")
    
    if password == "pass123":
        print("Password is correct ✅")
        print("🎉 Login Successful!")
    else:
        print("Password is incorrect ❌")
else:
    print("Username not found ❌")

# ============================================
# 5. MULTIPLE CONDITIONS (and, or, not)
# ============================================
print("\n" + "=" * 60)
print("MULTIPLE CONDITIONS")
print("=" * 60)

# AND operator - Both conditions must be True
age = 25
salary = 50000

if age >= 21 and salary >= 30000:
    print(f"Age: {age}, Salary: ₹{salary}")
    print("✅ Eligible for loan!")
else:
    print(f"Age: {age}, Salary: ₹{salary}")
    print("❌ Not eligible for loan")

# OR operator - At least one condition must be True
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("🎉 It's a day off! Enjoy!")
else:
    print("📚 It's a working day")

# NOT operator - Reverses the condition
is_raining = False

if not is_raining:
    print("☀️ No rain, let's go out!")
else:
    print("🌧️ It's raining, stay inside")

# Complex conditions
temperature = 25
is_sunny = True
has_time = True

if temperature >= 20 and temperature <= 30 and is_sunny and has_time:
    print(f"🏖️ Perfect weather ({temperature}°C) for a picnic!")
else:
    print("Maybe next time...")

# ============================================
# 6. TERNARY OPERATOR (Shorthand if-else)
# ============================================
print("\n" + "=" * 60)
print("TERNARY OPERATOR (One-line if-else)")
print("=" * 60)

# Syntax: value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age} → Status: {status}")

# Another example
number = 15
result = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {result}")

# With calculations
a = 10
b = 20
max_value = a if a > b else b
print(f"Maximum of {a} and {b} is {max_value}")

# Nested ternary (not recommended, but possible)
score = 75
grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "D"))
print(f"Score: {score} → Grade: {grade}")

# ============================================
# 7. PRACTICAL EXAMPLES
# ============================================
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Discount calculator
print("\nExample 1: Discount Calculator")
total_amount = 5000
is_member = True

if total_amount >= 10000:
    discount = 0.25  # 25% discount
    print(f"Discount: 25% (Purchase ≥ ₹10,000)")
elif total_amount >= 5000:
    discount = 0.15  # 15% discount
    print(f"Discount: 15% (Purchase ≥ ₹5,000)")
elif is_member:
    discount = 0.10  # 10% for members
    print(f"Discount: 10% (Member)")
else:
    discount = 0.05  # 5% default
    print(f"Discount: 5% (Regular)")

final_amount = total_amount - (total_amount * discount)
print(f"Original: ₹{total_amount}")
print(f"Final Amount: ₹{final_amount}")

# Example 2: Temperature classifier
print("\nExample 2: Temperature Classifier")
temp = 35

if temp >= 40:
    category = "Extreme Heat 🔥"
elif temp >= 30:
    category = "Hot 🌡️"
elif temp >= 20:
    category = "Warm ☀️"
elif temp >= 10:
    category = "Cool 🍂"
else:
    category = "Cold ❄️"

print(f"Temperature: {temp}°C → {category}")

# Example 3: Largest of three numbers
print("\nExample 3: Largest of Three Numbers")
num1, num2, num3 = 45, 78, 32

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"Numbers: {num1}, {num2}, {num3}")
print(f"Largest: {largest}")

# Example 4: Leap year checker
print("\nExample 4: Leap Year Checker")
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a LEAP year ✅")
else:
    print(f"{year} is NOT a leap year ❌")

# Example 5: Login validation
print("\nExample 5: Login Validation")
entered_user = "vipin"
entered_pass = "python123"
correct_user = "vipin"
correct_pass = "python123"

if entered_user == correct_user:
    if entered_pass == correct_pass:
        print("✅ Login Successful!")
        print("Welcome, Vipin!")
    else:
        print("❌ Incorrect password")
else:
    print("❌ User not found")

# ============================================
# 8. COMMON PATTERNS
# ============================================
print("\n" + "=" * 60)
print("COMMON PATTERNS")
print("=" * 60)

# Pattern 1: Range check
number = 50
if 1 <= number <= 100:
    print(f"{number} is between 1 and 100 ✅")

# Pattern 2: Value in list
fruit = "apple"
fruits = ["apple", "banana", "cherry"]
if fruit in fruits:
    print(f"'{fruit}' found in list ✅")

# Pattern 3: Check type
value = 42
if isinstance(value, int):
    print(f"{value} is an integer ✅")

# Pattern 4: None check
result = None
if result is None:
    print("Result is None ✅")

print("\n✅ if-else statements completed successfully!")
