"""
06 - Type Conversion in Python
Learn how to convert between different data types

Topics covered:
- Implicit type conversion
- Explicit type conversion
- Converting to int, float, str, bool
- Handling conversion errors
"""

# ============================================
# 1. IMPLICIT TYPE CONVERSION (Automatic)
# ============================================
print("=" * 60)
print("IMPLICIT TYPE CONVERSION")
print("=" * 60)

# Python automatically converts int to float when needed
int_num = 10
float_num = 5.5

result = int_num + float_num
print(f"Integer: {int_num} (type: {type(int_num).__name__})")
print(f"Float: {float_num} (type: {type(float_num).__name__})")
print(f"Result: {result} (type: {type(result).__name__})")
print("→ Python automatically converted int to float!")

# ============================================
# 2. CONVERTING TO INTEGER - int()
# ============================================
print("\n" + "=" * 60)
print("CONVERTING TO INTEGER - int()")
print("=" * 60)

# String to int
str_num = "42"
int_num = int(str_num)
print(f"String '{str_num}' → int {int_num}")

# Float to int (truncates decimal part)
float_num = 3.99
int_from_float = int(float_num)
print(f"Float {float_num} → int {int_from_float} (decimal removed)")

# Boolean to int
bool_true = True
bool_false = False
print(f"Boolean True → int {int(bool_true)}")
print(f"Boolean False → int {int(bool_false)}")

# Binary, Octal, Hex to int
binary = "1010"
octal = "12"
hexadecimal = "A"
print(f"\nBinary '{binary}' → int {int(binary, 2)}")
print(f"Octal '{octal}' → int {int(octal, 8)}")
print(f"Hex '{hexadecimal}' → int {int(hexadecimal, 16)}")

# ============================================
# 3. CONVERTING TO FLOAT - float()
# ============================================
print("\n" + "=" * 60)
print("CONVERTING TO FLOAT - float()")
print("=" * 60)

# String to float
str_decimal = "3.14"
float_num = float(str_decimal)
print(f"String '{str_decimal}' → float {float_num}")

# Integer to float
int_num = 42
float_from_int = float(int_num)
print(f"Integer {int_num} → float {float_from_int}")

# Boolean to float
print(f"Boolean True → float {float(True)}")
print(f"Boolean False → float {float(False)}")

# Scientific notation
scientific = "2.5e3"
print(f"Scientific '{scientific}' → float {float(scientific)}")

# ============================================
# 4. CONVERTING TO STRING - str()
# ============================================
print("\n" + "=" * 60)
print("CONVERTING TO STRING - str()")
print("=" * 60)

# Integer to string
num = 42
str_num = str(num)
print(f"Integer {num} → string '{str_num}'")

# Float to string
pi = 3.14159
str_pi = str(pi)
print(f"Float {pi} → string '{str_pi}'")

# Boolean to string
print(f"Boolean True → string '{str(True)}'")
print(f"Boolean False → string '{str(False)}'")

# List to string
my_list = [1, 2, 3]
str_list = str(my_list)
print(f"List {my_list} → string '{str_list}'")

# ============================================
# 5. CONVERTING TO BOOLEAN - bool()
# ============================================
print("\n" + "=" * 60)
print("CONVERTING TO BOOLEAN - bool()")
print("=" * 60)

# Numbers to boolean
print(f"bool(0) = {bool(0)} (0 is False)")
print(f"bool(1) = {bool(1)}")
print(f"bool(42) = {bool(42)} (any non-zero is True)")
print(f"bool(-5) = {bool(-5)}")

# Strings to boolean
print(f"\nbool('') = {bool('')} (empty string is False)")
print(f"bool('Hello') = {bool('Hello')} (non-empty is True)")
print(f"bool('0') = {bool('0')} (even '0' string is True!)")

# Collections to boolean
print(f"\nbool([]) = {bool([])} (empty list is False)")
print(f"bool([1, 2]) = {bool([1, 2])} (non-empty is True)")
print(f"bool({{}}) = {bool({})} (empty dict is False)")

# None to boolean
print(f"\nbool(None) = {bool(None)} (None is False)")

# ============================================
# 6. PRACTICAL EXAMPLES
# ============================================
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: User input conversion
print("\nExample 1: Age Calculator")
# In real scenario: birth_year_str = input("Enter birth year: ")
birth_year_str = "1998"  # Simulating user input
birth_year = int(birth_year_str)  # Convert to int
current_year = 2026
age = current_year - birth_year
print(f"Birth year (string): '{birth_year_str}'")
print(f"Birth year (int): {birth_year}")
print(f"Your age: {age} years")

# Example 2: Price calculation
print("\nExample 2: Price Calculation")
# price_str = input("Enter price: ")
price_str = "1299.99"  # Simulating user input
price = float(price_str)  # Convert to float
tax = price * 0.18
total = price + tax
print(f"Price (string): '{price_str}'")
print(f"Price (float): ₹{price:.2f}")
print(f"Tax (18%): ₹{tax:.2f}")
print(f"Total: ₹{total:.2f}")

# Example 3: Building messages
print("\nExample 3: Building Messages")
name = "Vipin"
age = 25
score = 95.5
is_passed = True

message = name + " is " + str(age) + " years old."
message += " Score: " + str(score)
message += " Passed: " + str(is_passed)
print(message)

# Better way with f-strings (no conversion needed!)
better_message = f"{name} is {age} years old. Score: {score} Passed: {is_passed}"
print(f"Better: {better_message}")

# ============================================
# 7. HANDLING CONVERSION ERRORS
# ============================================
print("\n" + "=" * 60)
print("HANDLING CONVERSION ERRORS")
print("=" * 60)

# Invalid conversions will raise errors
print("\nValid conversions:")
print(f"int('42') = {int('42')} ✅")
print(f"float('3.14') = {float('3.14')} ✅")

print("\nInvalid conversions (would raise errors):")
print("int('hello') → ValueError ❌")
print("int('3.14') → ValueError (use float first) ❌")
print("float('abc') → ValueError ❌")

# Safe conversion with try-except (we'll learn this later)
print("\nSafe conversion example:")
value = "abc"
try:
    result = int(value)
    print(f"Converted: {result}")
except ValueError:
    print(f"Cannot convert '{value}' to integer ❌")

value = "42"
try:
    result = int(value)
    print(f"Converted '{value}' to {result} ✅")
except ValueError:
    print(f"Cannot convert '{value}' to integer ❌")

# ============================================
# 8. CONVERSION SUMMARY TABLE
# ============================================
print("\n" + "=" * 60)
print("CONVERSION SUMMARY")
print("=" * 60)

print("""
Function    Purpose                 Example
--------    -------                 -------
int()       Convert to integer      int('42') → 42
float()     Convert to float        float('3.14') → 3.14
str()       Convert to string       str(42) → '42'
bool()      Convert to boolean      bool(1) → True

Common conversions:
• String to number: int('42'), float('3.14')
• Number to string: str(42), str(3.14)
• Float to int: int(3.99) → 3 (truncates)
• Int to float: float(42) → 42.0
""")

print("✅ Type conversion completed successfully!")
