"""Program to print all negative numbers in a list."""

def print_negative_numbers_in_a_list():
    """Print all negative numbers from a list."""
    arr = [12, -3, 5, -7, 19, -1, 8, -15, 4]

    negative_numbers = [num for num in arr if num < 0]

    print(f"List: {arr}")
    print(f"Negative numbers: {negative_numbers}")
    return negative_numbers

if __name__ == "__main__":
    print_negative_numbers_in_a_list()
