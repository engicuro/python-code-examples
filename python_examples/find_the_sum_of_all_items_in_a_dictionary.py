"""Program to find the sum of all values in a dictionary."""

def find_the_sum_of_all_items_in_a_dictionary():
    """Calculate the sum of all values in a dictionary."""
    my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

    total1 = sum(my_dict.values())

    total2 = 0
    for value in my_dict.values():
        total2 += value

    print(f"Dictionary: {my_dict}")
    print(f"Sum (using sum()): {total1}")
    print(f"Sum (using loop): {total2}")
    return total1

if __name__ == "__main__":
    find_the_sum_of_all_items_in_a_dictionary()
