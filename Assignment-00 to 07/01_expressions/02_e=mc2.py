# Mass-Energy Equivalence

C: int = 299792458   # The speed of light in m/s

def main():
    mass_into_kg: float = float(input("\033[1;3m Enter kilos of mass: \033[0m "))

    # Calculating Energy
    # e = m * (C ** 2)
    # Using ** operator to raise C to the power of 2
    energy_in_joules: float = mass_into_kg * (C ** 2)

    # Display work to user
    print("e = m * C ^ 2..")
    print(f"m = {mass_into_kg} kg")
    print(f"C = {C} m/s")

    print(f"{energy_in_joules} joules of energy!")

if __name__ == "__main__":
    main()
