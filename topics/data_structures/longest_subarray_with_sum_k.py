"""Longest Subarray with Sum K - Exercise."""

def longest_subarray_with_sum_k():
    """Find the length of the longest subarray with a given sum."""
    arr = [10, 5, 2, 7, 1, 9]
    k = 15

    max_length = 0
    n = len(arr)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == k:
                max_length = max(max_length, j - i + 1)

    print(f"Array: {arr}")
    print(f"Target sum: {k}")
    print(f"Longest subarray length: {max_length}")
    return max_length

if __name__ == "__main__":
    longest_subarray_with_sum_k()
