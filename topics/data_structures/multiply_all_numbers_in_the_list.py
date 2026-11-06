"""Program to multiply all numbers in a list.

We start with 1 (the multiplicative identity)
and multiply each number in the list one by one.
For example: [1, 2, 3, 4, 5]
  1 * 1 = 1
  1 * 2 = 2
  2 * 3 = 6
  6 * 4 = 24
  24 * 5 = 120
So the product is 120.
"""

def multiply_all_numbers_in_the_list():
    """Multiply all numbers in a list."""
    arr = [1, 2, 3, 4, 5]

    # Start with 1 (multiplying by 1 doesn't change the result)
    product = 1

    # Multiply each number in the list, one at a time
    for num in arr:
        product = product * num
        print(f"  After multiplying by {num}: product = {product}")

    print(f"\nList: {arr}")
    print(f"Final product: {product}")
    return product

# Run the function when this file is executed
if __name__ == "__main__":
    multiply_all_numbers_in_the_list()
