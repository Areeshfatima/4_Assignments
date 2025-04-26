# Enter message of number of times which user give

def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message)

def main():
    message = input("\033[94m Please type a message:\033[0m ")
    repeats = int(input("\033[94m Enter a numbers of times to repeat your message \033[0m"))

    print_multiple(message, repeats)

if __name__ == "__main__":
    main()