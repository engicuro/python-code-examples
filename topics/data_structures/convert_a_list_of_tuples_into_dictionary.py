"""Program to convert a list of tuples into a dictionary."""

def convert_a_list_of_tuples_into_dictionary():
    """Convert a list of key-value tuples into a dictionary."""
    list_of_tuples = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

    dict1 = dict(list_of_tuples)
    print(f"Using dict(): {dict1}")

    dict2 = {key: value for key, value in list_of_tuples}
    print(f"Using comprehension: {dict2}")

    dict3 = {}
    for key, value in list_of_tuples:
        dict3[key] = value
    print(f"Using loop: {dict3}")

    return dict1

if __name__ == "__main__":
    convert_a_list_of_tuples_into_dictionary()
