# mars weight

def main():
    # Gravity factors relative to Earth
    gravity_factors = {
        "mercury": 0.38,
        "venus": 0.91,
        "mars": 0.378,
        "jupiter": 2.36,
        "saturn": 0.92,
        "uranus": 0.89,
        "neptune": 1.13,
        "pluto": 0.07
    }

    # Ask user for weight and planet
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ").lower()

    # Calculate and print the equivalent weight
    if planet in gravity_factors:
        equivalent_weight = earth_weight * gravity_factors[planet]
        equivalent_weight = round(equivalent_weight, 2)
        print(f"\nThe equivalent weight on {planet.capitalize()}: {equivalent_weight}")
    else:
        print("\nSorry, unknown planet!")

if __name__ == "__main__":
    main()
