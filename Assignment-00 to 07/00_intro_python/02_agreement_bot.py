# Agreement bot

def main():
    # Ask user about their favourite animal!

    fav_animal: str = input("\033[1;3m What's your favourite animal? \033[0m ")
    print(f"My favourite animal is also {fav_animal}!")


if __name__ == "__main__":
    main()