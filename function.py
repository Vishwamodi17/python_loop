# WHAT IS THE FUNCTION ?
# A function is a reusable block of code that performs a specific task.
# Instead of writing the same code again and again, you can put it inside a function and use it whenever needed.

# WHY USE FUNCTION ?
# We use functions in programming to make our code better, cleaner, and easier to manage
# 1. avoid rewriting the code

# SYNTAX
# def function_name(parameters):
#      code block
#     return value

# EXAMPLE 
def greet():
    print("hello world")
greet()


# ANOTHER EXAMPLE
def greet(name="student"):
    print("hello", name)

greet()
greet("vishwa")

# function with return value
# used when we want to send result back
def add(a, b):
    return a + b

result = add(2, 3)
print(result)

# TASK 1
# create a function to calculate and return result
def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        return "Invalid operation"

print(calculate(10, 5, "add")) 
print(calculate(10, 5, "mul"))  

# TASK 2
# create a function to check if a number is even or odd
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
result = even_odd(number)
print("The number is:", result)

# TASK 3
# create a function to find the factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print(factorial(5))


# TASK 4
# create a function to write a maximum of three number
def max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
result = max(x, y, z)
print("Maximum number is:", result)

# TASK 5
# create a function to check if the string is palindrome or not
def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]

input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("It is a palindrome")
else:
    print("Not a palindrome")

# TASK 6
# create a function to calculate the area of circle
def circle(radius):
    pi = 3.14
    return pi * radius * radius

r = float(input("Enter radius: "))
print("Area of circle is:",circle(r))

