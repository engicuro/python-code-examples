"""Jumping through While - Exercise."""

def jumping_through_while():
    """Demonstrate break and continue in while loops."""
    i = 0
    while i < 20:
        i += 1
        if i == 5:
            continue  # Skip 5
        if i == 10:
            break  # Stop at 10
        print(i, end=" ")
    print()

if __name__ == "__main__":
    jumping_through_while()
