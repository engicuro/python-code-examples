"""Program to implement bitonic sort."""

def bitonic_sort():
    """Sort an array using bitonic sort algorithm."""
    arr = [3, 7, 4, 8, 6, 2, 1, 5]

    def compare_and_swap(arr, i, j, direction):
        if (direction == 1 and arr[i] > arr[j]) or (direction == 0 and arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

    def bitonic_merge(arr, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                compare_and_swap(arr, i, i + k, direction)
            bitonic_merge(arr, low, k, direction)
            bitonic_merge(arr, low + k, k, direction)

    def bitonic_sort_rec(arr, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            bitonic_sort_rec(arr, low, k, 1)
            bitonic_sort_rec(arr, low + k, k, 0)
            bitonic_merge(arr, low, cnt, direction)

    n = len(arr)
    direction = 1
    bitonic_sort_rec(arr, 0, n, direction)

    print(f"Original array: [3, 7, 4, 8, 6, 2, 1, 5]")
    print(f"Sorted array: {arr}")
    return arr

if __name__ == "__main__":
    bitonic_sort()
