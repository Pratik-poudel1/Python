# File I/O
# The RAM memory is volatile, and all its contents are lost once a program 
# terminates in order to presist the data forever, we use files.

# A file is data stored in a storage device. A python program can talk to the file by reading 
# content from it and writing content to it.

# Types of File :
# 1. Text files(.txt, .c etc)
# 2. Binary files(.jpg, .dat, etc)

# Python has a lot of functions for reading,updating and deleting files.

# Opening a File: 
# Python has an open() function for opening files. It takes 2 parameters: filename and made.

# Syntax:
#           open("filename","mode of opening(read mode)")
# Example: open("this.txt","r")

# Example :
f = open("this.txt")    # w for write mode,r for read mode
data=f.read()           # Helps to read a file
print(data)
f.close()               # Whenever a file is opened, it must be closed after use.