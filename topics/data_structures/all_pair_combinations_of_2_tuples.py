"""Program to find all pair combinations of two tuples.

A pair combination means we take one item from the
first tuple and pair it with one item from the second
tuple. For example, (1, 'a') is one such pair.
"""

def all_pair_combinations_of_2_tuples():
    """Find all pair combinations of two tuples."""
    tuple1 = (1, 2, 3)
    tuple2 = ('a', 'b', 'c')

    # For each item in tuple1, pair it with every item in tuple2
    combinations = []
    for x in tuple1:
        for y in tuple2:
            combinations.append((x, y))

    print(f"Tuple 1: {tuple1}")
    print(f"Tuple 2: {tuple2}")
    print(f"All pair combinations: {combinations}")
    return combinations

# Run the function when this file is executed
if __name__ == "__main__":
    all_pair_combinations_of_2_tuples()
