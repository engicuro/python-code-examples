"""Program to accept a string that ends with an alphanumeric character."""

def accept_string_ending_with_alphanumeric():
    """Check if a string ends with an alphanumeric character."""
    test_strings = ["hello1", "world!", "test2", "nope@"]

    for s in test_strings:
        if len(s) > 0 and s[-1].isalnum():
            print(f'"{s}" ends with an alphanumeric character.')
        else:
            print(f'"{s}" does NOT end with an alphanumeric character.')

if __name__ == "__main__":
    accept_string_ending_with_alphanumeric()
