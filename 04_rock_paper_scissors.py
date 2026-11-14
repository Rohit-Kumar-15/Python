# FILE 4: Mini project - Rock Paper Scissors
# Play against the computer.
# Concepts: input, random, conditions, loops, and score tracking.

import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("=== ROCK PAPER SCISSORS ===")
print("Type rock, paper, or scissors.")
print("Type quit to stop playing.\n")

while True:
    player = input("Your choice: ").lower().strip()

    if player == "quit":
        break

    if player not in choices:
        print("Invalid choice. Try again.\n")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> You: {player_score} | Computer: {computer_score}\n")

print("\n=== FINAL SCORE ===")
print(f"You: {player_score}")
print(f"Computer: {computer_score}")
print("Thanks for playing!")
