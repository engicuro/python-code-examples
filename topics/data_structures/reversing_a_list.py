"""Program to reverse a list."""

def reversing_a_list():
    """Reverse a list using different methods."""
    original = [1, 2, 3, 4, 5]

    list1 = original.copy()
    list1.reverse()

    list2 = original[::-1]

    print(f"Original list: {original}")
    print(f"Reversed (reverse()): {list1}")
    print(f"Reversed (slicing): {list2}")
    return list1

if __name__ == "__main__":
    reversing_a_list()
