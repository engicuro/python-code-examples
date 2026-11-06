"""Program to implement binary search using both recursive and iterative approaches."""

def binary_search_recursive_and_iterative():
    """Binary search using both recursive and iterative methods."""
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23

    def binary_search_iterative(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def binary_search_recursive(arr, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)

    result_iter = binary_search_iterative(arr, target)
    result_rec = binary_search_recursive(arr, target, 0, len(arr) - 1)

    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Iterative result: Index {result_iter}")
    print(f"Recursive result: Index {result_rec}")

    return result_iter, result_rec

if __name__ == "__main__":
    binary_search_recursive_and_iterative()
