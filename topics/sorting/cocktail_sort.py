"""Program to implement cocktail sort (bidirectional bubble sort)."""

def cocktail_sort():
    """Sort an array using cocktail sort algorithm."""
    arr = [5, 1, 4, 2, 8, 0, 2]

    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        start += 1

    print(f"Original array: [5, 1, 4, 2, 8, 0, 2]")
    print(f"Sorted array: {arr}")
    return arr

if __name__ == "__main__":
    cocktail_sort()
