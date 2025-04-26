# Giving user total fruits cost according to their fruits

def main():
    fruits = {"apples": 1.5, "kiwi": 1, "jackfruit": 80, "rambutan": 1.5, "mango": 5}

    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input(f"\033[1;3m How many {fruit_name} do you want to buy?: \033[0m "))
        total_cost += (price * amount_bought)

    print(f"Your total is $ {total_cost}")

if __name__ == "__main__":
    main()