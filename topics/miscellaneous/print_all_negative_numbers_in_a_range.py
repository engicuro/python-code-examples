"""Program to print all negative numbers in a given range."""

def print_all_negative_numbers_in_a_range():
    """Print all negative numbers in a specified range."""
    start = -20
    end = -1

    print(f"Negative numbers from {start} to {end}:")
    negative_numbers = [num for num in range(start, end + 1) if num < 0]
    print(negative_numbers)
    return negative_numbers

if __name__ == "__main__":
    print_all_negative_numbers_in_a_range()
