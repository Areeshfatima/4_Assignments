# international votinng age.

PETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48

def main():


    # Get the user age
    while True:
        user_input = input("\033[94m Tell how old are you or press enter to stop! \033[0m ")

        if user_input == "":
            print("Goodbye!")
            break

        if user_input.isdigit(): 
            user_age = int(user_input)

            # Check if the user can vote in Peturksbouipo
            if user_age >= PETURKSBOUIPO_AGE:
                print("You can vote in Peturksbouipo where the voting age is", str(PETURKSBOUIPO_AGE) + ".")
            else:
                print("You can not vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")

    
            # Check if the user can vote in Stanlau
            if user_age >= STANLAU_AGE:
                print("You can vote in Stanlau where the voting age is", str(STANLAU_AGE) + ".")
            else:
                print("You can not vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")


            # Check if the user can vote in mayengua
            if user_age >= MAYENGUA_AGE:
                print("You can vote in Mayengua where the voting age is", str(MAYENGUA_AGE) + ".")
            else:
                print("You can not vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
        else:
            print("Enter a valid whole number.")
    

if __name__ == "__main__":
    main()


    

    




