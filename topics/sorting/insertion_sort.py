"""Program to implement insertion sort."""

def insertion_sort():
    """Sort an array using insertion sort algorithm."""
    arr = [12, 11, 13, 5, 6]

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print(f"Original array: [12, 11, 13, 5, 6]")
    print(f"Sorted array: {arr}")
    return arr

if __name__ == "__main__":
    insertion_sort()
