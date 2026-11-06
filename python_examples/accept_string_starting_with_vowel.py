"""Program to accept a string that starts with a vowel."""

def accept_string_starting_with_vowel():
    """Check if a string starts with a vowel."""
    test_strings = ["apple", "orange", "banana", "umbrella", "grape"]
    vowels = set('aeiouAEIOU')

    for s in test_strings:
        if len(s) > 0 and s[0] in vowels:
            print(f'"{s}" starts with a vowel.')
        else:
            print(f'"{s}" does NOT start with a vowel.')

if __name__ == "__main__":
    accept_string_starting_with_vowel()
