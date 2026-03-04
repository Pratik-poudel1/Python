# ======================== Question 1 ============================
# Create two virtual environments, install few packages in the first one. 
# How do you create a similar environment in the second one?


# ======================== Question 2 ============================
# Write a program to input name, marks and phone number of a student and format it 
# using the format function like below:
# "The name of the student is Pratik, his marks are 72 and phone number is 99999888"
name=input("Enter name: ")
marks=input("Enter marks: ")
phone=input("Enter phone number: ")
print("The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phone))

# ======================== Question 3 ============================
# A list contains the multiplication table of 7.
# write a program to convert it to vertical string of same numbers.
table=[7*i for i in range(1,11)]
s="\n".join(str(i) for i in table)
print(s)

#========================= Question 4 ============================
# Write a program to filter a list of numbers which are divisible by 5
l = [1,2,3,4,5,6,7,8,9,10]
def five(n):
    if n%5==0:
        return True
    return False
s=list(filter(five,l))
print(s)

#========================= Question 5 ============================
# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

num =[110,20,330,40,510,10]
def max(a,b):
    if a>b:
        return a
    return b
print(reduce(max,num))

#========================= Question 6 ============================
# Rum pip freeze for the system interpreter.Take the contents and create a similar virtualenv.

#========================= Question 7 ============================
# Explore the 'Flask' module and create a web server using Flask and Python.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()