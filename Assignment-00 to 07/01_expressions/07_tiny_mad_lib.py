# Tiny Mad Lib

SENTENCE_START: str = "Learning Python is fun! I learned alot of new things for making "  # noun, verb, adjective 

def main():
    # Get three input from users to make the adlib
    adjective: str = input("Please type an adjective and press enter: ")
    noun: str = input("Please type a noun and press enter: ")
    verb: str = input("Please type a verb and press enter: ")

    # Join all inputs together 
    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")

if __name__ == "__main__":
    main()