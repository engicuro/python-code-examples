"""Program to add a tuple to a list and vice versa."""

def adding_tuple_to_list_and_vice_versa():
    """Demonstrate adding a tuple to a list and vice versa."""
    my_tuple = (1, 2, 3, 4, 5)
    my_list = list(my_tuple)
    print(f"Tuple {my_tuple} converted to list: {my_list}")

    my_list2 = [10, 20, 30, 40, 50]
    my_tuple2 = tuple(my_list2)
    print(f"List {my_list2} converted to tuple: {my_tuple2}")

    my_list.append(my_tuple)
    print(f"List after appending tuple: {my_list}")

    combined = my_tuple2 + tuple(my_list2)
    print(f"New tuple after adding list elements: {combined}")

if __name__ == "__main__":
    adding_tuple_to_list_and_vice_versa()
