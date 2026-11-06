"""Program to find the sum of all elements in a list."""

def find_sum_of_elements_in_list():
    """Calculate the sum of all elements in a list."""
    arr = [1, 2, 3, 4, 5]

    total1 = sum(arr)

    total2 = 0
    for num in arr:
        total2 += num

    print(f"List: {arr}")
    print(f"Sum (using sum()): {total1}")
    print(f"Sum (using loop): {total2}")
    return total1

if __name__ == "__main__":
    find_sum_of_elements_in_list()
