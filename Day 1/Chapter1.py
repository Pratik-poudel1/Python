# Modules,Comments and PIP
# A module is a file containing Python definitions and statements.
# The file name is the module name with the suffix .py added.
# You can import a module to use its functions and variables in your code.
# To import a module, you can use the import statement.

# To Install a module, you can use the Syntax: pip install module_name
# To check if a module is installed, you can use the Syntax: pip show module_name
# To uninstall a module, you can use the Syntax: pip uninstall module_name

# Example to install a module: pip install pyjokes
# Example to import a module: import pyjokes

import pyjokes
joke= pyjokes.get_joke()
print(joke)
# More info about pyjokes: https://pyjok.es/

# Module is Of two types:
# 1. Built-in Modules: These are modules that come with Python and are available for use without needing to install 
#    them. Examples include math, random, datetime, etc.
# 2. External Modules: These are modules that are not included with Python and need to be installed separately 
#    using pip. Examples include requests, numpy, pandas, etc.

# Comments are used to explain the code and make it more readable.
# They are ignored by the Python interpreter and do not affect the execution of the program. 
# In Python, comments can be created using the # symbol for single-line comments or 
# triple quotes (''' or """) for multi-line comments.
