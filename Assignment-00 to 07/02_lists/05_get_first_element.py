# get first element

def get_first_element(lst):

    # Print first element to a provided list
    print(lst[0])

def get_lst():

    # Prompts the user to enter one element of the list at a time 
    lst = []
    elemt: str = input("Please enter an element of the list or press enter to stop. ")
    
    while elemt != "":
        lst.append(elemt)
        elemt = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == "__main__":
    main()
