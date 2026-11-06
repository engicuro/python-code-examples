"""Program to find the remainder of the product of array elements."""

def find_remainder_of_array_product():
    """Find the remainder when the product of array elements is divided by a number."""
    arr = [2, 3, 5, 7, 11]
    divisor = 13

    product = 1
    for num in arr:
        product *= num

    remainder = product % divisor

    print(f"Array: {arr}")
    print(f"Product: {product}")
    print(f"Divisor: {divisor}")
    print(f"Remainder: {remainder}")
    return remainder

if __name__ == "__main__":
    find_remainder_of_array_product()
