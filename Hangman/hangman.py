"""Hangman

Classic game without visuals.
"""

from random import choice


PHRASES = ["an apple a day keeps the doctor away",
           "better late than never",
           "dont count your chickens before they hatch",
           "dont judge a book by its cover",
           "easy as pie",
           "theres no place like home",
           "you snooze you lose",
           "cool as a cucumber",
           "hold your horses",
           "dont spill the beans",
           "if at first you dont succeed try try again",
           "the early bird catches the worm"]
secret_word = choice(PHRASES)
secret_word_set = set(secret_word)
guesses = set(" ")
TRIES = 20


for x in range(1, TRIES):
    # Printing word as list
    print("".join([character if character in guesses else "_" for character in secret_word]))

    # Testing for victory
    if secret_word_set.issubset(guesses):
        print("\nYou Win")
        break

    # Guessing and recording guesses in set
    guess = input("Guess a character: ")
    guesses.add(guess)
    if guess not in secret_word:
        print("Wrong")

    # Count remaining guesses
    print("You have", 1 + TRIES - x, 'more guesses\n')
else:
    # For-else is triggered if loop never escapes
    print("You Lose")
