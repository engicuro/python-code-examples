"""Program to replace duplicate occurrences in a string."""

def replace_duplicate_occurrence_in_string():
    """Replace duplicate consecutive occurrences of a character in a string."""
    test_strings = ["aaabbbccc", "hellooo", "mississippi", "aabbcc"]

    for s in test_strings:
        result = s[0] if s else ''
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                result += s[i]
        print(f"Original: '{s}' -> After replacing duplicates: '{result}'")

if __name__ == "__main__":
    replace_duplicate_occurrence_in_string()
