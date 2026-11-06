"""Program to print all positive numbers in a list."""

def print_positive_numbers_in_a_list():
    """Print all positive numbers from a list."""
    arr = [12, -3, 5, -7, 19, -1, 8, -15, 4]

    positive_numbers = [num for num in arr if num > 0]

    print(f"List: {arr}")
    print(f"Positive numbers: {positive_numbers}")
    return positive_numbers

if __name__ == "__main__":
    print_positive_numbers_in_a_list()
