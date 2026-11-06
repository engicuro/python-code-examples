"""Program to flatten a tuple of lists into a single tuple."""

def flatten_tuple_of_list_to_tuple():
    """Flatten a tuple containing lists into a single tuple."""
    nested = ([1, 2, 3], [4, 5], [6, 7, 8, 9])

    flat_list = []
    for item in nested:
        flat_list.extend(item)
    result1 = tuple(flat_list)

    result2 = tuple(item for sublist in nested for item in sublist)

    print(f"Nested tuple: {nested}")
    print(f"Flattened (loop): {result1}")
    print(f"Flattened (comprehension): {result2}")
    return result1

if __name__ == "__main__":
    flatten_tuple_of_list_to_tuple()
