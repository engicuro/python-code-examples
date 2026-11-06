"""Program to implement odd-even sort (brick sort)."""

def odd_even_sort_brick_sort():
    """Sort an array using odd-even sort (brick sort)."""
    arr = [5, 1, 4, 2, 8, 0, 2]

    n = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

    print(f"Original array: [5, 1, 4, 2, 8, 0, 2]")
    print(f"Sorted array: {arr}")
    return arr

if __name__ == "__main__":
    odd_even_sort_brick_sort()
