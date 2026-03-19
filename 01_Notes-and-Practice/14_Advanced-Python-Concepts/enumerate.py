# Enumerate Function in Python :
# enumerate is a built-in function in Python that returns an iterator that 
# generates a sequence of tuples containing the index and the value of each element in a sequence.

# Example 2:
# l = [3,53,513,535]
# index =0
# for item in l:
#     print(f"The item number {index} is {item}")
#     index +=1

#  This can be simplified using enumerate function:
l = [3,53,513,535]
for index, item in enumerate(l):
    print(f"The item number {index} is {item}")