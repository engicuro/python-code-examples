"""Program to sort Python dictionaries by key or value."""

def sort_python_dictionaries_by_key_or_value():
    """Sort a dictionary by key or by value."""
    my_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}

    sorted_by_key = dict(sorted(my_dict.items()))

    sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    print(f"Original dictionary: {my_dict}")
    print(f"Sorted by key: {sorted_by_key}")
    print(f"Sorted by value: {sorted_by_value}")
    return sorted_by_key, sorted_by_value

if __name__ == "__main__":
    sort_python_dictionaries_by_key_or_value()
