"""Program to implement bubble sort."""

def bubble_sort():
    """Sort an array using bubble sort algorithm."""
    arr = [64, 34, 25, 12, 22, 11, 90]

    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    print(f"Original array: [64, 34, 25, 12, 22, 11, 90]")
    print(f"Sorted array: {arr}")
    return arr

if __name__ == "__main__":
    bubble_sort()
