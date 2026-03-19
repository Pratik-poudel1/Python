#===================== Question 1 =====================#
# WAP to store seven fruits in a list entered by the user.
fruits = []
fruits.append(input("Enter the name of fruit 1: "))
fruits.append(input("Enter the name of fruit 2: "))
fruits.append(input("Enter the name of fruit 3: "))
fruits.append(input("Enter the name of fruit 4: "))
fruits.append(input("Enter the name of fruit 5: "))
fruits.append(input("Enter the name of fruit 6: "))
fruits.append(input("Enter the name of fruit 7: "))
print("The list of fruits you entered is: ", fruits)

#===================== Question 2 =====================#
# WAP to accept marks of 6 subjects from the user and display them in sorted manner.
marks = []
marks.append(float(input("Enter the marks of subject 1: ")))
marks.append(float(input("Enter the marks of subject 2: ")))
marks.append(float(input("Enter the marks of subject 3: ")))
marks.append(float(input("Enter the marks of subject 4: ")))
marks.append(float(input("Enter the marks of subject 5: ")))
marks.append(float(input("Enter the marks of subject 6: ")))
marks.sort()
print("The marks of the 6 subjects in sorted order are: ", marks)

#===================== Question 3 =====================#
# Check that a tuple type cannot be chananged in Python.
tuple1=(1,2,3,4,5)
print("The tuple is: ", tuple1)
# tuple1[0] = 10  # This will raise an error because tuples are immutable

#===================== Question 4 =====================#
# WAP to sum a list with 4 numbers.
num=[22,33,44,55]
print("The sum of the numbers is: ", sum(num)) # Output: 154,
# Sum() is a built-in function in Python that takes an iterable (like a list) and returns the sum of its elements.

#===================== Question 5 =====================#
# WAP to count the nomber of zeros in the following tuple : a= (7, 0, 8, 0, 0, 9)
tuple=(7, 0, 8, 0, 0, 9)
print(tuple.count(0))  # This will return the number of occurrences of 0 in the tuple