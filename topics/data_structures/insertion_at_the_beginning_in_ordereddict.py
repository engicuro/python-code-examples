"""Program to insert an element at the beginning of a dictionary.

In Python 3.7+, dictionaries remember the order
keys were added. To insert at the beginning,
we create a new dictionary with the new key first,
then add all the old keys.
"""

def insertion_at_the_beginning_in_ordereddict():
    """Insert a key-value pair at the beginning of a dictionary."""
    # Start with a dictionary of three items
    my_dict = {'b': 2, 'c': 3, 'd': 4}

    print("Before insertion:")
    for key, value in my_dict.items():
        print(f"  {key}: {value}")

    # To insert at the beginning, we create a new dictionary
    # with the new key first, then unpack the old dictionary
    my_dict = {'a': 1, **my_dict}

    print("\nAfter inserting 'a' at the beginning:")
    for key, value in my_dict.items():
        print(f"  {key}: {value}")

# Run the function when this file is executed
if __name__ == "__main__":
    insertion_at_the_beginning_in_ordereddict()
