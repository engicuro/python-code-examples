"""Program to find the second largest number in a list."""

def find_second_largest_number_in_a_list():
    """Find the second largest element in a list."""
    arr = [12, 35, 1, 10, 34, 1]

    sorted_arr = sorted(set(arr), reverse=True)
    second_largest1 = sorted_arr[1] if len(sorted_arr) >= 2 else None

    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    print(f"List: {arr}")
    print(f"Second largest (sorted): {second_largest1}")
    print(f"Second largest (single pass): {second}")
    return second

if __name__ == "__main__":
    find_second_largest_number_in_a_list()
