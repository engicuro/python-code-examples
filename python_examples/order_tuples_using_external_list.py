"""Program to order tuples using an external list."""

def order_tuples_using_external_list():
    """Sort a list of tuples based on an external list of keys."""
    tuples = [('banana', 3), ('apple', 1), ('cherry', 2)]
    order = ['apple', 'banana', 'cherry']

    priority = {key: i for i, key in enumerate(order)}

    sorted_tuples = sorted(tuples, key=lambda x: priority.get(x[0], float('inf')))

    print(f"Original tuples: {tuples}")
    print(f"External order: {order}")
    print(f"Sorted tuples: {sorted_tuples}")
    return sorted_tuples

if __name__ == "__main__":
    order_tuples_using_external_list()
