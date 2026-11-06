"""Program to check if a string contains only defined characters."""

def check_if_string_contain_only_defined_characters():
    """Check if a string contains only alphabetic characters."""
    test_strings = ["hello", "hello123", "world!", "Python", "abc_def"]

    for s in test_strings:
        if s.isalpha():
            print(f'"{s}" contains only alphabetic characters.')
        else:
            print(f'"{s}" contains characters other than alphabets.')

if __name__ == "__main__":
    check_if_string_contain_only_defined_characters()
