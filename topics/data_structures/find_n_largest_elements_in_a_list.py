"""Program to find the N largest elements in a list."""

def find_n_largest_elements_in_a_list():
    """Find the N largest elements in a list."""
    arr = [12, 3, 5, 7, 19, 1, 8, 15, 4]
    n = 3

    result = sorted(arr, reverse=True)[:n]

    print(f"List: {arr}")
    print(f"{n} largest elements: {result}")
    return result

if __name__ == "__main__":
    find_n_largest_elements_in_a_list()
