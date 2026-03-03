# Dictionary Merge and Update Operators:
# New Operators | and |= allow for merging and updating dictionaries.

dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
merged = dict1 | dict2
print(merged)    # Output: {'a': 1, 'b': 3, 'c': 4}

# You can now use multiple context managers in a single with statement, 
# and the order of evaluation is determined by the order of the context managers
with (
    open("file1.txt", "r") as f1,
    open("file2.txt", "w") as f2
):   # Process files
    pass