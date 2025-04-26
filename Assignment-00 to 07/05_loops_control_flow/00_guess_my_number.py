# Guess my number

import random

def main():

    # Generate the secret number at random!
    secret_numbers = random.randint(1, 99)

    print("I am thinking of a number between 1 and 99..")

    # Get user guess
    user_guess = int(input("Enter a guess: "))

    # True if guess is not equal to secret number
    while user_guess != secret_numbers:
        if user_guess < secret_numbers:
            print("You guess is too low!")
        else:
            print("You guess is too high!")
        print()  # Print an empty line to tidy up the console for new guesses

        user_guess = int(input("Enter a new guess: "))

    print(f"\033[94m Congratulations! The number was {secret_numbers} \033[0m")

if __name__ == "__main__":
    main()



