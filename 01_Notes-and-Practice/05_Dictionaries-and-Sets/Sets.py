# Sets :

# A set is a collection which is unordered, unchangeable*, and unindexed.
# In Python sets are written with curly brackets, and they have no duplicate items.

# Create and print a set:
my_set={"apple","banana","cherry"}
print(my_set,type(my_set))

# To Create Empty Set:
empty_set=set()
print(empty_set,type(empty_set))

# Properties of a set:
# 1. Unordered: The items in a set are unordered, meaning that they do not have a defined order.
# 2. Unchangeable*: Once a set is created, you cannot change its items, but you can add new items to it.
# 3. Unindexed: Sets do not have indexes, so you cannot access items in a set by referring to an index.
# 4. No Duplicate Items: Sets do not allow duplicate items. If you try to add a duplicate item, it will be ignored.

len(my_set) # To get the number of items in a set.
print(len(my_set))

# Set Methods:
# 1. add(): Adds an element to the set.
my_set.add("orange")
print(my_set)

# 2. remove(): Removes the specified element from the set. If the element is not found, it raises a KeyError.
my_set.remove("banana")
print(my_set)

# 3. discard(): Removes the specified element from the set. If the element is not found, it does nothing.
my_set.discard("banana") # This will not raise an error even though "banana" is not in the set.
print(my_set)

# 4. pop(): Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
popped_item=my_set.pop()
print(popped_item)
print(my_set)

# 5. copy(): Returns a shallow copy of the set.
my_set_copy=my_set.copy()
print(my_set_copy)

# 6. clear(): Removes all the elements from the set.
my_set.clear()
print(my_set)

# 7. union(): Returns a new set that contains all the items from both sets.
set1={"apple","banana","cherry"}
set2={"orange","grape","melon"}
set3=set1.union(set2)
print(set3)

# 8. intersection(): Returns a new set that contains only the items that are present in both sets.
set4={2,4,6,8,10}
set5={1,2,3,4,5,6}
set6=set4.intersection(set5)
print(set6)

# 9. difference(): Returns a new set that contains the items that are present in the first set but not in the second set.
set7=set4.difference(set5)
print(set7)

# 10. symmetric_difference(): Returns a new set that contains the items that are present in either set, but not in both sets.
set8=set4.symmetric_difference(set5)
print(set8)

# 11. issubset(): Returns True if all items in the set are present in another set, otherwise returns False.
set9={1,2,3}
set10={1,2,3,4,5}
print(set9.issubset(set10)) # True
print(set10.issubset(set9)) # False

# 12. issuperset(): Returns True if all items in another set are present in the set, otherwise returns False.
print(set10.issuperset(set9)) # True
print(set9.issuperset(set10)) # False


