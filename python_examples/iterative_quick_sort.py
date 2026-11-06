"""Program to implement iterative quicksort."""

def iterative_quick_sort():
    """Sort an array using iterative quicksort."""
    arr = [10, 7, 8, 9, 1, 5]

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_iterative(arr):
        stack = [(0, len(arr) - 1)]
        while stack:
            low, high = stack.pop()
            if low < high:
                pi = partition(arr, low, high)
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))

    print(f"Original array: {arr}")
    quick_sort_iterative(arr)
    print(f"Sorted array: {arr}")
    return arr

if __name__ == "__main__":
    iterative_quick_sort()
