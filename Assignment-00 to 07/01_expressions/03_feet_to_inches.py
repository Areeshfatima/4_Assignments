# Convert feet to inches

INCHES_IN_FOOT: int = 12   #There are 12 inches in 1 foot

def main():
    feet: float = float(input("Enter number of feet: "))
    inches: float = feet * INCHES_IN_FOOT   #Perform Conversion
    print(f"That is {inches} inches!")

if __name__ == "__main__":
    main()

