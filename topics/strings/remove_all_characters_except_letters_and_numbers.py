"""Program to remove all characters except letters and numbers from a string."""

def remove_all_characters_except_letters_and_numbers():
    """Remove all special characters from a string, keeping only letters and digits."""
    test_strings = [
        "Hello@World!123",
        "Python#3.9$is&great*",
        "user@example.com",
    ]

    for s in test_strings:
        cleaned = ''.join(ch for ch in s if ch.isalnum())
        print(f"Original: '{s}' -> Cleaned: '{cleaned}'")

if __name__ == "__main__":
    remove_all_characters_except_letters_and_numbers()
