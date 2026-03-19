# Functions and Recursions

# Functions :
# A function is a block of organized, reusable code used to perform a single task.

# Why use functions?
# 1. Avoid repetition
# 2. Make code modular
# 3. Easy to debug
# 4. Improves readability

# Syntax : 
        # def func():
        #     print("Hello")
        # func()

# Defining a Function
def greet():
    print("Hello, Welcome to Python!")

# Calling a Function
greet()


# Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)


# Types of Functions
# 1. Built-in functions → print(), len(), type()
# 2. User-defined functions → Created using def
# 3. Lambda functions → Anonymous functions

# Example of lambda:

square = lambda x: x * x
print(square(4))

# Functions with Arguments :
# A Function can accept some values it can work with.
# We can put these values in the parentheses.

# Function with Arguments Example :
def greet(name):
    print("Hello", name)
    return "Thankyou"

greet("Pratik")
a=greet("Ram")
print(a)

# Default Parameter Value :
# We can have a value as default as default argument in a function.

# Example :
def greet(name="stranger"):
    print("Good Day",name)

greet() # name will be 'stranger' in function body(default)
greet("Pratik") # name will be "Pratik" in function body(passed)
