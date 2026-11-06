"""Program to split a string into words and join them back."""

def split_and_join_a_string():
    """Split a string into words and join them back with a different separator."""
    test_string = "Hello World Python Programming"

    words = test_string.split()
    print(f"Original string: '{test_string}'")
    print(f"Split into words: {words}")

    joined_space = ' '.join(words)
    joined_dash = '-'.join(words)
    joined_underscore = '_'.join(words)

    print(f"Joined with space: '{joined_space}'")
    print(f"Joined with dash: '{joined_dash}'")
    print(f"Joined with underscore: '{joined_underscore}'")
    return words

if __name__ == "__main__":
    split_and_join_a_string()
