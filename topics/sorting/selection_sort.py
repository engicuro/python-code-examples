"""Program to implement selection sort."""

def selection_sort():
    """Sort an array using selection sort algorithm."""
    arr = [64, 25, 12, 22, 11]

    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(f"Original array: [64, 25, 12, 22, 11]")
    print(f"Sorted array: {arr}")
    return arr

if __name__ == "__main__":
    selection_sort()
