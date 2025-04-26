# get list from user

def main():
    
    lst = []   # Make an empty list to store things in

    val = input("Enter a value: ")        # Get an initial value

    while val:     # While the user input isn't an empty value
        lst.append(val)  # add val to the list
        val = input("Enter a value: ")        

    print("Here's the list:", lst)

if __name__ == "__main__":
    main()