"""
04 - Input and Output in Python
Learn how to get user input and display output

Topics covered:
- print() function
- input() function
- Formatting output
- f-strings
"""

# ============================================
# 1. PRINT FUNCTION - Display output
# ============================================
print("=" * 50)
print("PRINT FUNCTION")
print("=" * 50)

# Basic print
print("Hello, World!")

# Print multiple items
print("Name:", "Vipin", "Age:", 25)

# Print with separator
print("Python", "Java", "JavaScript", sep=" | ")

# Print with custom end (default is newline)
print("Loading", end="...")
print("Done!")

# Print without newline
print("Same ", end="")
print("line!")

# ============================================
# 2. STRING FORMATTING
# ============================================
print("\n" + "=" * 50)
print("STRING FORMATTING")
print("=" * 50)

name = "Vipin"
age = 25
city = "Bangalore"

# Method 1: Concatenation (not recommended)
print("Name: " + name + ", Age: " + str(age))

# Method 2: format() method
print("Name: {}, Age: {}, City: {}".format(name, age, city))

# Method 3: f-strings (RECOMMENDED - Python 3.6+)
print(f"Name: {name}, Age: {age}, City: {city}")

# ============================================
# 3. F-STRING ADVANCED
# ============================================
print("\n" + "=" * 50)
print("F-STRING ADVANCED")
print("=" * 50)

price = 1234.5678

# Formatting numbers
print(f"Price: ${price:.2f}")  # 2 decimal places
print(f"Price: ${price:,.2f}")  # With comma separator

# Alignment
print(f"{'Left':<10}|")   # Left aligned
print(f"{'Center':^10}|")  # Center aligned
print(f"{'Right':>10}|")   # Right aligned

# Expressions in f-strings
a = 10
b = 20
print(f"Sum: {a} + {b} = {a + b}")
print(f"Product: {a} × {b} = {a * b}")

# ============================================
# 4. INPUT FUNCTION - Get user input
# ============================================
print("\n" + "=" * 50)
print("INPUT FUNCTION")
print("=" * 50)

# UNCOMMENT BELOW TO TRY INTERACTIVE INPUT
# Note: Input always returns a string!

# Example 1: String input
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# Example 2: Number input (need to convert)
# age_str = input("Enter your age: ")
# age_int = int(age_str)
# print(f"Next year you will be {age_int + 1}")

# Example 3: Multiple inputs on one line
# name, city = input("Enter name and city (separated by space): ").split()
# print(f"{name} lives in {city}")

# ============================================
# 5. PRACTICAL EXAMPLES
# ============================================
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Display formatted information
print("\n--- User Profile ---")
username = "vipin_yadav"
email = "vipin@example.com"
role = "Python Developer"
experience = 2

print(f"Username    : {username}")
print(f"Email       : {email}")
print(f"Role        : {role}")
print(f"Experience  : {experience} years")

# Example 2: Display calculation results
print("\n--- Calculation ---")
num1 = 45
num2 = 12

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} × {num2} = {num1 * num2}")
print(f"{num1} ÷ {num2} = {num1 / num2:.2f}")

# Example 3: Display table
print("\n--- Price Table ---")
print(f"{'Item':<15} {'Quantity':>10} {'Price':>10}")
print("-" * 35)
print(f"{'Laptop':<15} {1:>10} {65000:>10,}")
print(f"{'Mouse':<15} {2:>10} {500:>10,}")
print(f"{'Keyboard':<15} {1:>10} {1500:>10,}")

# ============================================
# COMMENTED INTERACTIVE EXAMPLES
# ============================================
print("\n" + "=" * 50)
print("INTERACTIVE EXAMPLES (COMMENTED)")
print("=" * 50)
print("Uncomment the code below to try interactive input!\n")

# # Example 1: Simple greeting
# name = input("What is your name? ")
# print(f"Nice to meet you, {name}!")

# # Example 2: Age calculator
# birth_year = int(input("Enter your birth year: "))
# current_year = 2026
# age = current_year - birth_year
# print(f"You are {age} years old!")

# # Example 3: Simple calculator
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# print(f"\nResults:")
# print(f"{num1} + {num2} = {num1 + num2}")
# print(f"{num1} - {num2} = {num1 - num2}")
# print(f"{num1} × {num2} = {num1 * num2}")
# print(f"{num1} ÷ {num2} = {num1 / num2:.2f}")

# # Example 4: Personal info
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")
# 
# print("\n--- Your Profile ---")
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"City: {city}")
# print(f"In 5 years, you will be {age + 5} years old!")

print("\n✅ Input/Output completed successfully!")
