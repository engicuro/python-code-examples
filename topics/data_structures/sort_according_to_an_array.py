"""Sort According to an Array - Exercise.

Given two arrays, sort the first array so that elements
appear in the same order as they do in the second array.
Elements not in the second array go to the end (sorted).
"""

def sort_according_to_an_array():
    """Sort elements of arr1 according to the order defined by arr2."""
    arr1 = [1, 5, 3, 2, 4]
    arr2 = [5, 2, 1]

    # Build a priority dictionary from arr2.
    # The earlier an element appears in arr2, the higher its priority (lower number).
    # Example: arr2 = [5, 2, 1] means 5 has priority 0, 2 has priority 1, 1 has priority 2.
    priority = {}
    for index, value in enumerate(arr2):
        priority[value] = index

    # Separate arr1 into two groups:
    # - Elements that ARE in arr2 (we'll sort them by arr2's order)
    # - Elements that are NOT in arr2 (we'll sort them normally)
    in_order = []
    not_in_order = []

    for x in arr1:
        if x in priority:
            in_order.append(x)
        else:
            not_in_order.append(x)

    # Sort the "in arr2" group by their priority (position in arr2)
    in_order.sort(key=lambda x: priority[x])

    # Sort the "not in arr2" group in normal ascending order
    not_in_order.sort()

    # Combine the two groups
    result = in_order + not_in_order

    print(f"Original array: {arr1}")
    print(f"Order array: {arr2}")
    print(f"Sorted according to order array: {result}")
    return result

if __name__ == "__main__":
    sort_according_to_an_array()
