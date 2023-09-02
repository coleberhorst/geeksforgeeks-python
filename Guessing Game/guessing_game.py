"""Module providing a guessing game between two numbers with logarithmically limited guesses."""

from random import randint
from math import log2

# Taking Inputs
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

# generating random number between the lower and upper
secret = randint(lower, upper)
chances = round(log2(upper - lower + 1))
print("\n\tYou've only ", chances, " chances to guess the integer!\n")

# for calculation of minimum number of guesses depends upon range
for x in range(chances):
    guess = int(input("Guess a number:- "))

    if secret > guess:
        print("You guessed too small!")
    elif secret < guess:
        print("You Guessed too high!")
    else:
        print("Congratulations! The number was ", secret)
        break
else:
    print(f"\nThe number is {secret} \n\tBetter Luck Next time!")
