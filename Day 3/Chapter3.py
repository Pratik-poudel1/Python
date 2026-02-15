# Strings
# A string is a sequence of characters. 
# In Python, strings are enclosed in either:
# single quotes (' '),double quotes (" ") or triple quotes (''' ''' or """ """)
# triple quotes are used for multi-line strings.
# String is immutable, which means that once a string is created, it cannot be changed.

# Example of a string
string = "Hello World!"

# String Slicing :
# String slicing is a way to extract a portion of a string.
# The syntax for string slicing is: string[start:stop:step]

# Example of string slicing:
slice = string[0:5]  # Extracts "Hello" (from index 0 to 5, But not including index 5)
print(slice)
# Also use -1 to slice from the end of the string
slice = string[-6:]  # Extracts "World!" (from index -6 to the end of the string)
print(slice)


# Slicing with step:
# The step parameter in string slicing allows you to specify the interval between characters to be extracted.

# Example of slicing with step:
slice = string[0:11:2]  # Extracts "HloWrd" (from index 0 to 11, with a step of 2)
print(slice)

# String Concatenation:
# String concatenation is the process of combining two or more strings into one string.
# In Python, you can concatenate strings using the + operator.