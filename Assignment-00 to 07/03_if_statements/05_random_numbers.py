# Random numbers in the range 1 to 100.

import random

N_NUM: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    generated_num: int = [random.randint(1, 100) for _ in range(10)]
    print("Generated random numbers:", *generated_num)
    
if __name__ == "__main__":
    main()

