# double user number until the value became 100 or greater

def main():
    get_user_val = int(input("Enter a number: "))

    while get_user_val < 100:
        get_user_val *= 2
        print(get_user_val, end=" ")

if __name__ == "__main__":
    main()
    