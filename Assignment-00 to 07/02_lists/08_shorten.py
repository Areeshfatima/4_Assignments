# shorten

MAX_LENGTH = 3

def shorten(lst):

    while len(lst) > MAX_LENGTH:
        last_elemt = lst.pop()
        print(last_elemt)

def get_lst():

    # Prompts the user to enter one element of the list at a time.
    lst = []
    elemt = input("Please enter an element of the list or press enter to stop.")

    while elemt != "":
        lst.append(elemt)
        elemt = input("Please enter an element of the list or press enter to stop.")
    return lst

def main():
    lst = get_lst()
    shorten(lst)
    print("Final list:", lst)  # <-- 👈 Shows th


if __name__ == "__main__":
    main()






