#  create list

def main():
    fruits_lst: list[str] = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(len(fruits_lst))
    fruits_lst.append("mango")
    print(len(fruits_lst))

    for fruit in fruits_lst:
        print(fruit)


if __name__ == "__main__":
    main()



# Initialize the list
my_list = [10, "learning", 66, "python", 99]

# Accessing Elements
def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Error: Index out of range."

# Modifying Elements
def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Error: Index out of range."

# Slicing the List
def slice_list(lst, start, end):
    # Adjusting start and end if they are out of range
    start = max(0, start)
    end = min(len(lst), end)
    if start > end:
        return "Error: Start index must be less than end index."
    return lst[start:end]

# Game Interaction
def list_game():
    print("Welcome to the List Game!")
    print(f"Here is your starting list: {my_list}\n")

    while True:
        print("\n Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit the game")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                idx = int(input("Enter the index you want to access: "))
                print("Result:", access_element(my_list, idx))
            except ValueError:
                print("Please enter a valid integer index.")

        elif choice == '2':
            try:
                idx = int(input("Enter the index you want to modify: "))
                new_val = input("Enter the new value: ")
                result = modify_element(my_list, idx, new_val)
                if isinstance(result, list):
                    print("List updated:", result)
                else:
                    print(result)
            except ValueError:
                print("Please enter a valid integer index.")

        elif choice == '3':
            try:
                start_idx = int(input("Enter the start index: "))
                end_idx = int(input("Enter the end index: "))
                print("Sliced List:", slice_list(my_list, start_idx, end_idx))
            except ValueError:
                print("Please enter valid integer indices.")

        elif choice == '4':
            print("Thank you for playing! Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Main function
def main():
    list_game()

# Call the main function
if __name__ == "__main__":
    main()
