"""Even Positioned Character - Exercise."""

def even_positioned_character():
    """Print characters at even positions in a string."""
    test_string = "HelloWorld"

    # Using slicing (0-indexed, so even indices are 0, 2, 4...)
    even_chars = test_string[::2]
    print(f"String: '{test_string}'")
    print(f"Even positioned characters: '{even_chars}'")

    # Using loop
    even_chars_loop = ""
    for i in range(len(test_string)):
        if i % 2 == 0:
            even_chars_loop += test_string[i]
    print(f"Even positioned (loop): '{even_chars_loop}'")

if __name__ == "__main__":
    even_positioned_character()
