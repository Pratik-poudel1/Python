#========================= Question 1 ======================
# Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class TwoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")

class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a= TwoDvector(1,2)
a.show()
b= ThreeDvector(1,2,3)
b.show()

#========================= Question 2 ======================
# Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets".
# Add a method 'bark' to class 'Dog".
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Woof Woof !")

d=Dog()
d.bark()

#========================= Question 3 ======================
# Create a class 'Employee' and add salary and increment properties to it.
# Write a method 'salaryAfterIncrement' method with a @property decorator with a setter
# which changes the value of increment based on the salary.
class Employee:
    salary=234
    increament = 20
    @property
    def salaryAfterIncreament(self):
        return self.salary + self.salary * (self.increament/100)

    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self,salary):
        self.increament = ((salary/self.salary)-1)*100

e = Employee()
# print(e.salaryAfterIncreament)
e.salaryAfterIncreament = 280.8
print(e.increament)

#========================= Question 4 ======================
# Write a class 'Complex' to represent complex numbers, along with overloaded
# operators'+' and '*' which adds and multiplies them.
class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
        
    def __add__(self,c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self,c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part,imag_part)

    
    def __str__(self):
        return f"{self.r} + {self.i}i "

c1=Complex(1,2)
c2=Complex(3,4)
print(c1+c2)
print(c1*c2)

#========================= Question 5 ======================
# Write a class vector representing a vector of n dimensions. Overload the + and * operator
# which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, components):
        self.components = components
        self.n = len(components)

    def __add__(self, other):
        if self.n != other.n:
            raise ValueError("Vectors must have same dimensions for addition")
        
        result = [self.components[i] + other.components[i] for i in range(self.n)]
        return Vector(result)

    def __mul__(self, other):
        if self.n != other.n:
            raise ValueError("Vectors must have same dimensions for dot product")
        
        dot_product = sum(self.components[i] * other.components[i] for i in range(self.n))
        return dot_product

    def __str__(self):
        return f"Vector({self.components})"
# Example Usage
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Vector 1:", v1)
print("Vector 2:", v2)

print("Sum:", v1 + v2)      # Vector addition
print("Dot Product:", v1 * v2)  # Dot product

#========================= Question 6 ======================
# Write str() method to print the vector as follows:
#           71 81 +10k
# Assume vector of dimension 3 for this problem.
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

v = Vector(7, 8, 10)
print(v)

#========================= Question 7 ======================
# Override the_len_() method on vector of problem 5 to display the dimension of the vector.
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    # Vector Addition
    def __add__(self, other):
        return Vector(self.i + other.i,self.j + other.j,self.k + other.k)

    # Dot Product
    def __mul__(self, other):
        return (self.i * other.i +self.j * other.j +self.k * other.k)

    # String Method
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    # Override len()
    def __len__(self):
        return 3

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("v1 =", v1)
print("v2 =", v2)

print("Sum =", v1 + v2)
print("Dot Product =", v1 * v2)

print("Dimension of v1 =", len(v1))
