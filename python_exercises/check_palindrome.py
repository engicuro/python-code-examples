"""Check Palindrome - Exercise."""

def check_palindrome():
    """Check if a string is a palindrome."""
    test_strings = ["racecar", "hello", "madam", "python", "level", "A man a plan a canal Panama"]

    for s in test_strings:
        cleaned = s.lower().replace(" ", "")
        is_palindrome = cleaned == cleaned[::-1]
        print(f'"{s}" -> Palindrome: {is_palindrome}')

if __name__ == "__main__":
    check_palindrome()
