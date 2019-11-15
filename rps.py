import random
from banner import banner

banner("Rock, Paper, Scissors", "Logan Eerdmans")

name = input("Howdy. What's your name?\n")

print(f"\nHey {name}! We're going to play Rock, Paper, Scissors.")
print("The first to win two out of three rounds is determined the winner.\n")

pscore = 0
cscore = 0

while pscore < 2 and cscore < 2:
    print(f"SCORE: Player: {pscore} Computer: {cscore}")
    print("1. Rock\n2. Paper\n3. Scissors")
    pchoice = int(input("What is your choice (Choose a number)?\n"))
    print("")

    cchoice = random.randint(1, 3)

    if pchoice == cchoice:
        if pchoice == 1:
            print("You chose rock, and the computer chose rock. It's a tie!")
        elif pchoice == 2:
            print("You chose paper, and the computer chose paper. It's a tie!")
        else:
            print("You chose scissors, and the computer chose scissors. It's a tie!")
    if pchoice == 1:
        if cchoice == 2:
            print("You chose rock, and the computer chose paper. The computer wins this round!")
            cscore += 1
        else:
            print("You chose rock, and the computer chose scissors. You win this round!")
            pscore += 1
    if pchoice == 2:
        if cchoice == 1:
            print("You chose paper, and the computer chose rock. You win this round!")
            pscore += 1
        else:
            print("You chose paper, and the computer chose scissors. The computer wins this round!")
            cscore += 1
    if pchoice == 3:
        if cchoice == 1:
            print("You chose scissors, and the computer chose rock. The computer wins this round!")
            cscore += 1
        else:
            print("You chose scissors, and the computer chose paper. You win this round!")
            pscore += 1

if cscore >= 2:
    print("The computer wins! You lose this game. Better luck next time!")
else:
    print("You won! You defeated the merciless, stingy computer!")