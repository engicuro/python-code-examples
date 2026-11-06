"""Program to convert a nested tuple to a dictionary with custom keys."""

def convert_nested_tuple_to_custom_key_dictionary():
    """Convert a nested tuple structure into a dictionary with custom keys."""
    nested = (('name', 'Alice'), ('age', 30), ('city', 'London'))

    result = {key: value for key, value in nested}
    print(f"Nested tuple: {nested}")
    print(f"Converted dictionary: {result}")
    return result

if __name__ == "__main__":
    convert_nested_tuple_to_custom_key_dictionary()
