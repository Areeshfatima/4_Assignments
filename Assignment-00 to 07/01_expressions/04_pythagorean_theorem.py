# Pythagorean Theorem of triangle

# import math library so we can use the sqrt function
import math

def main():
    # Get the two sides length from the user and cast them to be numbers.
    ab: float = float(input("\033[1;3m Enter the length of AB: \033[0m "))
    ac: float = float(input("\033[1;3m Enter the length of AC: \033[0m "))

    # Calculate the hypotenuse using the two sides
    bc: float = math.sqrt(ab ** 2 + ac ** 2)
    print(f"The length of BC (the hypotenuse) is: {bc:.2f}")

if __name__ == "__main__":
    main()
