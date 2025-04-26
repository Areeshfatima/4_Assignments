# Simullate rolling of two dice

#  import the random library
import random

NUM_SIDES: int = 6

def main():
    # Setting a seed is useful for debugging.
    random.seed(1)

    # Roll die
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)

    # SUm of Both dice
    total: int = die1 + die2

    # Print out the results
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die rolled: {die1}.")
    print(f"Second die rolled: {die2}.")
    print(f"Total of both the dice is: {total}")

if __name__ == "__main__":
    main()
    

