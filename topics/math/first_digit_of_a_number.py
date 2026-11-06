"""First Digit of a Number - Exercise."""

def first_digit_of_a_number():
    """Find the first digit of a given number."""
    test_nums = [12345, 987, 5, 1000, 42]

    for num in test_nums:
        # Method 1: Convert to string
        first_digit_str = int(str(abs(num))[0])

        # Method 2: Using division
        n = abs(num)
        while n >= 10:
            n //= 10
        first_digit_math = n

        print(f"Number: {num}, First digit (string): {first_digit_str}, First digit (math): {first_digit_math}")

if __name__ == "__main__":
    first_digit_of_a_number()
