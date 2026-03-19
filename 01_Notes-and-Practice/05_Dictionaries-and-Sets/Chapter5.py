# Dictionary :

# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

# Create and print a dictionary:
marks={
    "Maths": 90,
    "Science": 85,
    "English": 88
}
print(marks,type(marks))
print(marks["Maths"])

# Change values in a dictionary:
marks["Maths"]=95
print(marks)

# Loop through a dictionary:
for subject in marks:
    print(subject,marks[subject])

# Properties of a dictionary:
# 1. Unordered: The items in a dictionary are unordered, meaning that they do not have a defined order.
#    When you print a dictionary, the items may appear in a different order than they were added.
# 2. Changeable: You can change the values of a dictionary after it has been created. 
#    You can add new key-value pairs, modify existing ones, or remove them.
# 3. Indexed: Each item in a dictionary has a key, which is used to access the corresponding value.
#    You can use the key to retrieve the value associated with it.

# Dictionary Methods:
# 1. keys(): Returns a view object that displays a list of all the keys in the dictionary.
print(marks.keys())

# 2. values(): Returns a view object that displays a list of all the values in the dictionary.
print(marks.values())

# 3. items(): Returns a view object that displays a list of dictionary's key-value tuple pairs.
print(marks.items())

# 4. get(): Returns the value of the specified key. If the key does not exist, it returns None.
print(marks.get("Maths")) # print(marks["History"]) # This will raise a KeyError because "History" is not a key in the dictionary.

# 5. pop(): Removes the item with the specified key and returns its value. 
#           If the key does not exist, it raises a KeyError.
print(marks.pop("Science"))
print(marks)

# 6. update(): Updates the dictionary with the elements from another dictionary object 
#              or from an iterable of key-value pairs.
new_marks={
    "History": 80,
    "Geography": 82
}
marks.update(new_marks)
marks.update({"Maths": 98})
print(marks)

# 7. copy(): Returns a shallow copy of the dictionary.
marks_copy=marks.copy()
print(marks_copy)

# 8. clear(): Removes all the items from the dictionary.
marks.clear()
print(marks)

# 9. popitem(): Removes the last inserted key-value pair from the dictionary and returns it as a tuple.
marks_copy.popitem()
print(marks_copy)

# 10. fromkeys(): Creates a new dictionary with keys from an iterable and values set to a specified value.
subjects=["Maths","Science","English"]
default_marks=0
new_marks_dict=dict.fromkeys(subjects,default_marks)
print(new_marks_dict)

# To create a empty dictionary, you can use either of the following methods:
empty_dict1={}
empty_dict2=dict()
print(empty_dict1,empty_dict2)