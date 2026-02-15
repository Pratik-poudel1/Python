# String Functions :
# Python provides a variety of built-in string functions that allow you to manipulate 
# and work with strings in different ways. Here are some commonly used string functions:

# 1. len() : Returns the length of a string.
string = "Hello World!"
length = len(string)
print(length)  # Output: 12

# 2. upper() : Converts all characters in a string to uppercase.
a = "Python programming "
cap_string = a.upper()
print(cap_string)  # Output: "PYTHON PROGRAMMING "

# 3. lower() : Converts all characters in a string to lowercase.
a = "PYTHON PROGRAMMING "
small_string = a.lower()
print(small_string)  # Output: "python programming "

# 4. endswith() : Checks if a string ends with a specified suffix.
a = "Hello World!"
print(a.endswith("!"))  # Output: True
print(a.endswith("d"))  # Output: False

# 5. startswith() : Checks if a string starts with a specified prefix.
a = "Hello World!"
print(a.startswith("H"))  # Output: True
print(a.startswith("h"))  # Output: False

# 6. capitalize() : Capitalizes the first character of a string and converts the rest to lowercase.
a = "hello world!"
cap_string = a.capitalize()
print(capitalized_string)  # Output: "Hello world!"

# 7. title() : Capitalizes the first character of each word in a string.
a = "hello world!"
title_string = a.title()
print(title_string)  # Output: "Hello World!"

# 8. strip() : Removes leading and trailing whitespace from a string.
a = "   Hello             World                        !   "
stripped_string = a.strip()
print(stripped_string)  # Output: "Hello World!" 

# 9. count() : Returns the number of occurrences of a substring in a string.
a = "Hello World! Hello everyone."
count = a.count("Hello")
print(count)  # Output: 2

# 10. find() : Returns the index of the first occurrence of a substring in a string.
a = "Hello World!"
index = a.find("World")
print(index)  # Output: 6

# 11. replace() : Replaces occurrences of a substring with another substring.
a = "Hello World! and Hello everyone."
new_string = a.replace("Hello", "HI")
print(new_string)  # Output: "HI World! and HI everyone."

# 12. split() : Splits a string into a list of substrings based on a specified delimiter.
a = "Hello World! and Hello everyone."
split_string = a.split(" ")  # Split the string by spaces
print(split_string)  # Output: ['Hello', 'World!', 'and', 'Hello', 'everyone.']


# The String are immutable, which means that once a string is created, it cannot be changed.
# Even though you can perform operations on a string, the original string remains unchanged.

