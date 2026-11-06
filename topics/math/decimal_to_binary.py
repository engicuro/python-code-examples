"""Decimal to Binary - Exercise.

This file shows two ways to convert a decimal (base-10) number
into binary (base-2).
"""

def decimal_to_binary():
    """Convert a decimal number to binary."""
    test_nums = [10, 255, 7, 100]

    for num in test_nums:
        # Method 1: Using Python's built-in bin() function
        # bin(10) gives '0b1010', so we slice off the first two characters
        binary1 = bin(num)[2:]

        # Method 2: Manual conversion (step by step)
        # How it works: keep dividing by 2 and collect the remainders.
        # Example for 10:
        #   10 / 2 = 5 remainder 0
        #    5 / 2 = 2 remainder 1
        #    2 / 2 = 1 remainder 0
        #    1 / 2 = 0 remainder 1
        # Read remainders bottom-to-top: 1010
        if num == 0:
            binary2 = "0"
        else:
            binary2 = ""
            n = num
            while n > 0:
                remainder = n % 2  # Get the remainder (0 or 1)
                binary2 = str(remainder) + binary2  # Put it at the front
                n = n // 2  # Divide by 2 (whole number division)

        print(f"Decimal: {num} -> Binary (bin()): {binary1}, Binary (manual): {binary2}")

if __name__ == "__main__":
    decimal_to_binary()
