"""Program to count matching characters between two strings."""

def count_matching_characters_in_two_strings():
    """Count the number of matching characters between two strings."""
    str1 = "aabcc"
    str2 = "abdca"

    counter1 = {}
    for ch in str1:
        counter1[ch] = counter1.get(ch, 0) + 1
    counter2 = {}
    for ch in str2:
        counter2[ch] = counter2.get(ch, 0) + 1

    common = {}
    for ch in counter1:
        if ch in counter2:
            common[ch] = min(counter1[ch], counter2[ch])
    total_matches = sum(common.values())

    print(f"String 1: '{str1}'")
    print(f"String 2: '{str2}'")
    print(f"Matching characters: {common}")
    print(f"Total matching characters: {total_matches}")
    return total_matches

if __name__ == "__main__":
    count_matching_characters_in_two_strings()
