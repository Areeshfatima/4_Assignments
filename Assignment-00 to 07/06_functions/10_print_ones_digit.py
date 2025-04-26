# print one digit

def print_one_digit(num):
    num = int(num)
    print("The ones digit is", num % 10)


def main():
    num = input("\033[94m Enter a number: \033[0m ")
    print_one_digit(num)

if __name__ == "__main__":
    main()
