"""Program to check if a string starts and ends with the same character."""

def check_whether_a_string_starts_and_ends_with_the_same_character_or_not():
    """Check if a string starts and ends with the same character."""
    test_strings = ["radar", "hello", "level", "world", "a", "abba"]

    for s in test_strings:
        if len(s) > 0 and s[0] == s[-1]:
            print(f'"{s}" starts and ends with the same character.')
        else:
            print(f'"{s}" does NOT start and end with the same character.')

if __name__ == "__main__":
    check_whether_a_string_starts_and_ends_with_the_same_character_or_not()
