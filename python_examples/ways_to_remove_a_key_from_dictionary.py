"""Program to remove a key from a dictionary using different methods."""

def ways_to_remove_a_key_from_dictionary():
    """Remove a key from a dictionary using different methods."""
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    key_to_remove = 'b'

    dict1 = my_dict.copy()
    dict1.pop(key_to_remove)

    dict2 = my_dict.copy()
    del dict2[key_to_remove]

    dict3 = {k: v for k, v in my_dict.items() if k != key_to_remove}

    print(f"Original dictionary: {my_dict}")
    print(f"After pop(): {dict1}")
    print(f"After del: {dict2}")
    print(f"Using comprehension: {dict3}")
    return dict1

if __name__ == "__main__":
    ways_to_remove_a_key_from_dictionary()
