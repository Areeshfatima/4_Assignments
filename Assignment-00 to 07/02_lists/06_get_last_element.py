# get last element 

def get_last_element(lst):

    # Takes the length of the list and minuses 1 since they are zero-indexed (we start counting at 0)
    print(lst[len(lst) - 1])
    # print(lst[-1])

def get_lst():

    # Prompts the user to enter one element of the list at a time 
    lst = []
    elemt = input("Please enter an element of the list or press enter to stop. ")

    while elemt != "":
        lst.append(elemt)
        elemt =  input("Please enter an element of the list or press enter to stop. ")

    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == "__main__":
    main()




