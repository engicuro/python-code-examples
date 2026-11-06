"""Program to find keys associated with values in a dictionary."""

def keys_associated_with_values_in_dictionary():
    """Find keys that map to a specific value in a dictionary."""
    my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    target_value = 2

    keys1 = [k for k, v in my_dict.items() if v == target_value]

    keys2 = list(filter(lambda k: my_dict[k] == target_value, my_dict))

    print(f"Dictionary: {my_dict}")
    print(f"Keys with value {target_value} (list comp): {keys1}")
    print(f"Keys with value {target_value} (filter): {keys2}")
    return keys1

if __name__ == "__main__":
    keys_associated_with_values_in_dictionary()
