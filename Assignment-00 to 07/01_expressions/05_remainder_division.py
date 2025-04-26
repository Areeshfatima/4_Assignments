# Find Remainder and division

def main():
    # Prompt user to inter a number
    dividend_num: int = int(input("Please enter an integer to be divided: "))
    divisor_num: int = int(input("Please enter an integer to divide by: "))

    quotient: int = dividend_num // divisor_num
    remainder: int = dividend_num % divisor_num   # Get the Remainder of the division

    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()