"""Height of Heap - Exercise."""

def height_of_heap():
    """Calculate the height of a heap with n elements."""
    test_sizes = [1, 2, 3, 4, 7, 8, 15, 16, 100]

    for n in test_sizes:
        # Height of a complete binary tree with n nodes
        height = n.bit_length() if n > 0 else 0
        print(f"Heap with {n} elements: height = {height}")

if __name__ == "__main__":
    height_of_heap()
