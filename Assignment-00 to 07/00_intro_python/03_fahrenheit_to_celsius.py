# Fahrenheit to Celsius

def main():
    # Prompt user enter the temperature in fahrenheit
    temperature_fahrenheit: float = float(input("\033[1;3m Enter the temperature in Fahrenheit: \033[0m "))


    # Convert to Celsius using the given formula
    temperature_celsius: float = (temperature_fahrenheit - 32) * 5.0/9.0

    # Print the result
    print(f"Temperature: {temperature_fahrenheit}F = {temperature_celsius:.2f}C")

if __name__ == "__main__":
    main()
