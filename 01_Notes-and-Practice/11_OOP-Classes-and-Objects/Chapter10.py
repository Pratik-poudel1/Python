# Object Oriented Programming :
# Solvine a problem by creating object is one of the most popular approaches in
# Programming. This is called object-oriented programming.

# Class :
# A Class is a blueprint for creating object.

# Syntax:
#           class Employee: #class name is written in pascal case
#               # Methods and variables

# Object :
# An object is an instantiation of a class. When a class is defined,
# a template(info) is defined. Memory is allocated only after object instantiation.

# Objects of a given class can invoke the methods available to it without revealing the 
# implementation detailed to the user. --Abstractions and Encapsulation

# Modelling a Problem in OOPs :
# We identify the following in our problem.
# 1. Noun -> Class -> Employee
# 2. Adjective -> Attributes -> name, age, salary
# 3. Verbs -> Methods -> getSalary(), increment()

# Class Attributes :
# An Attributes that belongs to the class rather than a particular object.

# Example :
class Employee:
    company="Google" # specific to Each class
sam = Employee() # Object Instatiation
sam.company
Employee.company="Youtube" # Changing class Attribute

# Instance Attributes:
# An attribute that belongs to the instace(object). Assuming the class from the previous example:
sam.name="Sam"
sam.salary= "30K" # Adding instance attribute

# Note: Instance attributes, take preference over class attributes during assignment and retrieval.
# When looking up for sam.attribute it checks for the following :
# 1) Is attributes present in object ?
# 2) Is attributes present in class ?

# Self Parameter :
# Self refers to the nstance of the class. It is automatically passed with a function call from an object.

pratik.getSalary() # here self is pratik
# equivalent to Employee.getSalary(pratik)

# The function getSalary() is defined as :
class Employee:
    company="Google"
    def getSalary(self):
        print("Salary is not there")

# Static Method:
# Sometimes we need a function that does not use the self-parameter. We can define a
# static method like this:
@staticmethod # decorator to mark greet as a static method
def greet():
    print("Hello User")

#__INIT__() Constructor:
# __init__() is a special method which is first run as soon as the object is created.
# __init__() method is also known as constructor.
# It takes self-argument and can also take further arguments.

# For Example:
class Employee:
    def __init__(self,name):
        self.name=name
    def getSalary(self):
        ...

harry = Employee("Harry")