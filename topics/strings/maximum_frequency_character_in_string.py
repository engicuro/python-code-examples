"""Program to find the character with the maximum frequency in a string."""

def maximum_frequency_character_in_string():
    """Find the most frequently occurring character in a string."""
    test_strings = ["programming", "hello world", "aabbccddee"]

    for s in test_strings:
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        most_common = max(counts.items(), key=lambda x: x[1])
        print(f"String: '{s}' -> Most frequent: '{most_common[0]}' (count: {most_common[1]})")

if __name__ == "__main__":
    maximum_frequency_character_in_string()
