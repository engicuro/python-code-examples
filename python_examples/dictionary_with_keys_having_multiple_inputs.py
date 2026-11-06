"""Program to create a dictionary where keys can have multiple values.

Normally, each dictionary key has one value.
But sometimes we want one key to be associated
with multiple values. We do this by storing
a list as the value for each key.

Example: ('a', 1) and ('a', 3) both have key 'a',
so 'a' maps to the list [1, 3].
"""

def dictionary_with_keys_having_multiple_inputs():
    """Create a dictionary where each key can have multiple values."""
    # Each pair is (key, value)
    pairs = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]

    # Build a dictionary where each key maps to a list of values
    multi_dict = {}
    for key, value in pairs:
        # If we haven't seen this key before, create an empty list for it
        if key not in multi_dict:
            multi_dict[key] = []
        # Add this value to the list for this key
        multi_dict[key].append(value)

    print("Dictionary with multiple values per key:")
    for key, values in multi_dict.items():
        print(f"  {key}: {values}")

    return multi_dict

# Run the function when this file is executed
if __name__ == "__main__":
    dictionary_with_keys_having_multiple_inputs()
