"""Program to check if binary representations of two numbers are anagrams."""

def check_if_binary_representations_of_two_numbers_are_anagram():
    """Check if binary representations of two numbers are anagrams of each other."""
    test_pairs = [(8, 4), (3, 5), (10, 12), (7, 11)]

    for a, b in test_pairs:
        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]
        is_anagram = sorted(bin_a) == sorted(bin_b)
        print(f"{a} ({bin_a}) and {b} ({bin_b}): Anagram = {is_anagram}")

if __name__ == "__main__":
    check_if_binary_representations_of_two_numbers_are_anagram()
