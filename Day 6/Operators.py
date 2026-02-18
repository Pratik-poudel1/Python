# Relational Operators:
# Relational operators are used in conditional statements to compare two values.
# They return a Boolean result: True or False.
# These operators are commonly used inside if, if…else, and loops.


# Logical Operators in Python: 

# Logical operators are used to combine two or more conditions in conditional statements.
# They return a Boolean value: True or False.
# They are often used with relational operators inside if, if…else, loops, etc.

# Types Of Logical Operators Used in Condiional Statements :
# 1. and Operator:
#       Returns True only when both conditions are True.

# Syntax:
#       condition1 and condition2

# Example:

age = 20
citizen = True
if age >= 18 and citizen:
    print("Eligible to vote")

# Explanation:
# Both conditions are true → Output prints.


# 2. or Operator:
#       Returns True if any one condition is True.

# Syntax:
#       condition1 or condition2


# Example:
marks = 35
if marks >= 40 or marks == 35:
    print("Grace Pass")

# Explanation:
# One condition is true → Output prints.


# 3. not Operator:
#       Reverses the Boolean result.

# Syntax:
#       not condition

# Example:
is_raining = False
if not is_raining:
    print("Go outside")


# Explanation:
# not False → True → Statement executes.

# ========Truth Table=========
A	      B	   A and B	A or B
True	True	True	True
True	False	False	True
False	True	False	True
False	False	False	False


