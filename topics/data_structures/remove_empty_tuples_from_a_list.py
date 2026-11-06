"""Program to remove empty tuples from a list."""

def remove_empty_tuples_from_a_list():
    """Remove empty tuples from a list."""
    list_with_tuples = [(1, 2), (), (3, 4), (), (5,), (), ('a', 'b')]

    filtered1 = [t for t in list_with_tuples if t]

    filtered2 = list(filter(None, list_with_tuples))

    print(f"Original list: {list_with_tuples}")
    print(f"Filtered (comprehension): {filtered1}")
    print(f"Filtered (filter): {filtered2}")
    return filtered1

if __name__ == "__main__":
    remove_empty_tuples_from_a_list()
