"""Program to print an inverted star pattern."""

def print_an_inverted_star_pattern():
    """Print an inverted star pattern."""
    n = 5

    print(f"Inverted star pattern (n={n}):")
    for i in range(n, 0, -1):
        print('*' * i)

if __name__ == "__main__":
    print_an_inverted_star_pattern()
