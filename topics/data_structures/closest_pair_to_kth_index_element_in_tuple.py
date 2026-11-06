"""Program to find the closest pair to the Kth index element in a tuple."""

def closest_pair_to_kth_index_element_in_tuple():
    """Find the pair of elements closest to the Kth index element."""
    tup = (10, 22, 28, 29, 30, 40)
    k = 3

    if k >= len(tup):
        print("K is out of range.")
        return None

    target = tup[k]
    print(f"Tuple: {tup}")
    print(f"Kth index ({k}) element: {target}")

    closest_pair = None
    min_diff = float('inf')

    for i in range(len(tup)):
        for j in range(i + 1, len(tup)):
            pair_sum = tup[i] + tup[j]
            diff = abs(pair_sum - target)
            if diff < min_diff:
                min_diff = diff
                closest_pair = (tup[i], tup[j])

    print(f"Closest pair to {target}: {closest_pair} (sum = {sum(closest_pair)}, diff = {min_diff})")
    return closest_pair

if __name__ == "__main__":
    closest_pair_to_kth_index_element_in_tuple()
