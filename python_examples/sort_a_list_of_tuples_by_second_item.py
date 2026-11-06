"""Program to sort a list of tuples by the second item."""

def sort_a_list_of_tuples_by_second_item():
    """Sort a list of tuples based on the second element."""
    tuples = [('apple', 3), ('banana', 1), ('cherry', 2), ('date', 5)]

    sorted_tuples = sorted(tuples, key=lambda x: x[1])

    print(f"Original tuples: {tuples}")
    print(f"Sorted by second item: {sorted_tuples}")
    return sorted_tuples

if __name__ == "__main__":
    sort_a_list_of_tuples_by_second_item()
