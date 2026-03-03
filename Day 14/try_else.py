# Try with else clause:
# The else block is executed when there is no exception raised in the try block.

try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print("Error:",e)
else:
    print("No exception")