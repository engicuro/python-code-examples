"""Program to implement linear search in a list."""

def linear_search():
    """Search for an element in a list using linear search."""
    arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    target = 110

    for i, num in enumerate(arr):
        if num == target:
            print(f"Element {target} found at index {i}")
            return i

    print(f"Element {target} not found")
    return -1

if __name__ == "__main__":
    linear_search()
