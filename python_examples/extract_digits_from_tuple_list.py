"""Program to extract digits from a list of tuples."""

def extract_digits_from_tuple_list():
    """Extract all digits from a list of tuples."""
    tuple_list = [(1, 2, 3), (4, 5), (6, 7, 8, 9)]

    digits = [item for tup in tuple_list for item in tup]
    print(f"Original list of tuples: {tuple_list}")
    print(f"Extracted digits: {digits}")

    digits2 = [item for tup in tuple_list for item in tup]
    print(f"Using chain equivalent: {digits2}")

    return digits

if __name__ == "__main__":
    extract_digits_from_tuple_list()
