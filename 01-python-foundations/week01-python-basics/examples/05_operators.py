"""
05 - Operators in Python
All types of operators with examples

Topics covered:
- Arithmetic operators
- Comparison operators
- Logical operators
- Assignment operators
- Identity operators
- Membership operators
"""

# ============================================
# 1. ARITHMETIC OPERATORS
# ============================================
print("=" * 60)
print("ARITHMETIC OPERATORS")
print("=" * 60)

a = 20
b = 3

print(f"a = {a}, b = {b}\n")
print(f"Addition       : {a} + {b} = {a + b}")
print(f"Subtraction    : {a} - {b} = {a - b}")
print(f"Multiplication : {a} × {b} = {a * b}")
print(f"Division       : {a} ÷ {b} = {a / b:.2f}")
print(f"Floor Division : {a} ÷÷ {b} = {a // b}")  # Quotient without decimal
print(f"Modulus        : {a} % {b} = {a % b}")    # Remainder
print(f"Exponentiation : {a} ** {b} = {a ** b}")  # Power

# ============================================
# 2. COMPARISON OPERATORS
# ============================================
print("\n" + "=" * 60)
print("COMPARISON OPERATORS (Return True/False)")
print("=" * 60)

x = 10
y = 20

print(f"x = {x}, y = {y}\n")
print(f"Equal to              : {x} == {y} = {x == y}")
print(f"Not equal to          : {x} != {y} = {x != y}")
print(f"Greater than          : {x} > {y} = {x > y}")
print(f"Less than             : {x} < {y} = {x < y}")
print(f"Greater than or equal : {x} >= {y} = {x >= y}")
print(f"Less than or equal    : {x} <= {y} = {x <= y}")

# ============================================
# 3. LOGICAL OPERATORS
# ============================================
print("\n" + "=" * 60)
print("LOGICAL OPERATORS (and, or, not)")
print("=" * 60)

p = True
q = False

print(f"p = {p}, q = {q}\n")
print(f"p AND q : {p} and {q} = {p and q}")
print(f"p OR q  : {p} or {q} = {p or q}")
print(f"NOT p   : not {p} = {not p}")
print(f"NOT q   : not {q} = {not q}")

# Practical example
age = 25
has_license = True
print(f"\nAge = {age}, Has License = {has_license}")
print(f"Can drive? (age >= 18 and has_license) = {age >= 18 and has_license}")

# ============================================
# 4. ASSIGNMENT OPERATORS
# ============================================
print("\n" + "=" * 60)
print("ASSIGNMENT OPERATORS")
print("=" * 60)

num = 10
print(f"Initial value: num = {num}")

num += 5  # num = num + 5
print(f"After num += 5  : num = {num}")

num -= 3  # num = num - 3
print(f"After num -= 3  : num = {num}")

num *= 2  # num = num * 2
print(f"After num *= 2  : num = {num}")

num /= 4  # num = num / 4
print(f"After num /= 4  : num = {num}")

num //= 2  # num = num // 2
print(f"After num //= 2 : num = {num}")

num %= 3  # num = num % 3
print(f"After num %= 3  : num = {num}")

num **= 3  # num = num ** 3
print(f"After num **= 3 : num = {num}")

# ============================================
# 5. IDENTITY OPERATORS
# ============================================
print("\n" + "=" * 60)
print("IDENTITY OPERATORS (is, is not)")
print("=" * 60)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1\n")

print(f"list1 == list2 (same values)  : {list1 == list2}")
print(f"list1 is list2 (same object)  : {list1 is list2}")
print(f"list1 is list3 (same object)  : {list1 is list3}")
print(f"list1 is not list2            : {list1 is not list2}")

# ============================================
# 6. MEMBERSHIP OPERATORS
# ============================================
print("\n" + "=" * 60)
print("MEMBERSHIP OPERATORS (in, not in)")
print("=" * 60)

fruits = ["apple", "banana", "cherry"]
text = "Python Programming"

print(f"Fruits list: {fruits}")
print(f"Text: '{text}'\n")

print(f"'apple' in fruits        : {'apple' in fruits}")
print(f"'mango' in fruits        : {'mango' in fruits}")
print(f"'mango' not in fruits    : {'mango' not in fruits}")
print(f"'Python' in text         : {'Python' in text}")
print(f"'Java' not in text       : {'Java' not in text}")

# ============================================
# 7. OPERATOR PRECEDENCE
# ============================================
print("\n" + "=" * 60)
print("OPERATOR PRECEDENCE")
print("=" * 60)

result1 = 10 + 5 * 2  # * has higher precedence
result2 = (10 + 5) * 2  # Parentheses first

print(f"10 + 5 * 2       = {result1}")
print(f"(10 + 5) * 2     = {result2}")

# Complex expression
result3 = 2 ** 3 + 10 / 5 - 3 * 2
print(f"2 ** 3 + 10 / 5 - 3 * 2 = {result3}")
print("Order: ** → / → * → + → -")

# ============================================
# PRACTICAL EXAMPLES
# ============================================
print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Check if number is even
number = 42
is_even = (number % 2 == 0)
print(f"\n{number} is even? {is_even}")

# Example 2: Check eligibility
age = 25
income = 50000
eligible = (age >= 18) and (income >= 30000)
print(f"\nAge: {age}, Income: {income}")
print(f"Eligible for loan? {eligible}")

# Example 3: Temperature check
temp = 35
is_hot = temp > 30
is_cold = temp < 15
is_comfortable = not (is_hot or is_cold)
print(f"\nTemperature: {temp}°C")
print(f"Is hot? {is_hot}")
print(f"Is cold? {is_cold}")
print(f"Is comfortable? {is_comfortable}")

# Example 4: Calculate discount
price = 1000
is_member = True
discount = 0.2 if is_member else 0.1
final_price = price - (price * discount)
print(f"\nOriginal Price: ₹{price}")
print(f"Is Member: {is_member}")
print(f"Discount: {discount * 100}%")
print(f"Final Price: ₹{final_price}")

# Example 5: Check range
score = 85
passed = score >= 40
grade_a = score >= 90
grade_b = 80 <= score < 90
grade_c = 70 <= score < 80
print(f"\nScore: {score}")
print(f"Passed? {passed}")
print(f"Grade A? {grade_a}")
print(f"Grade B? {grade_b}")
print(f"Grade C? {grade_c}")

print("\n✅ Operators completed successfully!")
