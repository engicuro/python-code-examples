"""Program to implement gnome sort."""

def gnome_sort():
    """Sort an array using gnome sort algorithm."""
    arr = [34, 2, 10, -9, 5, 23, 1]

    index = 0
    n = len(arr)
    while index < n:
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

    print(f"Original array: [34, 2, 10, -9, 5, 23, 1]")
    print(f"Sorted array: {arr}")
    return arr

if __name__ == "__main__":
    gnome_sort()
