"""Program to find the length of a list."""

def find_length_of_a_list():
    """Find the length of a list without using len()."""
    my_list = [10, 20, 30, 40, 50]

    length1 = len(my_list)

    count = 0
    for _ in my_list:
        count += 1
    length2 = count

    length3 = sum(1 for _ in my_list)

    print(f"List: {my_list}")
    print(f"Length (using len()): {length1}")
    print(f"Length (using loop): {length2}")
    print(f"Length (using sum): {length3}")
    return length1

if __name__ == "__main__":
    find_length_of_a_list()
