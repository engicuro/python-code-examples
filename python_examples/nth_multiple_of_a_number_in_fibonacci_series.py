"""Program to find the Nth multiple of a number in the Fibonacci series."""

def nth_multiple_of_a_number_in_fibonacci_series():
    """Find the Nth multiple of a given number in the Fibonacci series."""
    num = 3
    n = 4

    def find_nth_multiple(num, n):
        count = 0
        a, b = 0, 1
        position = 0
        while count < n:
            if a % num == 0 and a != 0:
                count += 1
                if count == n:
                    return a, position
            a, b = b, a + b
            position += 1
        return None, position

    result, pos = find_nth_multiple(num, n)
    print(f"Number: {num}, Nth multiple: {n}")
    print(f"The {n}th multiple of {num} in Fibonacci is: {result} (at position {pos})")
    return result

if __name__ == "__main__":
    nth_multiple_of_a_number_in_fibonacci_series()
