# Conditional Expression :
# Conditional statements in Python are used to perform different actions based on different conditions.
# They allow a program to make decisions and execute specific blocks of code only when certain conditions are true.
# They work by evaluating a Boolean expression (True or False).

# Types of Conditional Statements in Python
# 1. if Statement :
#       Executes a block of code only if the condition is true.

# Syntax:
if condition:
    statement(s)


# Example:
age = 18
if age >= 18:
    print("You are eligible to vote.")


# 2. if...else Statement :
#       Executes one block if the condition is true, and another block if it is false.

# Syntax:
if condition:
    statement(s)
else:
    statement(s)

# Example:
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 3. if...elif...else Ladder :
#       Used when there are multiple conditions to check.

# Syntax:

if condition1:
    statement(s)
elif condition2:
    statement(s)
else:
    statement(s)


# Example:

marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


# 4. Nested if Statement
#       An if statement inside another if statement.

# Syntax:

if condition1:
    if condition2:
        statement(s)


# Example:

age = 20
citizen = True
if age >= 18:
    if citizen:
        print("Eligible to vote")
