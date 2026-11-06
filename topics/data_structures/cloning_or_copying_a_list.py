"""Program to clone or copy a list."""

def cloning_or_copying_a_list():
    """Demonstrate different ways to copy/clone a list."""
    original = [1, 2, 3, 4, 5]

    copy1 = original.copy()
    copy2 = list(original)
    copy3 = original[:]

    print(f"Original list: {original}")
    print(f"Copy using copy(): {copy1}")
    print(f"Copy using list(): {copy2}")
    print(f"Copy using slicing: {copy3}")

    original.append(6)
    print(f"\nAfter appending 6 to original:")
    print(f"Original: {original}")
    print(f"Copy1: {copy1}")

if __name__ == "__main__":
    cloning_or_copying_a_list()
