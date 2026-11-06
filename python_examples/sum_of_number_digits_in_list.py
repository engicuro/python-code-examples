"""Program to find the sum of digits of each number in a list."""

def sum_of_number_digits_in_list():
    """Calculate the sum of digits for each number in a list."""
    arr = [123, 456, 789, 101]

    digit_sums = [sum(int(d) for d in str(num)) for num in arr]

    print(f"Original list: {arr}")
    print(f"Sum of digits for each number: {digit_sums}")
    return digit_sums

if __name__ == "__main__":
    sum_of_number_digits_in_list()
