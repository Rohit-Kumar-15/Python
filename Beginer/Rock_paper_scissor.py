import random

def get_choices():
    player_choice = input("Enter a Choice (rock, paper, scissor) : ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)

    choices = {"player":player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"you chose {player}, Computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    
    elif player == "rock":
        if computer == "scissor":
            return "Rock Smashes Scissor! You Win!"
        else:
            return "Paper covers Rock! You lose."

    elif player == "paper":
            if computer == "rock":
                return "Paper covers Rock! You Win!"
            else:
                return "Scissor cuts Paper! You lose."

    elif player == "scissor":
            if computer == "paper":
                return "Scissor cuts Paper! You Win!"
            else:
                return "Rock Smashes Scissor! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)