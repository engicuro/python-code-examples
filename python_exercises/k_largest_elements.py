"""K Largest Elements - Exercise.

Given an array of numbers, find the K largest elements.
For example, in [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
the 4 largest elements are [9, 6, 5, 5].
"""

def k_largest_elements():
    """Find the K largest elements in an array."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    k = 4  # How many of the largest elements we want

    # Sort the array from largest to smallest,
    # then take the first k elements
    result = sorted(arr, reverse=True)[:k]

    print(f"Array: {arr}")
    print(f"K = {k}")
    print(f"The {k} largest elements: {result}")
    return result

# Run the function when this file is executed
if __name__ == "__main__":
    k_largest_elements()
