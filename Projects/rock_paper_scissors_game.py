import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices) # chooses a random choice from the list for computer

    player = None
    while player not in choices:
        player = input("Rock, paper, scissors, shoot! ").lower() # forces the user to input a choice within our choices

# All of this down here is just to make rock go over scissors, scissors over paper, and paper over rock
    if player == computer:
        print("Computer: " + computer)
        print("Player: " + player)
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You lose!")
        if computer == "scissors":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You lose!")
        if computer == "rock":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You lose!")
        if computer == "paper":
            print("Computer: " + computer)
            print("Player: " + player)
            print("You win!")

    # Asks  the user if they want to play again
    play_again = input("Play Again: Yes/No  ").lower()
    if  play_again != "yes":
        break