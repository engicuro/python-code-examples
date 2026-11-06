"""Distinct Elements - Exercise."""

def distinct_elements():
    """Find distinct elements in an array."""
    arr = [1, 2, 3, 2, 1, 4, 5, 4, 6]

    # Method 1: Using set
    distinct1 = list(set(arr))

    # Method 2: Using a loop (preserves order)
    seen = set()
    distinct2 = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            distinct2.append(num)

    print(f"Original array: {arr}")
    print(f"Distinct elements (set): {distinct1}")
    print(f"Distinct elements (ordered): {distinct2}")
    return distinct2

if __name__ == "__main__":
    distinct_elements()
