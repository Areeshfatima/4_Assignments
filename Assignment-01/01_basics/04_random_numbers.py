#  random numbers

import random

N_NUM: int = 10
MIN_NUM: int = 1
MAX_NUM: int = 100

def main():
    for _ in range(10):
        print(random.randint(MIN_NUM, MAX_NUM),end= " ")

if __name__ == "__main__":
    main()