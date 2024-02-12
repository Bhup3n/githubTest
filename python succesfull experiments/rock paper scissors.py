import random
import time

choices = ["rock", "paper", "scissors"]
play = True
while play == True:
    computer = random.choice(choices)
    player = None  # player = nothing
    while player not in choices:
        player = input("rock, paper, or scissors:").lower()  # the .lower() means if they type the object in all caps, it will put it all lower case so its not case sensitive

    print("computer:", computer)
    time.sleep(1)
    print("you:", player)
    time.sleep(1)

    if player == computer:
        print("its a tie!")
    elif player == "rock":
        if computer == "paper":
            print("you lose!")
        else:
            print("you win!")
    elif player == "paper":
        if computer == "scissors":
            print("you lose!")
        else:
            print("you win!")
    else:
        if computer == "rock":
            print("you lose!")
        else:
            print("you win!")

    play_again = input("do you want to play again, yes or no:").lower()
    if play_again == "yes":
        pass
    else:
        break