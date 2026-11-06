"""Less Than - Exercise."""

def less_than():
    """Find all elements less than a given value in a list."""
    arr = [1, 5, 3, 8, 2, 9, 4, 7, 6]
    threshold = 5

    # Using list comprehension
    result = [x for x in arr if x < threshold]
    print(f"List: {arr}")
    print(f"Elements less than {threshold}: {result}")

    # Using filter
    result2 = list(filter(lambda x: x < threshold, arr))
    print(f"Using filter: {result2}")

if __name__ == "__main__":
    less_than()
