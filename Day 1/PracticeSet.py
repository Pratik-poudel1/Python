# WAP to print Twinkle Twinkle Little Star using Python.

# This is a multi-line string in Python, which can be used to print multiple
# lines of text without needing to use multiple print statements.
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.''')


# Use REPL and print the Table of % Usinng Python.
print("\nTable of 5")
print(5*1)
print(5*2)
print(5*3)
print(5*4)
print(5*5)
print(5*6)
print(5*7)
print(5*8)
print(5*9)
print(5*10)


# Install an external module and use it to perform an operation of your interest.
import pyttsx3
engine = pyttsx3.init()
engine.say('''Hello, welcome to Python programming!
    This is an example of using the pyttsx3 module to convert text to speech.
    You can use this module to create applications that can speak to the user.''')
engine.runAndWait()


# WAP to print the contents of a Directory using the OS module.
# Search for the OS module in Python and use it to print the contents of a directory of your choice.
import os

# Specify the directory path
directory_path = r"E:"   # Change this to your desired path

try:
    # Get list of files and folders
    contents = os.listdir(directory_path)

    print(f"Contents of directory: {directory_path}\n")

    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")


