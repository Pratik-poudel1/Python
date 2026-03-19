# Lists:

# Lists are mutable, meaning you can change their contents after they have been created.
# They are defined using square brackets [].
list1 = [1, 2, 3, 4, 5]
friends = ["Apple","Orange",5,False,"Akash","Rohit"]
print(list1)
print(friends)

# You can access elements of a list using their index, which starts at 0.
print(list1[0])  # Output: 1
print(friends[3])  # Output: "False"

# You can also use negative indexing to access elements from the end of the list.
print(list1[-1])  # Output: 5
print(friends[-2])  # Output: "Akash"

# Lists can contain elements of different data types, including other lists.
mixed_list = [1, "Hello", 3.14, [1, 2, 3]]
print(mixed_list)

# You can modify the contents of a list by assigning new values to specific indices.
list1[0] = 10 # List are Mutable unlike Strings and Tuples
print(list1)  # Output: [10, 2, 3, 4, 5]

# List Slicing allows you to access a portion of the list by specifying a range of indices.
list = list1[1:4]  # This will give you a new list containing elements from index 1 to 3 (4 is exclusive)
print(list)  # Output: [2, 3, 4]


# List Methods:
# Lists have various built-in methods that allow you to perform operations on them.
# Here the List itself changes when we use these methods, unlike Strings. 
# Some common list methods include:
# append(): Adds an element to the end of the list.
    list1.append(6)
    print(list1)  # Output: [10, 2, 3, 4, 5, 6]
# insert(): Inserts an element at a specific index.
    list1.insert(1, 15)  # This will insert 15 at index 1
    print(list1)  # Output: [10, 15, 2, 3, 4, 5, 6]
# remove(): Removes the first occurrence of a specified value.
    list1.remove(3)  # This will remove the first occurrence of 3
    print(list1)  # Output: [10, 15, 2, 4, 5, 6]
# pop(): Removes and returns the element at a specified index (or the last element if no index is provided).
    print(list1.pop(2)) # This will remove and return the element at index 2, Output: 2
    print(list1)  # Output: [10, 15, 4, 5, 6]
# sort(): Sorts the elements of the list in ascending order.
    list1.sort()  # This will sort the list in ascending order
    print(list1)  # Output: [4, 5, 6, 10, 15]
# reverse(): Reverses the order of the elements in the list.
    list1.reverse()  # This will reverse the order of the list
    print(list1)  # Output: [15, 10, 6, 5, 4]
# clear(): Removes all elements from the list.
    list1.clear()  # This will remove all elements from the list
    print(list1)  # Output: []
# index(): Returns the index of the first occurrence of a specified value.
    friends_index = friends.index("Akash")  # This will return the index of the first occurrence of "Akash"
    print(friends_index)  # Output: 4
# count(): Returns the number of occurrences of a specified value in the list.
    count_5 = friends.count(5)  # This will return the number of occurrences of 5 in the friends list
    print(count_5)  # Output: 1

