# Calculate the perimeter of Triangle

def main():
    # Prompt the user for enter length of side 1.
    tri_side1: float = float(input("\033[1;3m What is the length of side1? \033[0m "))

    # Prompt the user for enter length of side 2.
    tri_side2: float = float(input("\033[1;3m What is the length of side2? \033[0m "))

    # Prompt the user for enter 1st side of length of triangle.
    tri_side3: float = float(input("\033[1;3m What is the length of side3? \033[0m "))

    # Print out the perimeter(sum of 3 sides)  of Triangle.
    sum_of_sides = tri_side1 + tri_side2 + tri_side3
    print(f"The Perimeter of the Triangle is: {sum_of_sides}")


if __name__ == "__main__":
    main()

