"""Program to find the largest element in an array."""

def largest_element_in_an_array():
    """Find the largest element in an array."""
    arr = [10, 324, 45, 90, 9808]

    largest1 = max(arr)

    largest2 = arr[0]
    for num in arr[1:]:
        if num > largest2:
            largest2 = num

    print(f"Array: {arr}")
    print(f"Largest element (using max()): {largest1}")
    print(f"Largest element (using loop): {largest2}")
    return largest1

if __name__ == "__main__":
    largest_element_in_an_array()
