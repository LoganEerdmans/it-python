import random

print("|=====================|")
print("|   GUESS MY NUMBER   |")
print("|  By Logan Eerdmans  |")
print("|=====================|")
print("")

name = input("What is your name?\n\n")
print("")

print("I'm thinking of an integer between 0 and 100. Can you guess it?")
number = random.randint(0, 100)

guess = -1

while guess != number:
    guess_text = input("So, whatcha' think?\n\n")
    guess = int(guess_text)

    if guess > 100 or guess < 0:
        print(f"\nHey {name}, could you perhaps guess a number between the range 0 and 100?")
    elif guess < number:
        print(f"\nSorry {name}, but your number is too LOW!")
    elif guess > number:
        print(f"\nSorry {name}, but your number is too HIGH!")
    else:
        print(f"\nHey, you got it! Well done, {name}!")

print("Thanks for playing. :P")