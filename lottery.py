import random
from banner import banner

banner("Lottery", "Logan Eerdmans")

print("Welcome to the Lottery Game. Choose a number between 1 and 999. If you choose the\nsame as the computer, you will win 10 times your bet amount!")

again = "Y"
balance = 20

while again.capitalize() == "Y":

    if balance <= 0:
        balance = 20

    while balance > 0 and balance < 1000000:

        print(f"\nBALANCE: ${balance}")

        bet = int(input("How much do you want to bet? "))
        if bet > balance:
            print("You don't have the BALANCE to bet that much.")
        elif bet <= 0:
            print("Please input a valid bet amount.")
        else:
            choice = int(input("What number do you pick? "))
            if choice > 999 or choice < 0:
                print("Please input a valid number between 1 and 999.")
            else:
                balance -= bet
                winnum = random.randint(1, 999)
                if choice == winnum:
                    wincash = bet * 10
                    print(f"Awesome, you chose {choice}, and so did the computer! You win ${winner} this round.")
                    balance += wincash
                else:
                    print(f"I'm sorry, you chose {choice} and the computer chose {winnum}. You lose ${bet} this round.")

    if balance <= 0:
        print("\nAww, you went bankrupt! Too bad. Better luck next time.")

        again = input("\nWant to give it another go (Y/N)? ")
    elif balance < 1000000:
        print("Congratulations, you've reached over a million dollars! That's nuts, man.")

        again = input("Want to give it another go (Y/N)? ")

print("\nThanks for playing the Lottery!")