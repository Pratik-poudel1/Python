# Tuples :
# A tuple is an ordered collection of elements, similar to a list, 
# but it is immutable, meaning that once a tuple is created, its contents cannot be changed.
# Tuples are defined using parentheses ().

# Creating a tuple
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("Apple","Orange",5,False,"Akash","Rohit")
print(tuple1)
print(tuple2)

# You can access elements of a tuple using their index, which starts at 0.
print(tuple1[0])  # Output: 1
print(tuple2[3])  # Output: "False"
# You can also use negative indexing to access elements from the end of the tuple.
print(tuple1[-1])  # Output: 5
print(tuple2[-2])  # Output: "Akash"

# Tuples can contain elements of different data types, including other tuples.
mixed_tuple = (1, "Hello", 3.14, (1, 2, 3))
print(mixed_tuple)

# Since tuples are immutable, you cannot modify their contents after they have been created.
# However, you can perform operations that create new tuples based on existing ones.

# Concatenation: You can concatenate two tuples using the + operator.
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (1, 2, 3, 4, 5, "Apple", "Orange", 5, False, "Akash", "Rohit")

# Repetition: You can repeat a tuple a specified number of times using the * operator.
tuple4 = tuple1 * 2
print(tuple4)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Tuple Slicing allows you to access a portion of the tuple by specifying a range of indices.
slice = tuple1[1:4]  # This will give you a new tuple
print(slice)  # Output: (2, 3, 4)

# To make a Empty Tuple, you can use empty parentheses.
empty_tuple = ()
print(empty_tuple)  # Output: ()
# To make tuple with a single element, you need to include a comma after the element.
single_tuple = (42,)
print(single_tuple)  # Output: (42,)


# Tuple Methods:
# Tuples have a few built-in methods that allow you to perform operations on them.
# count(): Returns the number of occurrences of a specified value in the tuple.
    print(tuple2.count(5))  # This will return the number of occurrences of 5 in the tuple2
    # Output: 1
# index(): Returns the index of the first occurrence of a specified value.
    print(tuple2.index("Akash"))  # This will return the index of the first occurrence of "Akash" in the tuple2
    # Output: 4
# Since tuples are immutable, they do not have methods that modify their contents,
    # such as append() or remove(), which are available for lists.

# Membership Testing: You can use the in keyword to check if a value exists in a tuple.
print(3 in tuple1)  # Output: True
print("Banana" in tuple2)  # Output: False

# Length of a Tuple: You can use the len() function to get the number of elements in a tuple.
print(len(tuple1))  # Output: 5

# Max and Min: You can use the max() and min() functions to find the maximum and minimum values in a tuple of numbers.
print(max(tuple1))  # Output: 5
print(min(tuple1))  # Output: 1

# Unpacking: You can unpack the elements of a tuple into separate variables.
a, b, c, d, e = tuple1
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: 4
print(e)  # Output: 5
