# Dice simulator

# import random which simulate random things like dice.
import random

# Number of the sides on  dice roll.
num_sides = 6

def roll_dice():
    # Simulate rolli g two sides and print their total
    die1: int = random.randint(1, num_sides)
    die2: int = random.randint(1, num_sides)
    rolled: int = die1 + die2
    print("Total of two dice is:", rolled)

def main():
    die1: int = 10
    print(f"die1 in main() starts as: {die1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die1 in main() is still: {die1}")


if __name__ == "__main__":
    main()

