"""Program to print duplicate elements from a list of integers.

A duplicate is a number that appears more than once in the list.
We count how many times each number appears,
then print only the ones that appear more than once.
"""

def print_duplicates_from_a_list_of_integers():
    """Find and print duplicate elements in a list of integers."""
    arr = [1, 2, 3, 2, 4, 5, 1, 6, 3]

    # Count how many times each number appears
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Find numbers that appear more than once
    duplicates = {}
    for num, count in counts.items():
        if count > 1:
            duplicates[num] = count

    print(f"List: {arr}")
    print(f"Duplicate numbers and their counts: {duplicates}")
    return duplicates

# Run the function when this file is executed
if __name__ == "__main__":
    print_duplicates_from_a_list_of_integers()
