# Example of different us
a = 5           # int
b = 2.5         # float
name = "Bob"    # str
is_valid = True  # bool
c = None          # NoneType

# You can use the type() function to check the type of a variable.
print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(name))  # Output: <class 'str'>
print(type(is_valid))  # Output: <class 'bool'>
print(type(c))  # Output: <class 'NoneType'>


# Type Casting
# Type casting is the process of converting a variable from one type to another.
# You can use the following functions for type casting:
# int() - converts a value to an integer
# float() - converts a value to a float
# str() - converts a value to a string

# Example of type casting
num_str = "123"
num_int = int(num_str)  # Convert string to integer
num2 = 2
print(num_int+num2)  # Output: 125

float_num = float(num_str)  # Convert string to float
print(float_num)  # Output: 123.0