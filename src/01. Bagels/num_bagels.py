"""Bagels, by Al Sweigart al@inventwithpython.com 
A deductive logic game where you must guess a number based on clues.
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3  # (!) try setting this to 1 or 10
MAX_GUESSES = 10  # (!) try setting this to 1 or 100


def main():
    print(
        """Bagels, a deductive logic game. By Al Sweigart al@inventwithpython.com
        
I am thinking of a {NUM_DIGITS}-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
    Pico       One digit is correct but in the wrong position.
    Femi       One digit is correct and in the right position.
    Bagels     No digit is correct.
For example, if the secret number was 248 and your guess was 734, I would say:
Fermi Pico Bagels""".format(
            NUM_DIGITS=NUM_DIGITS
        )
    )

    while True:
        secret_number = get_secret_number()
        print("I have thought up a number.")
        print("You have {} tries to get it.".format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(num_guesses))
                guess = input("> ")

            clues = get_clues(guess, secret_number)
            print(clues)
            num_guesses += 1

            if guess == secret_number:
                break
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secret_number))
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")


def get_secret_number():
    """prints a string made up of NUM_DIGITs randon digits"""
    numbers = list(range(10))
    random.shuffle(numbers)
    secret_number = ""
    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    return secret_number


def get_clues(guess, secret_number):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secret_number:
        return "You got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append("Fermi")
        elif guess[i] in secret_number:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"  # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return " ".join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
