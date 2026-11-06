"""Program to extract unique values from a dictionary."""

def extract_unique_values_dictionary_values():
    """Extract unique values from a dictionary."""
    my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 4}

    unique_values = list(set(my_dict.values()))
    print(f"Original dictionary: {my_dict}")
    print(f"Unique values: {unique_values}")
    return unique_values

if __name__ == "__main__":
    extract_unique_values_dictionary_values()
