"""Program to check if the binary representation of a number is a palindrome."""

def check_if_binary_representation_is_palindrome():
    """Check if the binary representation of a number is a palindrome."""
    test_nums = [5, 7, 9, 10, 15, 21]

    for num in test_nums:
        binary = bin(num)[2:]
        is_palindrome = binary == binary[::-1]
        print(f"Number: {num}, Binary: {binary}, Is palindrome: {is_palindrome}")

if __name__ == "__main__":
    check_if_binary_representation_is_palindrome()
