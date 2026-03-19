#=========================== Question 1 =========================
# Create a Class "Programmer" for storing information of few programmers working at Microsoft.
class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("Pratik",120000,245001)
print(p.name,p.salary,p.pin,p.company)
s=Programmer("Sam",100000,245002)
print(s.name,s.salary,s.pin,s.company)

#=========================== Question 2 =========================
# Write a class "calculator" capable of finding square, cube and square root of a number.
class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The Square is {self.n*self.n}")
    def cube(self):
        print(f"The Cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The Square Root is {self.n**1/2}")

a=Calculator(4)
a.square()
a.cube()
a.squareroot()

#=========================== Question 3 =========================
# Create a class with a class attribute a; create an object from it and set 'a' directly
# using object.no. Does this change the class attribute?
class Demo:
    a=4

o=Demo()
print(o.a) # Prints class attribute, because instance attribute is not present
o.a=0 # Instance attribute is set now,
print(o.a)  # Prints the instancce attribute because it is present now
# No,The class attribute has not change.because if i use print(Demo.a),it gives 4

#=========================== Question 4 =========================
# Add a static method in problem 2, to greet the user with hello..
class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The Square is {self.n*self.n}")
    def cube(self):
        print(f"The Cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The Square Root is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello User!")

a=Calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()

#=========================== Question 5 =========================
# Write a class Train which has methods to book a ticket, get status (no of seats) and
# get fare information of train running under Indian Railways.
import random # from ramdom import randit
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no:{self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
        

    def getFare(self,fro,to):
        print(f"Ticket is booked in train no:{self.trainNo} from {fro} to {to} is {random.randint(222,5555)}")

t=Train(12399)
t.book("Kathmandu","Jhapa")
t.getStatus()
t.getFare("Kathmandu","Jhapa")
        

#=========================== Question 6 =========================
# Can you change the self-parameter inside a class to something else (say "harry").
# Try changing self to "slf" or "harry" and see the effects.

class Programmer:
    company="Microsoft"
    def __init__(slf,name,salary,pin):
        slf.name=name
        slf.salary=salary
        slf.pin=pin

p=Programmer("Pratik",120000,245001)
print(p.name,p.salary,p.pin,p.company)
s=Programmer("Sam",100000,245002)
print(s.name,s.salary,s.pin,s.company)
# With the use of slf instead of self nothing happens,program runs smoothly