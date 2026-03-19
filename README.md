# Python Learning Journey

Hi! This is my Python repository where I have been putting all my code since I started learning Python. I am a first semester CSIT student and this is basically my whole journey from writing `print("Hello World")` to making actual working programs with GUI and everything.

I started this because our college has Python in the syllabus and honestly I wanted to practice more than what we do in lab. So I just kept adding stuff here as I learned new things.

---

## What's Inside

The repo is divided into three folders. I tried to keep things organized.

```
Python/
├── 01_Notes-and-Practice/     ← chapter wise notes and exercises
├── 02_Projects/               ← terminal/CLI projects
└── 03_GUI-Projects/           ← projects with actual windows (tkinter, pygame)
```

---

## 01 - Notes and Practice

This is where I wrote code while learning each topic. Every chapter has a main notes file and a practice set. I tried to add comments explaining what each thing does because honestly future me will forget.

| Chapter | Topic |
|---|---|
| 01 | Variables and Basics |
| 02 | Operators and Type Casting |
| 03 | Strings and String Functions |
| 04 | Lists and Tuples |
| 05 | Dictionaries and Sets |
| 06 | Conditionals and Loops |
| 07 | Functions and Scope |
| 08 | Recursion |
| 09 | Mini Project 1 |
| 10 | File Handling |
| 11 | OOP - Classes and Objects |
| 12 | OOP - Inheritance and Decorators |
| 13 | Mini Project 2 |
| 14 | Advanced Python Concepts |
| 15 | Virtual Environments and Modules |

The recursion chapter was honestly the hardest one for me to understand. I spent like two days just on factorial before it clicked. The OOP chapters took even longer but I am glad I did them because the projects became way easier after.

---

## 02 - Projects (CLI / Terminal)

These run in the terminal. No fancy windows, just input and output. But I am actually proud of some of these.

### Rock Paper Scissors
Classic game. You vs the computer. Computer picks randomly, you type your choice. Simple but it was one of my first "complete" programs.

### Quiz Game
A multiple choice quiz. Has questions, options, tracks your score. I added a score at the end.

### Password Generator
Generates a random password based on the length you want. Uses uppercase, lowercase, numbers, special characters. You can customize what to include.

### Password Checker
Checks how strong a password is. Tells you if it's weak, medium or strong based on length and character types.

### Expense Tracker
This one saves your expenses to a CSV file so the data is not lost when you close the program. You can add expenses with category and date, and view a summary. The CSV part took me a while to figure out.

### Pomodoro Timer
A 25 minute work timer with 5 minute break. Based on the Pomodoro technique. Runs in the terminal and beeps when the timer is done.

### Gaming Gadget Store
This is the biggest one. It is a full billing system for an imaginary gaming store. It has:
- User registration and login (stores credentials in a file)
- A product catalog with 15 items
- Shopping cart
- Membership discounts (Silver 10%, Gold 15%, Platinum 25%)
- Gift wrap options
- Home delivery or store pickup
- VAT calculation (13% inside Kathmandu, 15% outside)
- Loyalty points
- Card payment simulation with PIN
- Saves bill to a record file

I spent the most time on this one. It is not perfect but it works.

### Automated File Organizer
Scans a folder and moves files into subfolders by type. Like all `.jpg` files go into an Images folder, all `.pdf` go into Documents, etc. Actually useful.

---

## 03 - GUI Projects

These have actual windows. I used `tkinter` for most of them and `pygame` for the game.

### Greeting GUI
My first ever GUI program. Just takes your name and shows a greeting. Small but it felt amazing when the window opened for the first time.

### Calculator GUI
A working calculator with buttons. Does basic math. Nothing fancy but the button layout took longer than expected.

### To-Do List GUI
Add tasks, mark them done, delete them. Has a simple list view. Data does not save when you close it though, that is something I want to fix later.

### Unit Converter GUI
Converts between units. Length, weight, temperature. Dropdown menus for selecting what to convert.

### Expense Tracker GUI
Same logic as the CLI expense tracker but with a proper window. Has input fields and shows the list of expenses in a table.

### Catch Balls Game (Pygame)
A game where balls fall from the top and you move a paddle to catch them. Built with pygame. Score goes up every time you catch one. Arrow keys to move. This was really fun to make and also really confusing at first because pygame is different from everything else.

---

## How to Run

You need Python 3 installed. Most files just need the standard library.

For the pygame game you need to install pygame first:

```bash
pip install pygame
```

For the GUI projects you need tkinter (usually comes with Python on Windows, on Linux you might need to install it):

```bash
sudo apt install python3-tk
```

Then just run any file with:

```bash
python filename.py
```

---

## Folder Structure (detailed)

```
Python/
│
├── 01_Notes-and-Practice/
│   ├── 01_Variables-and-Basics/
│   │   ├── Hello.py
│   │   ├── Chapter1.py
│   │   └── PracticeSet.py
│   ├── 02_Operators-and-TypeCasting/
│   ├── 03_Strings-and-Functions/
│   ├── 04_Lists-and-Tuples/
│   ├── 05_Dictionaries-and-Sets/
│   ├── 06_Conditionals-and-Loops/
│   ├── 07_Functions-and-Scope/
│   ├── 08_Recursion/
│   ├── 09_Mini-Project/
│   ├── 10_File-Handling/
│   ├── 11_OOP-Classes-and-Objects/
│   ├── 12_OOP-Inheritance-and-Decorators/
│   ├── 13_Mini-Project-2/
│   ├── 14_Advanced-Python-Concepts/
│   └── 15_Virtual-Environments-and-Modules/
│
├── 02_Projects/
│   ├── Rock-Paper-Scissors/
│   ├── Quiz-Game/
│   ├── Password-Tools/
│   ├── Expense-Tracker/
│   ├── Pomodoro-Timer/
│   ├── Gaming-Gadget-Store/
│   ├── Music-Player/
│   └── Automated-File-Organizer/
│
└── 03_GUI-Projects/
    ├── Greeting-GUI/
    ├── Calculator-GUI/
    ├── To-Do-List-GUI/
    ├── Unit-Converter-GUI/
    ├── Expense-Tracker-GUI/
    └── Catch-Balls-Game/
```

---

## Things I Learned

Not just Python syntax but also things like:

- How to break a big problem into small functions
- Reading and writing files (file handling was honestly confusing but important)
- OOP made my brain hurt but property decorators are actually really cool once you get them
- pygame is a completely different world
- Comments are important. I stopped writing them for a while and then came back to my own code and had no idea what it did

---

## Things I Want to Add Later

- Save data properly in the To-Do list (maybe use SQLite)
- Add more questions to the Quiz game
- Fix the password storage in Gaming Gadget Store (plain text is not safe, I know)
- Maybe add a leaderboard to the Catch Balls game

---

## Note

Some of the early code is not great. I look at my Chapter 1 stuff now and it is a bit embarrassing. But that is kind of the point I guess. The repo shows the whole process, not just the final result.

If you are also learning Python and any of this code helps you understand something, that is great.

---

*Made by Pratik Poudel — CSIT 1st Semester*