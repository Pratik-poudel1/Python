string = "Hello Everyone ! This is me Pratik Poudel"

f= open("myfile.txt","w")
f.write(string)
f.close


# In Open function:
# r -> open for reading
# w -> open for writing
# a -> open for appending
# + -> open for updating
# rb -> open for reading in binary mode
# rt -> open for reading in text mode

# Other Method to read the file:
# We can use f.readline() function to read one full line at a time.
f= open("myfile.txt","w")
lines=f.readlines()    # Read one line from the file
print(lines)
f.close()

f= open("myfile.txt","w")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)

# Another way:

line=f.readline()
while(line!=""):
    print(line)
    line = f.readline()
f.close()

# Write Files in Python:
# In order to write ta a file,we first open it in write or append mode after which,
# we use the python's f.write() method to write to the file.

f= open("this.txt","w")
f.write("\nThis a added line\n")
f.close()

# WITH Statement:
# The best way to pen and close the file automatically is the with statement.
# Open the file in read mode using 'with', which automatically closes the file
with open("this.txt","r") as f:
    text= f.read()
print(text)
