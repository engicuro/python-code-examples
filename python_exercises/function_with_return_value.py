"""Function With Return Value - Exercise."""

def function_with_return_value():
    """Demonstrate functions that return values."""
    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    result1 = add(5, 3)
    result2 = multiply(4, 7)

    print(f"Addition: 5 + 3 = {result1}")
    print(f"Multiplication: 4 * 7 = {result2}")
    return result1, result2

if __name__ == "__main__":
    function_with_return_value()
