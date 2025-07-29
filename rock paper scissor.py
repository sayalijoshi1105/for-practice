import random

choices = ["rock", "paper", "scissors"]

user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print("You chose:", user)
print("Computer chose:", computer)

