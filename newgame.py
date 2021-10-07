import random
from enum import IntEnum

class Choice(IntEnum):
    Rock=0
    Paper=1
    Scissors=2
    Lizard=3
    Spock=4

CHOICES = [f"{choice.name}[{choice.value}]" for choice in Choice]
CHOICES_STR = ", ".join(CHOICES)

BEATS = {
    Choice.Rock: [Choice.Scissors, Choice.Lizard, ],
    Choice.Paper: [Choice.Rock, Choice.Spock, ],
    Choice.Scissors: [Choice.Paper, Choice.Lizard, ],
    Choice.Lizard:[Choice.Paper, Choice.Spock, ],
    Choice.Spock: [Choice.Scissors, Choice.Rock, ],
}

MESSAGES = {
    (Choice.Rock, Choice.Scissors): "crushes",
    (Choice.Rock, Choice.Lizard): "crushes",
    (Choice.Paper, Choice.Rock): "covers",
    (Choice.Paper, Choice.Spock): "disproves",
    (Choice.Scissors, Choice.Paper): "cut",
    (Choice.Scissors, Choice.Lizard): "decapitates",
    (Choice.Lizard, Choice.Paper): "eats",
    (Choice.Lizard, Choice.Spock): "poisons",
    (Choice.Spock, Choice.Scissors): "smashes",
    (Choice.Spock, Choice.Rock): "vaporizes",
}


def show_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"It's a tie! Both users choice '{computer_choice.name}'")
    elif user_choice not in BEATS.keys():
        print(f"\nYou typed '{user_choice}' which isn't valid throw")
    else:
        # BEATS[user_choice] is the list of things user_choice wins over
        user_wins = computer_choice in BEATS[user_choice]

        if user_wins:
            verb = MESSAGES[(user_choice, computer_choice)]
            print(
                f"{user_choice.capitalize()} {verb} {computer_choice}, you win!"
            )
        else:
            verb = MESSAGES[(computer_choice, user_choice)]
            print(
                f"{computer_choice.capitalize()} {verb} {user_choice}, you lose!"
            )

while True:
    print("Make your throw:")
    try:
        value = input(f"    Enter a choice ({CHOICES_STR}): ")
        user_choice = Choice(int(value))
    except:
        print(f"\nYou typed '{value}' which isn't a valid choice.")
        continue

    value = random.randint(0, len(Choice) - 1)
    computer_choice = Choice(value)
    show_winner(user_choice, computer_choice)

    again = input("\nWant some more? (y/n): ")
    if again.lower() == "n":
        break

    print()

print("\nGoodbye!")