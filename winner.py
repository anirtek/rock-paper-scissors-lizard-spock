import random

CHOICES = ["ROCK", "PAPER", "SCISSORS"]

print("Make your throw :")

def show_winner(uc, cc):
    if uc == cc:
        print(f"It's a tie! Both users choice '{cc}'")
    elif uc == CHOICES[0]:
        if cc == CHOICES[2]:
            print("Rock smashesh scissors, you win!")
        else:
            print("Paper covers rock, you loose!")
    elif uc == CHOICES[1]:
        if cc == CHOICES[0]:
            print("Paper covers rock, you win!")
        else:
            print("Scissors cut paper, you loose!")
    elif uc == CHOICES[2]:
        if cc == CHOICES[1]:
            print("Scissors cut paper, you win!")
        else:
            print("Rock smashes scissors, you loose!")
    else:
        print(f"\nYou typed '{user_choice}' which isn't valid throw")

while True:
    user_choice = input("   Type rock, paper or scissors: ")
    computer_choice = random.choice(CHOICES)
    show_winner(user_choice.upper(), computer_choice)

    again = input("\nWant some more? (y/n): ")
    if again.lower() == "n":
        break

    print()

print("\nGoodbye")
