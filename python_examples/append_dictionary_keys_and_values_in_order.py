"""Program to append dictionary keys and values in order.

A dictionary in Python remembers the order in which
keys were added (Python 3.7+). We can add new keys
and they will appear at the end.
"""

def append_dictionary_keys_and_values_in_order():
    """Show how dictionary keys maintain insertion order."""
    # Create a dictionary with some initial key-value pairs
    my_dict = {}
    my_dict['first'] = 1
    my_dict['second'] = 2
    my_dict['third'] = 3

    print("Dictionary (in order of addition):")
    for key, value in my_dict.items():
        print(f"  {key}: {value}")

    # Add more keys - they go to the end
    my_dict['fourth'] = 4
    my_dict['fifth'] = 5

    print("\nAfter appending new keys and values:")
    for key, value in my_dict.items():
        print(f"  {key}: {value}")

# Run the function when this file is executed
if __name__ == "__main__":
    append_dictionary_keys_and_values_in_order()
