"""Program to create tuples of numbers and their cubes."""

def create_tuples_of_numbers_and_their_cubes():
    """Create a list of tuples where each tuple contains a number and its cube."""
    n = 5
    result = [(i, i ** 3) for i in range(1, n + 1)]

    print(f"Numbers 1 to {n} with their cubes:")
    for num, cube in result:
        print(f"  {num}^3 = {cube}")

    return result

if __name__ == "__main__":
    create_tuples_of_numbers_and_their_cubes()
