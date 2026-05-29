"""
02 - Variables and Data Types
Learn about Python variables and basic data types
"""

# Integer
age = 25
print(f"Age: {age}, Type: {type(age)}")

# Float
price = 99.99
print(f"Price: {price}, Type: {type(price)}")

# String
name = "Vipin Yadav"
print(f"Name: {name}, Type: {type(name)}")

# Boolean
is_learning = True
print(f"Is Learning: {is_learning}, Type: {type(is_learning)}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Same value to multiple variables
a = b = c = 100
print(f"a={a}, b={b}, c={c}")

# Type conversion
num_str = "42"
num_int = int(num_str)
print(f"String '{num_str}' converted to int: {num_int}")

# Input from user
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

print("\n✅ Variables and data types completed!")
