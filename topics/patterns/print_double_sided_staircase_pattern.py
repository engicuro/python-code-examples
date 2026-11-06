"""Program to print a double-sided staircase pattern."""

def print_double_sided_staircase_pattern():
    """Print a double-sided staircase pattern."""
    n = 5

    print(f"Double-sided staircase pattern (n={n}):")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * i
        print(f"{spaces}{stars}{spaces}")

if __name__ == "__main__":
    print_double_sided_staircase_pattern()
