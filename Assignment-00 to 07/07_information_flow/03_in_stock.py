# fruits in stock

def num_in_stock(fruit: str):

    # This function returns the number of fruit Sophia has in stock.
    if fruit == "apples":
        return 2
    if fruit == "durain":
        return 4
    if fruit == "pears":
        return 100
    if fruit == "mangoes":
        return 50
    else:
        return 0  # This fruit is not in stock
    
def main():
    fruit: str = input("Enter a fruit: ")
    stock = num_in_stock(fruit)

    if stock == 0:
        print("This fruit is not in stock!")

    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

if __name__ == "__main__":
    main()

