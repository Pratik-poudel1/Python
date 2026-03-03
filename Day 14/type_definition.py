# Types Definitions in Python :
# Types hints are added using the colon(:) syntax for the variables and the -> syntax for the functions.

# Variable type hint:
n : int =5
name : str = "Pratik"

# Function type hint:
def sum(a:int,b:int) -> int:
    return a+b

# Usage:
print(sum(2,3))

# Advanced Type Hints :
# Python's typing module provides more advanced type hints, such as Union, List, Dict, and Tuple.

from typing import Union, List, Dict, Tuple
# The syntax of types looks something like this:

# List of Integers
numbers: List[int] = [1, 2, 3]

# Tuple of a string and a integer
person: Tuple[str, int] = ("Pratik", 18)

# Dictionary with string keys and a List of Integers as values
marks: Dict[str, int] = {
    "Pratik" : 90,
    "Nishant" : 80
}

# Union type for variables that can hold multiple types
identifier: Union[ int,str] = "ID123"
identifier = 12345 # Also valid