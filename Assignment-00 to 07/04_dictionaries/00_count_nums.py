#  count numbers

def get_user_numbers():

    #  create a empty list
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")

        # If the user enters a blank line, break out of the loop and stop asking for input.
        if user_input == "":
            break

        # convert the user input to an integer and add it to the list
        num = int(user_input)
        user_numbers.append(num)
    
    return user_numbers

def count_nums(num_lst):

    # Create an empty dictionary.
    # Loop over the list of numbers. 
    # If the number is not in the dictionary, add it as a key with a value of 1.
    # If the number is in the dictionary, increment its value by 1.

    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    return num_dict

def print_counts(num_dict):

    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")

def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == "__main__":
    main()