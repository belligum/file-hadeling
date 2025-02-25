import random

def get_winner(player,computer):
    if player==computer:
        return"it is a tie!"
    elif(player=="rock"and computer=="scissors")or\
        (player=="scissors"and computer=="paper")or\
        (player=="paper"and computer=="rock"):
        return"You win!"
    else:
        return"Computer wins!"
    
choices=["rock","paper","scissors"]

player_choice=input("Enter rock,paper,or scissors:").lower()
if player_choice not in choices:
    print("invalid choice! please enter rock,paper,or scissors.")
else:
    computer_choice=random.choice(choices)

    print(f"\nYou chose:{player_choice}")
    print(f"\ncomputer chose:{computer_choice}")

    result=get_winner(player_choice,computer_choice)
    print("\n"+result)
    