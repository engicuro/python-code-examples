"""Program to swap two elements in a list."""

def swap_two_elements_in_a_list():
    """Swap two elements in a list."""
    arr = [1, 2, 3, 4, 5]
    i, j = 1, 3

    print(f"Original list: {arr}")
    print(f"Swapping elements at indices {i} and {j}")

    arr[i], arr[j] = arr[j], arr[i]

    print(f"List after swap: {arr}")
    return arr

if __name__ == "__main__":
    swap_two_elements_in_a_list()
