"""Program to count different character types in a string."""

def count_character_types():
    """Count uppercase, lowercase, digits, and special characters in a string."""
    test_string = "Hello World! 123 @#%"

    uppercase = sum(1 for ch in test_string if ch.isupper())
    lowercase = sum(1 for ch in test_string if ch.islower())
    digits = sum(1 for ch in test_string if ch.isdigit())
    special = sum(1 for ch in test_string if not ch.isalnum() and not ch.isspace())

    print(f"String: '{test_string}'")
    print(f"Uppercase letters: {uppercase}")
    print(f"Lowercase letters: {lowercase}")
    print(f"Digits: {digits}")
    print(f"Special characters: {special}")

    return uppercase, lowercase, digits, special

if __name__ == "__main__":
    count_character_types()
