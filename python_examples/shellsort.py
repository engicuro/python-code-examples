"""Program to implement Shell sort."""

def shellsort():
    """Sort an array using Shell sort algorithm."""
    arr = [12, 34, 54, 2, 3]

    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    print(f"Original array: [12, 34, 54, 2, 3]")
    print(f"Sorted array: {arr}")
    return arr

if __name__ == "__main__":
    shellsort()
