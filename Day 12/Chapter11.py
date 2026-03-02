# Inheritance :
# It is a way of creating a new class from an existing class.

# Syntax:
        # class Employee:  Base Class
        #      Code 
        
        # class Programmer(Employee): Derived or Child Class
        #      Code

# We can use the method and attributes of "Employee" in "Programmer" object.
# Also,we can overwrite or add new attributes and methods in "Programmer" class.

# Types of Inheritance :
# 1) Single Inheritance
# 2) Multiple Inheritance
# 3) Multilevel Inheritance

# Single Inheritance:
#   It occurs when child class inherits only a single parent class.

# Multiple Inheritance:
#   It occurs when the child class inherits from more than one parent classes.

# Multilevel Inheritance: 
#   When a child class becomes a parent class for another child class.

# Super() Method: 
#   It is used to access the methods of a super class in the derived class.

# Syntax:
#           super().__init__()
#           __init__() calls constructor of the base class

# Class Method:
#   It is a method which is bound to the class and not the object of the class.

# @classmethod decorator is used to create a class method.

# Syntax:
#           @classmethod
#               def(cls,p1,p2)

# @Property Decorators:
# Consider following Class:
Class Employee:
    @property
    def name(self):
        return self.name
# If e=Employee() is an object of class employee, we can print(e.name) to print 
# the ename by internally calling name() function.

# @.GETTERS AND @.SETTERS :
# The method name with "@property" decorator is called getter method.

# We can define a function + @ name.setter decorator like below:
@name.setter
def name(self,value):
    self.ename = value

# Operator Overloading in Python:
# Operators in python can be overloaded using dunder methods.
# These methods are called when a given operator is used on the objects.
# Operators in python can be overloaded using the following methods:
# p1+p2 (p1.__add__(p2))
# p1-p2 (p1.__sub__(p2))
# p1*p2 (p1.__mul__(p2))
# p1/p2 (p1.__truediv__(p2))
# p1//p2 (p1.__floordiv__(p2))

# Other dunder/magic methods in Python:
__str__() # Used to set what gets desplayed upon calling str(obj)
__len__() # Used to set what gets displayed upon calling.__len__() or len(obj)
