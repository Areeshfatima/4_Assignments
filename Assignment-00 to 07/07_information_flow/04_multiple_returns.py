# user info with multiple returns

def user_info():
    first_name: str = input("What is your name? ")
    last_name: str = input("What is you last name? ")
    email_address: str = input("What is your email address? ")

    return first_name, last_name, email_address

def main():
    user_data = user_info()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()