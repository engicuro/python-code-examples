"""Program to implement counting sort."""

def counting_sort():
    """Sort an array using counting sort algorithm."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    max_val = max(arr)

    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(max_val + 1):
        sorted_arr.extend([i] * count[i])

    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")
    return sorted_arr

if __name__ == "__main__":
    counting_sort()
