'''
A ternary operator is a short one-line version of if-else.
'''
from operator import truediv

age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)

#   Structure:-
'''
value_if_true if condition else value_if_false
'''
#Login example
logged_in = True
message = "Welcome" if logged_in else "Please Login"
print(message)

#odd even
num= int(input("Enter a number: "))
result = "even" if num%2==0 else "odd"
print(result)


#age check
age = int(input("Enter your age: "))
result = "Adult" if age >= 18 else "Minor"
print(result)

#pass fail
num = int(input("Enter a number: "))
result = "pass" if num>=40 else "fail"
print(result)

#largest number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = {num1} if num1>num2 else {num2}
print('largest number is:-',result)