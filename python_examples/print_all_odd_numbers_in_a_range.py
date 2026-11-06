"""Program to print all odd numbers in a given range."""

def print_all_odd_numbers_in_a_range():
    """Print all odd numbers in a specified range."""
    start = 1
    end = 20

    print(f"Odd numbers from {start} to {end}:")
    odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]
    print(odd_numbers)
    return odd_numbers

if __name__ == "__main__":
    print_all_odd_numbers_in_a_range()
