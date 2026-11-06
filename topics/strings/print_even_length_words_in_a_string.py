"""Program to print all even-length words in a string."""

def print_even_length_words_in_a_string():
    """Print words that have an even number of characters."""
    test_string = "Hello world this is a test string"

    words = test_string.split()
    even_words = [word for word in words if len(word) % 2 == 0]

    print(f"String: '{test_string}'")
    print(f"Even-length words: {even_words}")
    return even_words

if __name__ == "__main__":
    print_even_length_words_in_a_string()
