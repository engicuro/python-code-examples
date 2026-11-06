"""Program to join tuples if they have similar initial elements."""

def join_tuples_if_similar_initial_element():
    """Join tuples that share the same first element."""
    tuples = [(1, 'a'), (1, 'b'), (2, 'c'), (2, 'd'), (3, 'e')]

    grouped = {}
    for first, rest in tuples:
        if first not in grouped:
            grouped[first] = []
        grouped[first].append(rest)

    result = []
    for key, values in grouped.items():
        joined = (key,) + tuple(values)
        result.append(joined)

    print(f"Original tuples: {tuples}")
    print(f"Joined tuples: {result}")
    return result

if __name__ == "__main__":
    join_tuples_if_similar_initial_element()
