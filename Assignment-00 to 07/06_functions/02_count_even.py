#  count even numbers

def count_even(lst):

    # Returns number of even numbers in list.

    count = 0    # Stores the count of even numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 == 0:    # If the current number in the list is even (divisible by 2)
            count += 1      # Add one to our count!
    
    print(count)

def get_list_of_int():

    lst = []  # Make an empty list to store integers
    user_input = input("Enter an integer or press enter to stop: ")

    while user_input != "":     # While the user doesn't enter nothing...
        lst.append(int(user_input))     # Cast the user input into an integer and add it to our list
        user_input = input("Enter an integer or press enter to stop: ")

    return lst

def main():
    lst = get_list_of_int()
    count_even(lst)


if __name__ == "__main__":
    main()
