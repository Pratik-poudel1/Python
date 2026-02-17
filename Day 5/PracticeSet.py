#========================= Question 1 =========================
# WAP to create a dictionary of Nepali words and their English meanings. Provide the user with an option to look it up.
words={
    "Namaste": "Hello",
    "Dhanyabad": "Thank you",
    "Biralo": "Cat",
    "Kukur": "Dog",
    "Paani": "Water"
}
word=input("Enter a Nepali word to look up its English meaning: ")
print(words[word])

#========================= Question 2 =========================
# WAP to input eight numbers from the user and display all the unique numbers(once).
num=set()
num1=int(input("Enter a number: "))
num.add(num1)
num.add(int(input("Enter a number: ")))
num.add(int(input("Enter a number: ")))
num.add(int(input("Enter a number: ")))
num.add(int(input("Enter a number: ")))
num.add(int(input("Enter a number: ")))
num.add(int(input("Enter a number: ")))
num.add(int(input("Enter a number: ")))
print("The unique numbers are:",num)

#========================= Question 3 =========================
# Can we have a set with 18(int) and "18"(str) as its elements? If yes, write a code to create such a set.
my_set={18,"18"}
print(my_set)

#========================= Question 4 =========================
# What will be the length of the following set s:
s= set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s)) # The length of the set will be 2 because 20 and 20.0 are considered the same element in a set,
# while "20" is a different element.

#========================= Question 5 =========================
s={} # What is the type of s? Is it a set or a dictionary? 
print(type(s)) # The type of s is <class 'dict'>, which means it is a dictionary, not a set.

#========================= Question 6 =========================
# Create an empty dictionary.Allow 4 friends to enter their favourite language as values and use key as their names.
# Assume that the names are unique.
languages={}
name=input("Enter name of the friend: ")
lang=input("Enter favourite language: ")
languages.update({name: lang})
name=input("Enter name of the friend: ")
lang=input("Enter favourite language: ")
languages.update({name: lang})
name=input("Enter name of the friend: ")
lang=input("Enter favourite language: ")
languages.update({name: lang})
name=input("Enter name of the friend: ")
lang=input("Enter favourite language: ")
languages.update({name: lang})
print(languages)

#========================= Question 7 =========================
# If the names of 2 firends are same; what will happen to the program in problem 6
# If the names of 2 friends are the same, the program will overwrite the value of the key with the new value.

# For example, if Alice and Bob have the same name,
# the program will only store the favourite language of the last person who entered their name as "Alice" or "Bob".
# The previous entry will be lost.

#========================= Question 8 =========================
# If language of one friend is same as another friend; what will happen to the program in problem 6
# If the language of one friend is the same as another friend, it will not affect the program because the keys (names) are unique.
# For example, if Alice and Bob both have "Python" as their favourite language,
# the program will still store both entries without any issues.

#========================= Question 9 =========================
# Can we change the values inside a list which is contained inside a set? Write a code to check your answer.
my_set={8,7,12,"Pratik",[1,2]} # This will raise a TypeError because lists are mutable and cannot be added to a set.
print(my_set)
