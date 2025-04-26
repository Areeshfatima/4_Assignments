# High-Low Game 🎮

import random

def main():
    print("Welcome to the High-Low Game! ✨")
    print("--------------------------------")

    score = 0
    rounds = 5  # Let's play 5 rounds

    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}")

        my_num = random.randint(1, 100)
        comp_num = random.randint(1, 100)

        print(f"Your number is {my_num}")
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        if (guess == "higher" and my_num > comp_num) or (guess == "lower" and my_num < comp_num):
            print(f"You were right! The computer's number was {comp_num}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")

        print(f"Your score is now {score}\n")

    print("Thanks for playing! 🎉")

if __name__ == "__main__":
    main()
