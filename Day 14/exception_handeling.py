# Exception Handling in Python:
# There are many built-in exceptions which are raised in python when 
# something goes wrong.

# Exception in python can be handeled using a try statement. The code that handels the 
# exception is written in the except block.
try:
    a = 10/0
    print(a)
except Exception as e:
    print("Error:",e)

# When the exception is handeled, the code flow continues without programming interruption.

# We can also specify the exception to ctch like below:
try:
    code
except ZeroDivisionError:
    # code
except NameError:
    # code
except:
    # code                    
    # All other exceptions

# We can also use else block to execute the code when there is no exception.
try:
    code
except:
    # code
else:
    # code

# We can also use finally block to execute the code whether there is an exception or not.
try:
    code
except:
    # code
finally:
    # code