# Double each element in list

def main():
    numbers: list[int] = [1, 3, 5, 7, 9]    # create a list of numbers

    for i in range(len(numbers)):           # Loop through the indices of the list
        element_at_index: int = numbers[i]  # Get the element at index i in the numbers list
        numbers[i] = element_at_index * 2   # Set the element at index i to be equal to the previous element times 2
    
    print(numbers)


if __name__ == "__main__":
    main()


