"""Program to merge two dictionaries."""

def merging_two_dictionaries():
    """Merge two dictionaries using different methods."""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}

    merged1 = dict1.copy()
    merged1.update(dict2)

    merged2 = {**dict1, **dict2}

    merged3 = dict1 | dict2

    print(f"Dict 1: {dict1}")
    print(f"Dict 2: {dict2}")
    print(f"Merged (update): {merged1}")
    print(f"Merged (** unpacking): {merged2}")
    print(f"Merged (| operator): {merged3}")
    return merged2

if __name__ == "__main__":
    merging_two_dictionaries()
