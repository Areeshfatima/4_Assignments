# guess my number

import random

def main():

    secret_num: int = random.randint(1, 99)

    print("I am thinking of a number between 0 and 99...")

    # Get user input
    guess_num: int = int(input("Enter a guess: "))

    while guess_num != secret_num:
        if guess_num < secret_num:
            print("Your guess is too low!")
        else:
            print("Your guess is too high!")

        print()
        guess_num: int = int(input("Enter a new guess"))

    print(f"Congratulations! The number was {secret_num}")

if __name__ == "__main__":
    main()
