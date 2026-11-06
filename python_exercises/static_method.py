"""Static Method - Exercise."""

class MathUtils:
    """A class demonstrating static methods."""

    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b

    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def is_even(n):
        """Check if a number is even."""
        return n % 2 == 0

def static_method():
    """Demonstrate static methods."""
    print(f"5 + 3 = {MathUtils.add(5, 3)}")
    print(f"4 * 7 = {MathUtils.multiply(4, 7)}")
    print(f"Is 10 even? {MathUtils.is_even(10)}")
    print(f"Is 7 even? {MathUtils.is_even(7)}")

if __name__ == "__main__":
    static_method()
