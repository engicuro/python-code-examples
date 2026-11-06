"""Program to find the most occurring character and its count in a string.

The most occurring character is the one that appears
the most times in the string.
"""

def find_the_most_occurring_character_and_its_count():
    """Find the most frequently occurring character in a string."""
    test_strings = ["programming", "hello world", "aabbccdd"]

    for s in test_strings:
        # Count how many times each character appears
        counts = {}
        for ch in s:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1

        # Find the character with the largest count
        most_common_char = s[0]
        for ch in counts:
            if counts[ch] > counts[most_common_char]:
                most_common_char = ch

        print(f"String: '{s}' -> Most frequent: '{most_common_char}' (appears {counts[most_common_char]} time(s))")

# Run the function when this file is executed
if __name__ == "__main__":
    find_the_most_occurring_character_and_its_count()
