# Map :
# Map applies a function to all the items in an input_list.

# Syntax:
#       map(function,input_list)
# the function can be lambda function

# Example:
l=[1,2,3,4,5]
sqlist = lambda x:x*x
sqlist = map(square,l)
print(list(sqlist))

#================================================================================

# Filter:
# Filter creates a list of items for which the function returns true.

# Syntax:
#       list(filter(function,input_list))
# the function can be lambda function

# Example:
def even(n):
    if n%2==0:
        return True
    return False
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list(filter(even,num)))

#================================================================================

# Reduce:
# Reduce applies a rolling computation to sequential pair of elements in a list.

# Syntax:
#       from functools import reduce
#       val=reduce(function,list1)
# the function can be lambda function

# Example:
from functools import reduce

def sum(a,b):
    return a+b
n=[1,2,3,4,5]
print(reduce(sum,n))
# Output:15
# Process of calculation:
# 1+2=3
# 3+3=6
# 6+4=10
# 10+5=15

#================================================================================