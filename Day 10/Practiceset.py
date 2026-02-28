#================= Question 1 ===============
# WAP to read the text from a given file 'poems.txt' and find out whether it 
# contains the word 'twinkle'
with open("poem.txt","r") as f:
    content=f.read()
    if ("twinkle" in content):
        print("Twinkle is present in Poem.txt")
    else:
        print("Twinkle is not present in Poem.txt")

#================= Question 2 ===============
# The game[] function in a program lets a user play a game and returns the score as an 
# integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score.
# You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import random
def game():
    print("You are playing the game.")
    score= random.randint(1,10000)
    # Fetch the High score
    with open("Hi-score.txt") as f:
        hiscore=f.read()
        if (hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore=0
    print(f"Your Score: {score}")
    if (score>hiscore or hiscore==""):
        # write this hiscore to the file
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
    return score
game()

#================= Question 3 ===============
# Write a program to generate multiplication tables from 2 to 20 and write it to 
# the different files. Place these files in a folder for a 13 year old.
def generateTable(n):
    table=""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"Tables/table_{n}.txt","w") as f:
        f.write(table)
for i in range(2,21):
    generateTable(i)

#================= Question 4 ===============
# A file contains a word "Donkey" multiple times.
# You need to write a program which replace this word with #### by updating the same file
word="Donkey"
with open("file.txt","r") as f:
    content = f.read()
newcontent=content.replace("Donkey","######")
with open("file.txt","w") as f:
    content = f.write(newcontent)

#================= Question 5 ===============
# Repeat program & for a list of such words to be censored.
words=["Donkey","animal","bad"]
with open("file.txt","r") as f:
    content = f.read()
for word in words:
    content=content.replace(word,"#"*len(word))
    
with open("file.txt","w") as f:
    content = f.write(content)

#================= Question 6 ===============
# Write a program to mine a log file and find out whether it contains 'python'
with open("log.txt","r")as f:
    content=f.read()
if("python" in content):
    print("Python is Present")
else:
    print("Python is not Present")

#================= Question 7 ===============
# Write a program to find out the line number where python is present from ques 6.
with open("log.txt","r")as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("python" in line):
        print(f"Python is Present.Line no:{lineno}")
        break
    lineno+=1

else:
    print("Python is not Present")

#================= Question 8 ===============
# Write a program to make a copy of a text file "this. txt"
with open("this.txt")as f:
    content=f.read()
with open("this_copy.txt","w")as f:
    content=f.write(content)

#================= Question 9 ===============
# Write a program to find out whether a file is identical & matches the content of another file.
with open("this.txt")as f:
    content1=f.read()
with open("this_copy.txt")as f:
    content2=f.read()
if (content1==content2):
    print("Yes,The files are identical")
else:
    print("No,The file are not identical")

#================= Question 10 ===============
# Write a program to wipe out the content of a file using python.
with open("copy.txt","w")as f:
    f.write("")

#================= Question 11 ===============
# Write a python program to rename a file to "renamed_by_python.txt
with open("old.txt")as f:
    content=f.read()
with open("renamed_by_python.txt","w")as f:
    f.write(content)
