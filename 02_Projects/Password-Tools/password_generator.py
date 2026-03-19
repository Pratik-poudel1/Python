# Making a password generator using python

import random
import string
import pyperclip

def get_mandatory_chars():
    l_case=random.choice(string.ascii_lowercase)
    password_chars.append(l_case)
    u_case=random.choice(string.ascii_uppercase)
    password_chars.append(u_case)
    num=random.choice(string.digits)
    password_chars.append(num)
    sym=random.choice(string.punctuation)
    password_chars.append(sym)
    return

def get_random_chars(length):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    for _ in range(length-4):
        random_char = random.choice(characters)
        password_chars.append(random_char)
    return 

def assemble_password(password_chars):
    random.shuffle(password_chars)
    return ''.join(password_chars)

while True:
    password_chars = []
    try:
        length = int(input("Enter the length of the password: "))
        if length < 8:
            print("Password length must be at least 8 characters.")
            print("Passwords shorter than 8 are weak and easily hackable.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue
    print("==============================================================")
    print("\t\t\tPASSWORD GENERATOR\t\t\t")
    print("==============================================================")
    get_mandatory_chars()
    get_random_chars(length)
    password = assemble_password(password_chars)
    print("Password:", password)
    print("Length:", len(password))
    pyperclip.copy(password)
    print("Password copied to clipboard.")
    print("==============================================================")
    break