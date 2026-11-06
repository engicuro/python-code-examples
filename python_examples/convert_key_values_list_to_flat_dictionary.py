"""Program to convert a list of key-value pairs to a flat dictionary."""

def convert_key_values_list_to_flat_dictionary():
    """Convert a list of key-value pairs into a flat dictionary."""
    kv_list = [('name', 'Alice'), ('age', 25), ('city', 'New York')]

    flat_dict = dict(kv_list)
    print(f"Key-value list: {kv_list}")
    print(f"Flat dictionary: {flat_dict}")
    return flat_dict

if __name__ == "__main__":
    convert_key_values_list_to_flat_dictionary()
