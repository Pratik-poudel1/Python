# Global Keyword
# The global keyword is used to create a global variable in a function.
a=100

def func():
    global a
    a=3
    print(a)

func()
print(a)
# output:
# 3
# 3
