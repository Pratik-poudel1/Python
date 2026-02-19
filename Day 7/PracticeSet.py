#========================== Question 1 ==========================
# WAP to print multiplication table of a given nnumber using for loop.
num=int(input("Enter any Number: "))
i=0
for i in range(1,11):
    print(num,"*",i,"=",num*i)
    i += 1

#========================== Question 2 ==========================
# WAP to greet all the person names stored in a list "l" and which starts with S
l=["Harry","Soham","Sachin","Rahul"]
for i in l:
    if i.startswith("S"):
        # if i[0]="S":
        print("Good Morning ! ",i)

#========================== Question 3 ==========================
# Attempt problem 1 Using While Loop
num=int(input("Enter any Number: "))
i=0
while (i<11):
    print(num,"*",i,"=",num*1)
    i += 1

#========================== Question 4 ==========================
# WAP to find whether a given number is Prime or Not.
num=int(input("Enter a Number :"))
i=2
if num <= 1:
    print(num, "is not a Prime Number")
isprime=0
for i in range (2,num):
    if num % i == 0:
        isprime += 1
        break
if isprime==0:
    print(num,"is a Prime Number")
else:
    print(num,"is not a Prime Number")

#========================== Question 5 ==========================
# WAP to find the sum of first n natural number using while loop
n=int(input("Enter any Number : "))
sum=0
i=1
while i<n+1:
    sum = sum + i
    i += 1
print (f"Sum of {n} Numbers is {sum}")

#========================== Question 6 ==========================
# WAP to calculate the factorial of a given number using for loop
num = int(input("Enter any Number: "))
if num < 0:
    print("Factorial Does Not Exist")
elif num == 0:
    print(f"Factorial of {num} is 1")
else:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(f"Factorial of {num} is {fact}")

#========================== Question 7 ==========================
# WAP to print  the following star pattern.
#   *
#  ***           
# *****           for n=3
n = int(input("Enter any Number :"))
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))

#========================== Question 8 ==========================
# WAP to print the following star pattern.
# *
# **
# ***
n=int(input("Enter any Number :"))
for i in range(1,n+1):
    print("*"*i)

#========================== Question 9 ==========================
# WAP to print the following star pattern.
# ***
# * *
# ***
n = int(input("Enter a number: "))
for i in range(n):
    if i == 0 or i == n-1:
        print("*" * n)
    else:
        print("*" + " "*(n-2) + "*")

#========================== Question 10 ==========================
# WAP to print multiplication table of n using for loop in reversed order
n= int(input("Enter any Number: "))
for i in range(10,0,-1):
    print(n,"*",i,"=",n*i)
