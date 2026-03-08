# Python Password Generator and Strength Checker

This project includes two Python scripts that help you create and evaluate passwords.
You can generate strong passwords and check any password for strength and missing components.

## Files

### 1. `password_generator.py`
This script generates a strong password for you. It ensures your password contains:

- At least one lowercase letter
- At least one uppercase letter
- At least one digit
- At least one special character

The script shuffles the characters to remove predictable patterns. Once the password is ready, it copies it to your clipboard so you can use it immediately.

**How to use:**

1. Run `password_generator.py`.
2. Enter the desired password length (minimum 8 characters).
3. The script displays your password, its length, and copies it to the clipboard.

### 2. `password_strength_checker.py`
This script checks the strength of any password you enter. It scores your password and tells you which character types are missing.

It checks:

- Minimum length of 8 characters
- Presence of lowercase letters
- Presence of uppercase letters
- Presence of digits
- Presence of special characters

**How to use:**

1. Run `password_strength_checker.py`.
2. Enter the password you want to check.
3. The script displays the password strength: Very Strong, Strong, Medium, or Weak.
4. It also lists missing character types, if any.


# Example

## Password Generator:

```
Enter the length of the password: 12
Password: A8#kLm2@PqR
Length: 12
Password copied to clipboard.
```

## Password Strength Checker:

```
Enter your password: A8#kLm2@PqR
Password is very strong.
Missing characters: None
```


## Why Use This Project

You can generate passwords that meet standard security requirements. You can also evaluate any password and see exactly what makes it strong or weak. This helps you protect your accounts with better passwords.


## Requirements

- Python 3.x  
- `pyperclip` module for clipboard functionality in `password_generator.py`

Install `pyperclip` using:

```bash
pip install pyperclip