# Phiriya Trakoolwang 633040223-5
"""
Write a Python program to implement a number guessing game
Generate a random integer in the range [1, 10] and then
assign it as an answer.
Then keep asking a number for a user to guess.
If the guess number is the same as the number, the program quits.
If the guess number is lower than the answer, display a message
for the user to try a higher number.  Increment the number of guesses
If the guess number is higher than the answer, display a message
for the user to try a lower number. Increment the number of guesses
Each user can guess at most 5 times.
The maximum number of guesses and the min and the max integer of
the randomly generated number should be in constant variables
"""

import random


def guess_number():
    MIN_NUM = 1
    MAX_NUM = 10
    n = random.randint(MIN_NUM, MAX_NUM)
    guess_num = int(input("Enter an integer to guess: "))
    x = 0
    limit_to_guess = 4

    while guess_num != n and limit_to_guess >= 0:

        if guess_num < n:
            print("Try a higher number.")
            print("You have", limit_to_guess, "guesses remaining")
            guess_num = int(input("Enter an integer to guess: "))
            x += 1
            limit_to_guess -= 1
            if limit_to_guess == 0:
                print("You have 0 guesses remaining")
                break


        elif guess_num > n:
            print("Try a lower number.")
            print("You have", limit_to_guess, "guesses remaining")
            guess_num = int(input("Enter an integer to guess: "))
            x += 1
            limit_to_guess -= 1
            if limit_to_guess == 0:
                print("You have 0 guesses remaining")
                break

    if guess_num == n:
        print("Congrats that you guess the number correctly")


if __name__ == "__main__":
    guess_number()
