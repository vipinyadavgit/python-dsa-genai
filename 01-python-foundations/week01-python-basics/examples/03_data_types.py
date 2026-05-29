"""
03 - Data Types in Python
Deep dive into Python data types

Topics covered:
- Numeric types (int, float, complex)
- String type
- Boolean type
- Type checking
"""

# ============================================
# 1. INTEGER (int) - Whole numbers
# ============================================
print("=" * 50)
print("INTEGER DATA TYPE")
print("=" * 50)

age = 25
year = 2026
negative_num = -100
large_num = 1000000

print(f"Age: {age}, Type: {type(age)}")
print(f"Year: {year}")
print(f"Negative: {negative_num}")
print(f"Large number: {large_num:,}")  # Formatted with commas

# ============================================
# 2. FLOAT - Decimal numbers
# ============================================
print("\n" + "=" * 50)
print("FLOAT DATA TYPE")
print("=" * 50)

price = 99.99
temperature = -3.5
pi = 3.14159
scientific = 2.5e3  # 2.5 * 10^3 = 2500

print(f"Price: ${price}")
print(f"Temperature: {temperature}°C")
print(f"Pi: {pi}")
print(f"Scientific notation (2.5e3): {scientific}")

# ============================================
# 3. COMPLEX - Complex numbers
# ============================================
print("\n" + "=" * 50)
print("COMPLEX DATA TYPE")
print("=" * 50)

complex_num = 3 + 4j
print(f"Complex number: {complex_num}")
print(f"Real part: {complex_num.real}")
print(f"Imaginary part: {complex_num.imag}")

# ============================================
# 4. STRING (str) - Text data
# ============================================
print("\n" + "=" * 50)
print("STRING DATA TYPE")
print("=" * 50)

name = "Vipin Yadav"
single_quotes = 'Python Programming'
multiline = """This is a
multiline
string"""

print(f"Name: {name}")
print(f"Single quotes: {single_quotes}")
print(f"Multiline:\n{multiline}")
print(f"Length of name: {len(name)}")

# ============================================
# 5. BOOLEAN (bool) - True/False
# ============================================
print("\n" + "=" * 50)
print("BOOLEAN DATA TYPE")
print("=" * 50)

is_learning = True
is_expert = False
result = 10 > 5  # Comparison returns boolean

print(f"Is learning: {is_learning}")
print(f"Is expert: {is_expert}")
print(f"10 > 5 = {result}")
print(f"Type: {type(is_learning)}")

# ============================================
# 6. TYPE CHECKING
# ============================================
print("\n" + "=" * 50)
print("TYPE CHECKING")
print("=" * 50)

variables = [42, 3.14, "Hello", True, 3+4j]

for var in variables:
    print(f"Value: {var:15} | Type: {type(var).__name__}")

# Using isinstance()
print(f"\nIs 42 an integer? {isinstance(42, int)}")
print(f"Is 3.14 a float? {isinstance(3.14, float)}")
print(f"Is 'Hello' a string? {isinstance('Hello', str)}")

# ============================================
# 7. NONE TYPE - Represents absence of value
# ============================================
print("\n" + "=" * 50)
print("NONE TYPE")
print("=" * 50)

nothing = None
print(f"Value: {nothing}")
print(f"Type: {type(nothing)}")
print(f"Is None? {nothing is None}")

# ============================================
# PRACTICE EXERCISES
# ============================================
print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# Exercise 1: Create variables of each type
my_int = 100
my_float = 75.5
my_string = "Data Types"
my_bool = True

print(f"Integer: {my_int}")
print(f"Float: {my_float}")
print(f"String: {my_string}")
print(f"Boolean: {my_bool}")

# Exercise 2: Type checking all variables
print(f"\nType of my_int: {type(my_int).__name__}")
print(f"Type of my_float: {type(my_float).__name__}")
print(f"Type of my_string: {type(my_string).__name__}")
print(f"Type of my_bool: {type(my_bool).__name__}")

print("\n✅ Data types completed successfully!")
