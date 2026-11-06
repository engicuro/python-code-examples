"""Program to implement comb sort."""

def comb_sort():
    """Sort an array using comb sort algorithm."""
    arr = [8, 4, 1, 56, 3, 44, 23, 6, 28, 16]

    def get_next_gap(gap):
        gap = int(gap * 10 / 13)
        if gap < 1:
            return 1
        return gap

    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False

        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

    print(f"Original array: [8, 4, 1, 56, 3, 44, 23, 6, 28, 16]")
    print(f"Sorted array: {arr}")
    return arr

if __name__ == "__main__":
    comb_sort()
