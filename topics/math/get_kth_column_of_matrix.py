"""Program to get the Kth column of a matrix."""

def get_kth_column_of_matrix():
    """Extract the Kth column from a matrix."""
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    k = 2

    column = [row[k] for row in matrix]

    print("Matrix:")
    for row in matrix:
        print(f"  {row}")
    print(f"Kth column (k={k}): {column}")
    return column

if __name__ == "__main__":
    get_kth_column_of_matrix()
