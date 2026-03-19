# Raising Exceptions:
# Exceptions can be raised using the raise keyword.
# The raise keyword is used to raise an exception in Python.
# Example:
a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
if b==0:
    raise ZeroDivisionError("b cannot be zero")
else:
    print(a/b)