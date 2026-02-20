# Recursions:
# Recursion is a process where a function calls itself to solve a smaller part of a problem.

# A recursive function must have:
# 1. Base Case (stopping condition)
# 2. Recursive Case (function calling itself)

# Example 1: Factorial using Recursion
# Factorial formula:
# n!=n×(n−1)!
def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n-1)   # Recursive case

print(factorial(5))

# Output:
# 120

# Example 2: Sum of Natural Numbers
def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n-1)

print(sum_n(5))


# Example 3: Fibonacci Series
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
