# choosing return

ADULT_AGE: int = 18  # U.S age

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False

def main():
    age: str = int(input("\033[1;3m How old is this person?: \033[0m "))
    print(is_adult(age))


if __name__ == "__main__":
    main()