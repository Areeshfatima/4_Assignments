# Tell user tall enough or not enough to ride.

MAXIMUN_HEIGHT: int = 50

def main():
    # ask user how tall are you.
    height: float = float(input("\033[1;3m How tall are you? \033[0m "))
    if height >= MAXIMUN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()




