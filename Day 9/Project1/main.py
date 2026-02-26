# We all have played snake, Water gun game in our childhood. If you haven't, google the rules of this game 
# and write a python program capable of playing this game with the user.

# 1 for Snake
# -1 for Water
# 0 for Gun

import random

game_dict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

while True:
    # User Input
    player = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

    # Computer Choice
    computer = random.choice([-1, 0, 1])

    # Convert user choice
    if player not in game_dict:
        print("Invalid Input!")
    else:
        p1 = game_dict[player]
        p2 = computer

        print(f"You chose {reverse_dict[p1]}")
        print(f"Computer chose {reverse_dict[p2]}")

        # Game Logic
        if (p1==-1 and p2==-1):
            print("Game Draw !")
        elif (p1==1 and p2==-1):
            print("You Wins !")
        elif (p1==1 and p2==1):
            print("Game Draw !")
        elif (p1==1 and p2==0):
            print("Computer Wins !")
        elif (p1==-1 and p2==1):
            print("Computer Wins !")
        elif (p1==-1 and p2==0):
            print("You Wins !")
        elif (p1==0 and p2==0):
            print("Game Draw !")
        elif (p1==0 and p2==-1):
            print("You Wins !")
        else:
            print("Player Wins")
    again=input("Do you want to play again (Y for yes and N for No) : " )
    if (again != 'y' and again != 'Y'):
        print("Thank you for Playing !")
        break
        
