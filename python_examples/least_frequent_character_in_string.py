"""Program to find the least frequent character in a string.

The least frequent character is the one that appears
the fewest times in the string.
"""

def least_frequent_character_in_string():
    """Find the least frequent character in a string."""
    test_strings = ["programming", "hello", "aabbcc"]

    for s in test_strings:
        # Count how many times each character appears
        counts = {}
        for ch in s:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1

        # Find the character with the smallest count
        least_freq_char = s[0]
        for ch in counts:
            if counts[ch] < counts[least_freq_char]:
                least_freq_char = ch

        print(f"String: '{s}' -> Least frequent: '{least_freq_char}' (appears {counts[least_freq_char]} time(s))")

# Run the function when this file is executed
if __name__ == "__main__":
    least_frequent_character_in_string()
