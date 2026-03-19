# List Comprehension:
# List comprehension is a way to create a new list by applying a function to each element of an existing list.

# Example:

mylist=[1,2,9,3,4,5]
sqlist=[]
for item in my list:
    sqlist.append(item*item)
print(sqlist)

# This can be simplified using list comprehension:
mylist=[1,2,9,3,4,5]
sqlist=[item*item for item in mylist]
print(sqlist)