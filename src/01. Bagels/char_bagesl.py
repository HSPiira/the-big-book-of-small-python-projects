import random

MAX_CHAR = 3
MAX_GUESSES = 10


def main():
    print(
        """Bagels, a deductive logic game. By Al Sweigart al@inventwithpython.com
        
I am thinking of a {MAX_CHAR}-character string. Try to guess what it is.
Here are some clues:
When I say:    That means:
    Pico       One character is correct but in the wrong position.
    Fermi      One character is correct and in the right position.
    Bagels     No character is correct.
For example, if the secret string was 248 and your guess was 734, I would say:
Fermi Pico Bagels""".format(
            MAX_CHAR=MAX_CHAR
        )
    )

    while True:
        secret_string = get_secret_string()
        print("I have thought up a string.")
        print("You have {} tries to get it.".format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != MAX_CHAR or not guess.isalpha():
                print("Guess #{}: ".format(num_guesses))
                guess = input("> ").upper()

            clues = get_clues(guess, secret_string)
            print(clues)
            num_guesses += 1

            if guess == secret_string:
                break
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print("The answer was {}.".format(secret_string))
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")


def get_secret_string():
    """Returns a string of MAX_CHAR random characters"""
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(letters)
    secret_string = ""
    for i in range(MAX_CHAR):
        secret_string += letters[i]
    return secret_string


def get_clues(guess, secret_string):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret string pair."""
    if guess == secret_string:
        return "You got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_string[i]:
            clues.append("Fermi")
        elif guess[i] in secret_string:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"  # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        clues.sort()
        # Make a single string from the list of string clues.
        return " ".join(clues)


if __name__ == "__main__":
    main()
