"""Program to sort the values of the first list using the second list."""

def sort_the_values_of_first_list_using_second_list():
    """Sort the first list based on the values of the second list."""
    list1 = [3, 1, 4, 1, 5]
    list2 = ['c', 'a', 'd', 'b', 'e']

    paired = list(zip(list2, list1))
    paired.sort()
    sorted_list1 = [x[1] for x in paired]
    sorted_list2 = [x[0] for x in paired]

    print(f"List 1 (original): {list1}")
    print(f"List 2 (original): {list2}")
    print(f"List 1 (sorted by List 2): {sorted_list1}")
    print(f"List 2 (sorted): {sorted_list2}")
    return sorted_list1

if __name__ == "__main__":
    sort_the_values_of_first_list_using_second_list()
