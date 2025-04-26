# Fibonacci sequence up to a maximun value.

MAX_TERM_VALUE: int = 10000

def main():
    cur_term: int = 0   # The 0th fibonacci number
    next_term: int = 1  # The 1st fibonacci number

    while cur_term < MAX_TERM_VALUE:
        print(cur_term)
        term_after_next = cur_term + next_term
        cur_term = next_term
        next_term = term_after_next

if __name__ == "__main__":
    main()