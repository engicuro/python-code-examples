"""Program to print all even numbers in a given range."""

def print_all_even_numbers_in_a_range():
    """Print all even numbers in a specified range."""
    start = 1
    end = 20

    print(f"Even numbers from {start} to {end}:")
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    print(even_numbers)
    return even_numbers

if __name__ == "__main__":
    print_all_even_numbers_in_a_range()
