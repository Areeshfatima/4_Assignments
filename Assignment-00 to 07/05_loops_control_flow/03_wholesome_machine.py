# wholesome machine

AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation:" + AFFIRMATION)

    user_feedback = input("\033[94m I am capable of doing anything I put my mind to.")  # Get user input

    while user_feedback != AFFIRMATION:
        print("That was not the correct affirmation!")

        # Ask the user to type the affirmation again!
        print("Please type the following affirmation:" + AFFIRMATION)
        user_feedback = input()
    
    print("That's correct!")

if __name__ == "__main__":
    main()
