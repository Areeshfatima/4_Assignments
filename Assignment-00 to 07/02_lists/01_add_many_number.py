# Add many numbers.

def sum_many_numbers(numbers)-> int:

    # Take a list of numbers and return sum of these numbers

    total_num_far: int = 0
    for number in numbers:
        total_num_far += number

    return total_num_far
    

def main():
    numbers: list[int] = [2, 4, 6, 8, 10]   # Make a list of numbers
    sum_of_numbers: int = sum_many_numbers(numbers)   # find the sum of the list
    print(sum_of_numbers)


if __name__ == "__main__":
    main()


