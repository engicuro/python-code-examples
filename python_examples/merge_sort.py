"""Program to implement merge sort."""

def merge_sort():
    """Sort an array using merge sort algorithm."""
    arr = [38, 27, 43, 3, 9, 82, 10]

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        return merge(left, right)

    print(f"Original array: {arr}")
    sorted_arr = merge_sort_recursive(arr)
    print(f"Sorted array: {sorted_arr}")
    return sorted_arr

if __name__ == "__main__":
    merge_sort()
