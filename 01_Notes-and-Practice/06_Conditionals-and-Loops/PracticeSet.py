#================= Question 1 =========================
# WAP to find the greatest of four number entered by User.
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=int(input("Enter Third Number:"))
num4=int(input("Enter Fourth Number:"))
# Or Greatest = max(num1,num2,num3,num4)
# print("Greatest Number is :",Greatest)
if (num1>num2 and num1>num3 and num1>num4):
    print("The Greatest Number is :",num1)
elif (num2>num1 and num2>num3 and num2>num4):
    print("The Greatest Number is :",num2)
elif (num3>num1 and num3>num2 and num3>num4):
    print("The Greatest Number is :",num3)
else:
    print("The Greatest Number is :",num4)

#================= Question 2 =========================
# WAP to find out whether a student is passed or fails,if it requires total 40% and at least 33% in each subject to pass.
# Assume 3 Subjects and take marks as an input from the User.
sub1=float(input("Enter Marks Of Math: "))
sub2=float(input("Enter Marks Of IIT: "))
sub3=float(input("Enter Marks Of DL: "))
per=(sub1+sub2+sub3)/3
if (per>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("Passed")
else:
    print("Fail")

#================= Question 3 =========================
# A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.
text = input("Enter comment: ").lower()

if ("make a lot of money" in text or
    "buy now" in text or
    "subscribe this" in text or
    "click this" in text):
    print("This is a Spam Comment")
else:
    print("Not Spam")

#================= Question 4 =========================
# Write a program to find whether a given username contains less than 10 characters or not
username=input("Enter Your Username: ")
if (len(username)<10):
    print("Username Contains less than 10 Characters")
else:
    print("Username doesnot contains less than 10 characters")

# #================= Question 5 =========================
# Write a program which finds out whether a given name is present in a list or not.
list=["Ram","Hari","Gita","Sita","Pratik","Nishant"]
name=input("Enter a Name: ")
if name in list:
    print("Given Name is in the List")
else:
    print("Given Name is Not in the List")

#================= Question 6 =========================
# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100 → Ex
# 80-90 → A
# 70-80 → B
# 60-70 → C
# 50-60 → D
# <50 → F

marks = int(input("Enter marks: "))
if marks >= 90 and marks <= 100:
    grade = "Ex"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

#================= Question 7 =========================
# Write a program to find out whether a given post is talking about "Pratik" or not.
post = input("Enter the post: ").lower()

if "pratik" in post:
    print("This post is talking about Pratik")
else:
    print("This post is not talking about Pratik")
