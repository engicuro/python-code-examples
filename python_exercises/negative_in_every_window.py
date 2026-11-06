"""Negative in Every Window of Size K - Exercise.

Given an array and a window size k, find all negative numbers
in every consecutive window of size k as it slides across the array.
If a window has no negatives, we record [0].
"""

def negative_in_every_window():
    """Find all negative numbers in every window of size k."""
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3  # Size of the sliding window

    n = len(arr)
    result = []  # This will store the negatives for each window

    # Slide the window across the array, one position at a time
    for start_index in range(n - k + 1):
        # Get the current window of k elements
        window = arr[start_index:start_index + k]

        # Find all negative numbers in this window
        negatives = []
        for num in window:
            if num < 0:
                negatives.append(num)

        # If there are no negatives, record [0] instead
        if len(negatives) == 0:
            negatives = [0]

        result.append(negatives)

    # Print the results
    print(f"Array: {arr}")
    print(f"Window size K = {k}")
    for window_index, neg in enumerate(result):
        print(f"Window {window_index + 1}: {neg}")

    return result

# Run the function when this file is executed
if __name__ == "__main__":
    negative_in_every_window()
