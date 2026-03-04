# Pip Freeze Command:
# 'pip freeze' returns all the package installed in a given python environment
# along with the versions of the packages.

# To run the pip freeze command, we need to use the command:
# - pip freeze

# Tp create a file  named requirements.txt, we need to use the command:
# - pip freeze > requirements.txt

# To install the packages from the requirements.txt file, we need to use the command:
# - pip install -r requirements.txt
# We can distribute the requirements.txt file to other developers.
# They can recreate the same environment on their own.

# ==============================================================================================

# Lambda Function:
# Lambda function is a function that is executed when a specific event occurs.
# Function created using an expression using 'lambda' keyword.

# Syntax:
#       lambda arguments: expression
#       lambda argument1,argument2: expression
# can be used as a normal function.

# Example 1:
square = lambda x: x * x
print(square(3))
print(square(4))

# Example 2:
sum = lambda a,b,c: a+b+c
print(sum(1,2,3))

# Example 3:
cube = lambda x: x**3
print(cube(4))

# ===============================================================================================

# Join Method (Strings):
# The join() method returns a string in which the string elements of sequence have been joined by str separator.
# Syntax:
#       string.join(sequence)
# Example:
l = ['a', 'b', 'c', 'd', 'e']
result = "-".join(l)
print(result)
# Output: a-b-c-d-e

# ===============================================================================================

# Format Method (Strings):
# The format() method formats the specified value and insert it in the string's placeholder.
# Syntax:
#       string.format(value1, value2, etc)
# Example 1:
name = "Pratik"
age = 18
print("My name is {} and I am {} years old.".format(name, age))

# Example 2:
a= "{1} is practicing {0}".format("Python","Pratik")
print(a)