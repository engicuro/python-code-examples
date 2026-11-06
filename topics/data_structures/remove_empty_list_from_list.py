"""Program to remove empty lists from a list of lists."""

def remove_empty_list_from_list():
    """Remove empty sublists from a list of lists."""
    list_of_lists = [[1, 2, 3], [], [4, 5], [], [], [6, 7, 8], []]

    filtered1 = [lst for lst in list_of_lists if lst]

    filtered2 = list(filter(None, list_of_lists))

    print(f"Original list: {list_of_lists}")
    print(f"Filtered (comprehension): {filtered1}")
    print(f"Filtered (filter): {filtered2}")
    return filtered1

if __name__ == "__main__":
    remove_empty_list_from_list()
