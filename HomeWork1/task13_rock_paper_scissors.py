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

if player != "rock" and player != "paper" and player != "scissors":
    print("Wrong choice")
elif player == computer:
    print("Draw")
elif player == "rock" and computer == "scissors":
    print("You win")
elif player == "paper" and computer == "rock":
    print("You win")
elif player == "scissors" and computer == "paper":
    print("You win")
else:
    print("You lose")
