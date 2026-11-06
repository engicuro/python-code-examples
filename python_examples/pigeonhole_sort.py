"""Program to implement pigeonhole sort."""

def pigeonhole_sort():
    """Sort an array using pigeonhole sort algorithm."""
    arr = [8, 3, 2, 7, 4, 6, 8]

    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    pigeonholes = [0] * range_of_elements

    for num in arr:
        pigeonholes[num - min_val] += 1

    sorted_arr = []
    for i in range(range_of_elements):
        sorted_arr.extend([i + min_val] * pigeonholes[i])

    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")
    return sorted_arr

if __name__ == "__main__":
    pigeonhole_sort()
