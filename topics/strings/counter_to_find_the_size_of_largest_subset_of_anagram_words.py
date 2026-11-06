"""Program to find the size of the largest group of anagram words.

Anagrams are words made from the same letters
but in a different order. For example, 'listen',
'silent', and 'enlist' are all anagrams.

We group words by their sorted letters to find
which words are anagrams of each other.
"""

def counter_to_find_the_size_of_largest_subset_of_anagram_words():
    """Find the largest group of anagram words."""
    words = ["listen", "silent", "enlist", "google", "gogole", "abc", "bca", "cab", "xyz"]

    # Group words by their sorted letters
    # Anagrams will have the same sorted letters
    anagram_groups = {}
    for word in words:
        # Sort the letters to create a key
        # e.g., 'listen' -> ('e', 'i', 'l', 'n', 's', 't')
        key = tuple(sorted(word))

        # Add this word to the group with the same key
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(word)

    # Print all anagram groups
    print("Anagram groups:")
    for key, group in anagram_groups.items():
        print(f"  {group}")

    # Find the largest group
    largest_group = []
    for group in anagram_groups.values():
        if len(group) > len(largest_group):
            largest_group = group

    print(f"\nLargest anagram group has {len(largest_group)} words: {largest_group}")
    return len(largest_group)

# Run the function when this file is executed
if __name__ == "__main__":
    counter_to_find_the_size_of_largest_subset_of_anagram_words()
