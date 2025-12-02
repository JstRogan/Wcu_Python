import random

print("Rock Paper Scissors")
print("Choose: rock, paper or scissors")

player = input("Your choice: ").strip().lower()

number = random.randint(1, 3)

if number == 1:
    computer = "rock"
elif number == 2:
    computer = "paper"
else:
    computer = "scissors"

print("Computer chose:", computer)

if player == "rock":
    if computer == "rock":
        print("Draw")
    elif computer == "scissors":
        print("You win")
    else:
        print("You lose")
elif player == "paper":
    if computer == "paper":
        print("Draw")
    elif computer == "rock":
        print("You win")
    else:
        print("You lose")
elif player == "scissors":
    if computer == "scissors":
        print("Draw")
    elif computer == "paper":
        print("You win")
    else:
        print("You lose")
else:
    print("Wrong choice")
