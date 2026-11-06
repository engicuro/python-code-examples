"""Program to check whether a string is a palindrome or not."""

def check_if_a_string_is_palindrome_or_not():
    """Check if a string is a palindrome."""
    test_strings = ["racecar", "hello", "madam", "python", "level"]

    for s in test_strings:
        cleaned = s.lower()
        if cleaned == cleaned[::-1]:
            print(f'"{s}" is a palindrome.')
        else:
            print(f'"{s}" is NOT a palindrome.')

if __name__ == "__main__":
    check_if_a_string_is_palindrome_or_not()
