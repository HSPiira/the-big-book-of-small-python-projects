In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. The game offers one of the following hints in response to your guess: “Pico” when your guess has a correct digit in the wrong place, “Fermi” when your guess has a correct digit in the correct place, and “Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number.

# The Program in Action

When you run bagels.py, the output will look like this:

---

```
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.comI am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:`  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.
Guess #1:123
Pico
Guess #2:
456
Bagels
Guess #3:
178
Pico Pico
--snip--
Guess #7:
791
Fermi Fermi
Guess #8:
701
You got it!
Do you want to play again? (yes or no)
no
Thanks for playing!
```

---

# How It Works

Keep in mind that this program uses not integer values but rather string values that contain numeric digits. For example, '426' is a different value than 426. We need to do this because we are performing string comparisons with the secret number, not math operations. Remember that '0' can be a leading digit: the string '026' is different from '26', but the integer 026 is the same as 26.
