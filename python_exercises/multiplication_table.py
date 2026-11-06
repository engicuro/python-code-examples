"""Multiplication Table - Exercise."""

def multiplication_table():
    """Print the multiplication table of a given number."""
    num = 5

    print(f"Multiplication table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

if __name__ == "__main__":
    multiplication_table()
