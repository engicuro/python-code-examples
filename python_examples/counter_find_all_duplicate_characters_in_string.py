"""Program to find all duplicate characters in a string.

A duplicate character is one that appears more than once.
We count each character's occurrences and report
only those that appear 2 or more times.
"""

def counter_find_all_duplicate_characters_in_string():
    """Find all duplicate characters in a string."""
    test_strings = ["programming", "hello", "aabbccdd", "python"]

    for s in test_strings:
        # Count how many times each character appears
        counts = {}
        for ch in s:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1

        # Keep only characters that appear more than once
        duplicates = {}
        for char, count in counts.items():
            if count > 1:
                duplicates[char] = count

        print(f"String: '{s}' -> Duplicate characters: {duplicates}")

# Run the function when this file is executed
if __name__ == "__main__":
    counter_find_all_duplicate_characters_in_string()
