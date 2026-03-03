#============================= Question 1 ==============================
# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present,
# a message without exiting the program must be printed prompting the same.
try:
    with open("1.txt", "r") as f1:
        print(f1.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f2:
        print(f2.read())
    print("File " + "2.txt" + " found")
except FileNotFoundError:
    print("File not found")
    
try:
    with open("3.txt", "r") as f3:
        print(f3.read())
except FileNotFoundError:
    print("File not found")

print("Thank you for using our service")

#============================= Question 2 ==============================
# Write a program to print third, fifth and seventh element from a list using enumerate function.
l=[1,2,3,4,5,6,7,8,9,10]
for index, item in enumerate(l):
    if index in [2,4,6]:  # if i==2 or i==4 or i==6
        print(item)

#============================= Question 3 ==============================
# Write a list comprehension to print a list which contains the multiplication table of a user entered number.
a= int(input("Enter a number: "))
table=[i*a for i in range(1,11)]
print(table)

#============================= Question 4 ==============================
# Write a program to display a/b where a and b are integers. If b=0, 
# display infinite by handling the 'ZeroDivisionError'.
a= int(input("Enter a number: "))
b= int(input("Enter another number: "))
try:
    print(a/b)
except ZeroDivisionError:
    print("Infinite")

#============================= Question 5 ==============================
# Store the multiplication tables generated in problem 3 in a file named Tables.txt.
a= int(input("Enter a number: "))
table=[i*a for i in range(1,11)]
print(table)
with open("Tables.txt", "a") as f:
    f.write(f"Table of {a} : {str(table)} \n")
