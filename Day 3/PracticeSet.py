# ======================= Ouestion 1 =======================
# WAP to display "Good Afternoon" followed by the user's name.
name = input("Enter your name: ")
print(f"Good Afternoon {name}")

# ======================= Ouestion 2 =======================
WAP to fill in a letter template which looks like below:
Letter = '''Dear <|NAME|>,
            You are selected!
            <|DATE|>  '''

print(Letter.replace("<|NAME|>", "Pratik").replace("<|DATE|>", "16th Feb 2026"))

# ======================= Ouestion 3 =======================
# WAP to detect double spaces in a string.
string = input("Enter a string: ")
print(string.find("  "))  # This will return the index of the first occurrence of double spaces, or -1 if not found.


# ======================= Ouestion 4 =======================
# Replace double spaces with single spaces in the given string.
string = input("Enter a string: ")
print(string.replace("  ", " "))

# ======================= Ouestion 5 =======================
# WAP to format the following letter using escape sequence characters
# Letter = "Dear Harry,
#           This Python course is nice.
#           Thanks!"

Letter = "Dear Harry,\n\tThis Python course is nice.\n\tThanks!"
print(Letter)
