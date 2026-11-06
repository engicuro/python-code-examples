"""Program to rotate an array using the reversal algorithm."""

def reversal_algorithm_for_array_rotation():
    """Rotate an array using the reversal algorithm."""
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2

    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    n = len(arr)
    d = d % n

    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)

    print(f"Original array: [1, 2, 3, 4, 5, 6, 7]")
    print(f"Array after rotating {d} positions: {arr}")
    return arr

if __name__ == "__main__":
    reversal_algorithm_for_array_rotation()
