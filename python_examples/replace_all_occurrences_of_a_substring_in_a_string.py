"""Program to replace all occurrences of a substring in a string."""

def replace_all_occurrences_of_a_substring_in_a_string():
    """Replace all occurrences of a substring with another string."""
    original = "Hello world, world is beautiful, world!"
    old = "world"
    new = "Earth"

    result1 = original.replace(old, new)

    print(f"Original: '{original}'")
    print(f"After replacing '{old}' with '{new}': '{result1}'")
    return result1

if __name__ == "__main__":
    replace_all_occurrences_of_a_substring_in_a_string()
