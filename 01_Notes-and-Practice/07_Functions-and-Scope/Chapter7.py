# Loops in Python :
# Loops in Python are used to execute a block of code repeatedly.

# There are mainly two types of loops in Python:

# 1.for loop
# 2.while loop

# 1. for Loop :
# The for loop is used to iterate over a sequence (like list, tuple, string, or range).

# Syntax:
        for variable in sequence:
            
# Example 1: Printing numbers 1 to 5
for i in range(1, 6):
    print(i)

# Output:

# 1
# 2
# 3
# 4
# 5

# Example 2: Loop through a list
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# 2. while Loop :
# The while loop runs as long as the condition is True.

# Syntax:
        while condition:

# Example:
i = 1
while i <= 5:
    print(i)
    i += 1


# Loop Control Statements
# These are used to control loop behavior:

# 1. break:
# Stops the loop completely.

for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Output:
# 1
# 2

# 2. continue:
# Skips the current iteration.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output:

# 1
# 2
# 4
# 5

# 3. pass:
# Does nothing (used as placeholder).
# It is a Null Statements.

for i in range(5):
    pass


# 4. Nested Loops:
# A loop inside another loop.

for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)

# For Loop with Else:
# An Optional else can be used with a for Loop if the code is to be executed when the loops exhausts.

# Example :
l=[1,7,8]
for items in l:
    print(item)
else:
    print("Done") # This is printed when the loop exhausts

# Output :
# 1
# 7
# 8
# Done

# Iteration means i=0,i=1,.........etc

