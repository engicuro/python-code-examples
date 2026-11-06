"""Dequeue - Exercise (Quiz).

A deque (double-ended queue) is a data structure that lets you
add and remove items from both the front and the back.
We'll use a Python list to simulate deque operations.
"""

def dequeue():
    """Quiz: Demonstrate deque operations using a list."""
    # Start with a simple list of numbers
    d = [1, 2, 3, 4, 5]
    print(f"Original list: {d}")

    # --- Adding items to both ends ---
    # append() adds to the back (right end)
    d.append(6)
    print(f"After append(6) to back: {d}")

    # insert(0, value) adds to the front (left end)
    d.insert(0, 0)
    print(f"After insert(0, 0) at front: {d}")

    # --- Removing items from both ends ---
    # pop() removes from the back
    d.pop()
    print(f"After pop() from back: {d}")

    # pop(0) removes from the front
    d.pop(0)
    print(f"After pop(0) from front: {d}")

    # --- Rotating the list ---
    # Rotate right by 2: take the last 2 items and move them to the front
    d = d[-2:] + d[:-2]
    print(f"After rotating right by 2: {d}")

    # Rotate left by 1: take the first item and move it to the back
    d = d[1:] + d[:1]
    print(f"After rotating left by 1: {d}")

    # --- Bounded (fixed-size) deque ---
    # A deque with a maximum length. When it gets full,
    # adding a new item removes the oldest one from the front.
    bounded = []
    max_length = 3
    print(f"\nBuilding a bounded deque (max length = {max_length}):")
    for i in range(5):
        bounded.append(i)
        print(f"  After adding {i}: {bounded}")
        if len(bounded) > max_length:
            removed = bounded.pop(0)
            print(f"    Removed {removed} from front (max length reached)")
    print(f"Final bounded deque: {bounded}")

# Run the function when this file is executed
if __name__ == "__main__":
    dequeue()
