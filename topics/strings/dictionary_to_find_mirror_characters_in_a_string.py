"""Program to find mirror characters in a string using a dictionary."""

def dictionary_to_find_mirror_characters_in_a_string():
    """Find characters that appear at mirror positions in a string."""
    test_strings = ["abcba", "racecar", "hello", "abccba"]

    for s in test_strings:
        mirror_chars = {}
        n = len(s)
        for i in range(n // 2):
            if s[i] == s[n - 1 - i]:
                mirror_chars[i] = s[i]

        print(f"String: '{s}' -> Mirror character pairs: {mirror_chars}")

if __name__ == "__main__":
    dictionary_to_find_mirror_characters_in_a_string()
