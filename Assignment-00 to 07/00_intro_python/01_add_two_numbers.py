# add_two_numbers

def main():
    print("This Program adds two numbers!")

    # Prompt the user to enter the first number
    num1: str = input("Enter the first number:")
    num1: int = int(num1)

    # Prompt the user to enter the second number
    num2: str = input("Enter the second number:")
    num2: int = int(num2)

    # Calculate the sum
    sum: int = num1 + num2

    # Print the total sum
    print(f"The sum of the given numbers is: {sum}.")


# Call the main function
if __name__ == "__main__":
    main()



