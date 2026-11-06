"""K Sized Subarray Maximum - Exercise.

Given an array and a window size k, find the maximum value
in every consecutive window of size k as it slides across the array.

Example: arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Windows:  [1,3,-1], [3,-1,-3], [-1,-3,5], [-3,5,3], [5,3,6], [3,6,7]
Maximums:    3,       3,       5,       5,       6,       7
"""

def k_sized_subarray_maximum():
    """Find the maximum in every window of size k.

    For beginners: We look at every group of k neighboring elements,
    find the biggest number in each group, and save it.
    """
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3  # Size of the sliding window

    n = len(arr)
    result = []  # This will store the maximum for each window

    # Go through the array, stopping when the window goes past the end
    for i in range(n - k + 1):
        # Grab the current window of k elements
        window = arr[i:i + k]

        # Find the biggest number in this window
        biggest = max(window)

        # Save it to our results
        result.append(biggest)

        # Show what we're doing (helpful for learning)
        print(f"Window {i + 1}: {window} -> max = {biggest}")

    print(f"\nArray: {arr}")
    print(f"Window size K = {k}")
    print(f"Maximum in each window: {result}")
    return result

# Run the function when this file is executed
if __name__ == "__main__":
    k_sized_subarray_maximum()
