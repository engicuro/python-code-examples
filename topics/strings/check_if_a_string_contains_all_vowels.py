"""Program to check if a string contains all vowels."""

def check_if_a_string_contains_all_vowels():
    """Check if a string contains all five vowels (a, e, i, o, u)."""
    test_strings = [
        "educational",
        "hello world",
        "sequoia",
        "programming",
    ]
    vowels = set('aeiou')

    for s in test_strings:
        found = set(s.lower()) & vowels
        has_all = found == vowels
        print(f'"{s}" contains all vowels: {has_all} (found: {found})')

if __name__ == "__main__":
    check_if_a_string_contains_all_vowels()
