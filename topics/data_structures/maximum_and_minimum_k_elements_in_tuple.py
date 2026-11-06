"""Program to find the maximum and minimum K elements in a tuple."""

def maximum_and_minimum_k_elements_in_tuple():
    """Find the K largest and K smallest elements in a tuple."""
    tup = (5, 1, 8, 3, 9, 2, 7, 4, 6)
    k = 3

    sorted_tup = sorted(tup)
    min_k = tuple(sorted_tup[:k])
    max_k = tuple(sorted_tup[-k:])

    print(f"Tuple: {tup}")
    print(f"K = {k}")
    print(f"{k} smallest elements: {min_k}")
    print(f"{k} largest elements: {max_k}")
    return min_k, max_k

if __name__ == "__main__":
    maximum_and_minimum_k_elements_in_tuple()
