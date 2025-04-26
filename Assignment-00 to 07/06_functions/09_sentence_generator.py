# Sentence generator accordinng to user input

def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        # noun
        print("I am excited to add this " + word + " to my vast collection of them!")

    elif part_of_speech == 1:
        # verb
        print("It's so nice outside today it makes me want to " + word + "!")

    elif part_of_speech == 2:
        # adjective
        print("Looking out my window, the sky is big and " + word + "!")

    else:
        # part_of_speech is invalid (not 0, 1, or 2)
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    word: str = input("\033[94m Please type a noun, verb, or adjective: \033[0m ")
    print("Is this a noun, verb, or adjective? ")
    part_of_speech = int(input("\033[94m Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

if __name__ == "__main__":
    main()







