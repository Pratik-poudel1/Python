# Operators
# Operators are used to perform operations on variables and values.

# Python has several types of operators, including:
# 1. Arithmetic Operators: +, -, *, /, %, **, //
# 2. Assignment Operators: =, +=, -=, *=, /=, %=,
# 3. Comparison Operators: ==, !=, >, <, >=, <=
# 4. Logical Operators: and, or, not
# 5. Bitwise Operators: &, |, ^, ~, <<, >>
# 6. Identity Operators: is, is not
# 7. Membership Operators: in, not in

# Example of Arithmetic Operators
a = 10
b = 3
print(a+b) 
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

# Example of Assignment Operators
x=5
x += 3  # Increament of value of x by 3
x -= 2  # Decreament of value of x by 2
x *= 4  # x=x*4
x /= 6  # x=x/6
x %= 3  # x=x%3
x **= 2  # x=x**2 (X to the power of 2)
x //= 1  # x=x//1

# Example of Comparison Operators
p=10
q=20
print(p==q)  # False
print(p!=q)  # True
print(p>q)   # False
print(p<q)   # True
print(p>=q)  # False
print(p<=q)  # True


# Example of Logical Operators
aa = int(input("Enter a number:"))
print(aa > 0 and aa < 100)  # True if aa is between 0 and 100
print(aa < 0 or aa > 100)   # True if aa is less than 0 or greater than 100
print(not(aa > 0 and aa < 100))  # True if aa is not between 0 and 100

# Example of Bitwise Operators
x = 5  # In binary: 0101
y = 3  # In binary: 0011
print(x & y)  # Bitwise AND: 0001 (1 in decimal)
print(x | y)  # Bitwise OR: 0111 (7 in decimal)
print(x ^ y)  # Bitwise XOR: 0110 (6 in decimal)
print(~x)     # Bitwise NOT: 1010 (-6 in decimal)
print(x << 1)  # Left shift: 1010 (10 in decimal)
print(x >> 1)  # Right shift: 0010 (2 in decimal)

