"""First Repeating - Exercise."""

def first_repeating():
    """Find the first repeating element in an array."""
    arr = [10, 5, 3, 4, 3, 5, 6]

    seen = set()
    first_repeat = None

    for num in arr:
        if num in seen:
            first_repeat = num
            break
        seen.add(num)

    print(f"Array: {arr}")
    print(f"First repeating element: {first_repeat}")
    return first_repeat

if __name__ == "__main__":
    first_repeating()
