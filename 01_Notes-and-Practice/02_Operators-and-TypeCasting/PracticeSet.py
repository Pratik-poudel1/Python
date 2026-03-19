# =========================== Question 1 ===========================
# WAP to add two numbers in Python
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
sum = num1 + num2
print (f"Sum of {num1} and {num2} is: {sum}")


# =========================== Question 2 ===========================
# WAP to find remainder when a number is divided by 2
num =int(input("Enter any Number:"))
rem = num % 2
print ("Remainder of Number After Divided by 2 is :",rem)


# =========================== Question 3 ===========================
# Check the type of a variable assigned using input() function
var = input("Enter something: ")
print("You entered:", var)
print("Type of the variable:", type(var))


# =========================== Question 4 ===========================
# Use Compearison Operator to find out whether a given variable a is greater than 'b' or not.Take a =34 and b=80
a=int(input("Enter First Number :"))
b=int(input("Enter Second Number :"))
print("Is a greater than b?", a>b)


# =========================== Question 5 ===========================
# WAP to find an average of two numbers entered by the user
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
avg = (a+b)/2
print (f"Average of {a} and {b} is: {avg}")


# =========================== Question 6 ===========================
# WAP to calculate the square of a number entered by the user
num=int(input("Enter a Number:"))
sq = num**2  # Or can use sq= num*num
print (f"Square of {num} is: {sq}")

