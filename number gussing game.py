import random

def number_gussing_game():
    print("welcome to the number gussing game!")
    print("i have chossen a number between 1 and 20.can you guss it?")

    secret_number=random.randint(1,20)
    attempts=0

    while True:
        try:
            guss=int(input("enter your guss:"))
            attempts+=1

            if guss<secret_number:
                print("too low!try again.")
            elif guss>secret_number:
                print("too high!try again.")
            else:
                print(f"congratulations!you gussed the number in{attempts}attempts.")
                break
        except ValueError:
            print("invalid input!please enter a valid number.")

number_gussing_game()
