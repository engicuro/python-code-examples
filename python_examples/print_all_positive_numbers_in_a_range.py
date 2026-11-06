"""Program to print all positive numbers in a given range."""

def print_all_positive_numbers_in_a_range():
    """Print all positive numbers in a specified range."""
    start = -10
    end = 10

    print(f"Positive numbers from {start} to {end}:")
    positive_numbers = [num for num in range(start, end + 1) if num > 0]
    print(positive_numbers)
    return positive_numbers

if __name__ == "__main__":
    print_all_positive_numbers_in_a_range()
