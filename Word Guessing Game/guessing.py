"""Module that implements a word guessing game"""

from random import choice


dictionary = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']
word = choice(dictionary)
word_set = set(word)
guesses = set()
TRIES = 13


print("Good Luck ! ", input("What is your name? "))
for x in range(1, TRIES):
    # Printing word as list
    print([char if char in guesses else "_" for char in word])

    # Test for victory
    if word_set.issubset(guesses):
        print("\nYou Win\nThe word is:", word)
        break

    # Guessing and recording guesses in set
    guess = input("Guess a character: ")
    guesses.add(guess)
    if guess not in word:
        print("Wrong")

    # Count remaining guesses
    print("You have", + TRIES - x, 'more guesses\n')
else:
    # For-else is triggered if loop never escapes
    print("You Lose")
