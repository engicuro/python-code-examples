"""Program to split an array and rotate it."""

def split_and_rotate_an_array():
    """Split an array into two parts and rotate them."""
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    left = arr[:k]
    right = arr[k:]
    rotated = right + left

    print(f"Original array: {arr}")
    print(f"Split at index {k}: left={left}, right={right}")
    print(f"After rotation: {rotated}")
    return rotated

if __name__ == "__main__":
    split_and_rotate_an_array()
