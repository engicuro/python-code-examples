"""Program to remove tuples of a specific length K from a list."""

def remove_tuples_of_length_k():
    """Remove all tuples of length K from a list of tuples."""
    tuple_list = [(1,), (1, 2), (1, 2, 3), (4,), (5, 6), (7, 8, 9), (10,)]
    k = 1

    filtered = [t for t in tuple_list if len(t) != k]

    print(f"Original list: {tuple_list}")
    print(f"After removing tuples of length {k}: {filtered}")
    return filtered

if __name__ == "__main__":
    remove_tuples_of_length_k()
