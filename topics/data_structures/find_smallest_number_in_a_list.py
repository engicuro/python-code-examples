"""Program to find the smallest number in a list."""

def find_smallest_number_in_a_list():
    """Find the smallest element in a list."""
    arr = [12, 3, 5, 7, 19, 1, 8]

    smallest1 = min(arr)

    smallest2 = arr[0]
    for num in arr[1:]:
        if num < smallest2:
            smallest2 = num

    print(f"List: {arr}")
    print(f"Smallest (using min()): {smallest1}")
    print(f"Smallest (using loop): {smallest2}")
    return smallest1

if __name__ == "__main__":
    find_smallest_number_in_a_list()
