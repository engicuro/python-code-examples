"""Program to check if a string is a binary string."""

def check_if_a_given_string_is_binary_string_or_not():
    """Check if a string contains only 0s and 1s."""
    test_strings = ["101010", "102010", "1111", "0000", "abc101"]

    for s in test_strings:
        if set(s) <= {'0', '1'} and len(s) > 0:
            print(f'"{s}" is a binary string.')
        else:
            print(f'"{s}" is NOT a binary string.')

if __name__ == "__main__":
    check_if_a_given_string_is_binary_string_or_not()
