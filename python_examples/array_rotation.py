"""Program to rotate an array by a given number of positions."""

def array_rotation():
    """Rotate an array by a given number of positions."""
    arr = [1, 2, 3, 4, 5]
    d = 2

    print(f"Original array: {arr}")

    rotated = arr[d:] + arr[:d]
    print(f"Array after rotating {d} positions: {rotated}")

    arr2 = arr.copy()
    for _ in range(d):
        arr2.append(arr2.pop(0))
    print(f"Array after rotating {d} positions (pop/insert): {arr2}")

    return rotated

if __name__ == "__main__":
    array_rotation()
