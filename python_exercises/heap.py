"""Heap - Exercise (Quiz).

A heap is a special tree-based data structure where the
parent node is always smaller (min-heap) or larger (max-heap)
than its children. We'll simulate a min-heap using a sorted list.
"""

def heap():
    """Quiz: Demonstrate heap-like operations using a sorted list."""
    # Start with some numbers
    data = [15, 10, 20, 8, 25, 5]

    # A min-heap keeps the smallest element at the front.
    # We simulate this by keeping our list sorted.
    data.sort()
    print(f"Min heap (sorted list): {data}")
    print(f"  Smallest element: {data[0]}")

    # Push: add a new element and re-sort
    data.append(3)
    data.sort()
    print(f"\nAfter pushing 3: {data}")
    print(f"  Smallest element: {data[0]}")

    # Pop: remove and return the smallest element (front of list)
    smallest = data.pop(0)
    print(f"\nPopped smallest element: {smallest}")
    print(f"Heap after pop: {data}")

    # Get the N largest elements (sort in reverse and take first N)
    print(f"\n3 largest elements: {sorted(data, reverse=True)[:3]}")

    # Get the N smallest elements (first N in sorted list)
    print(f"3 smallest elements: {data[:3]}")

# Run the function when this file is executed
if __name__ == "__main__":
    heap()
