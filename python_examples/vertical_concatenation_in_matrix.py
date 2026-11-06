"""Program to concatenate matrices vertically."""

def vertical_concatenation_in_matrix():
    """Concatenate two matrices vertically (stack rows)."""
    matrix1 = [[1, 2, 3],
               [4, 5, 6]]
    matrix2 = [[7, 8, 9],
               [10, 11, 12]]

    result = matrix1 + matrix2

    print("Matrix 1:")
    for row in matrix1:
        print(f"  {row}")
    print("\nMatrix 2:")
    for row in matrix2:
        print(f"  {row}")
    print("\nVertical concatenation:")
    for row in result:
        print(f"  {row}")
    return result

if __name__ == "__main__":
    vertical_concatenation_in_matrix()
