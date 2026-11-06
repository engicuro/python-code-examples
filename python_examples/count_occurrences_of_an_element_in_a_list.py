"""Program to count occurrences of a specific element in a list."""

def count_occurrences_of_an_element_in_a_list():
    """Count how many times an element appears in a list."""
    arr = [1, 2, 3, 2, 4, 2, 5, 2, 6]
    target = 2

    count1 = arr.count(target)

    count2 = 0
    for item in arr:
        if item == target:
            count2 += 1

    print(f"List: {arr}")
    print(f"Target: {target}")
    print(f"Count (using count()): {count1}")
    print(f"Count (using loop): {count2}")

    return count1

if __name__ == "__main__":
    count_occurrences_of_an_element_in_a_list()
