# for number genaration
import random

# number guessing game
def number_guessing_game():

    #secret number initialize
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:

        guess = int(input("Guess the number (1, 100) : "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            print(f"Congratulations!, You guess the number in {attempts} attempts.")
            break

number_guessing_game()