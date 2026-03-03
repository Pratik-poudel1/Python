# Walrus Operator :
# The Walrus operator := is a new assignment operator introduced in Python 3.8.
# It allows you to assign a value to a variable in a single line of code,
# without the need for a separate declaration statement.
# The syntax is: variable := expression

# Example 1:
# Using Walrus Operator:
if (n := int(input("Enter a number: ")) % 2) == 0:
    print(f"{n} is even.")
else:
    print(f"{n} is odd.")

# Example 2:
# Using Walrus Operator:
if (n := len([1,2,3,4,5])) > 3:
    print(f"List is too long ({n} elements ,expected <= 3).")
# In this program,n is assigned the value of len([1,2,3,4,5]) and then used in the 
# comparison within the if statement.
