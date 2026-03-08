# Making a Password Strength Checker using python

import string

def missing_chars(password):
    missing_chars = []
    if len(password) < 8:
        missing_chars.append("At least 8 characters")
    if not any(char.islower() for char in password):
        missing_chars.append("Lowercase letter")
    if not any(char.isupper() for char in password):
        missing_chars.append("Uppercase letter")
    if not any(char.isdigit() for char in password):
        missing_chars.append("Digit")
    if not any(char in string.punctuation for char in password):
        missing_chars.append("Special character")
    return missing_chars

password=input("Enter your password: ")
score=0

if len(password)>=8:
    score+=1
if any(char.islower() for char in password):
    score+=1
if any(char.isupper() for char in password):
    score+=1
if any(char.isdigit() for char in password):
    score+=1
if any(char in string.punctuation for char in password):
    score+=1

if score==5:
    print("Password is very strong.")
elif score==4:
    print("Password is strong.")
elif score==3:
    print("Password is medium.")
else:
    print("Password is weak.")

missing = missing_chars(password)
if missing:
    print("Missing characters:", ", ".join(missing))