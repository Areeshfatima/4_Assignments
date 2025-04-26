#  in range

def in_range(n, low, high):

    # Returns True if n is between low and high, inclusive. 
    # high is guaranteed to be greater than low.

    if n >= low and n <= high:
        return True
    
    return False

def main():
    print(in_range(4, 6, 2))  # False
    print(in_range(6, 9, 3))  # False
    print(in_range(6, 2, 9))  # True

if __name__ == "__main__":
    main()