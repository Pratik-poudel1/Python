#===================== Question 1 ========================
# WAP using function to find greatest of three numbers.
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))
print(f"Greatest Number is {greatest(a,b,c)}")

# OR def greatest(a,b,c):
#       return max(a,b,c)

#===================== Question 2 ========================
# WAP using function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(temp):
    return (9/5) * temp + 32

temp = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(temp)

print(f"Temperature in Fahrenheit: {fahrenheit}")

#===================== Question 3 ========================
# How do you prevent a python print() function to print a new line at the end.
print("a")
print("b")
print("c",end="")   # use end="" to prevent a new line
print("d",end="")

#===================== Question 4 ========================
# WAP to print first n lines of the following pattern.
# ***
# **
# *         -for n=3
def pat(n):
    for i in range(1,n+1):
        print("*"*i)
n=int(input("Enter any Number: "))
pat(n)

#===================== Question 5 ========================
# WAP a function which convert inches to cms.
def inch_to_cms(l):
    return l*2.54
l=float(input("Enter Length in Inches: "))
print(f"Length into cms : {inch_to_cms(l)}")

#===================== Question 6 ========================
# WAP a recursive function to calcuate the sun of first n natural numbers.
def sum(n):
    if n==1: 
        return 1
    return n+sum(n-1)
n=int(input("Enter a Number: "))
print(f"Sum of first {n} natural number is {sum(n)}")

#===================== Question 7 ========================
# WAP a function to remove a given word from a list ad strip it at the same time.
list=["Ram","Sita","Pratik","Hari","Rajesh","esh"]
def rem(list,word):
    n=[]
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n
print(rem(list,"esh"))

#===================== Question 8 ========================
# WAP a function to print multiplication table of a given number.
def table(num):
    for i in range (1,11):
        print(num,"*",i,"=",num*i)
num=int(input("Enter any Number: "))
print(f"Multiplication Table of {num}")
table(num)