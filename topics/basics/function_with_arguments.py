"""Function With Arguments - Exercise."""

def function_with_arguments():
    """Demonstrate functions with arguments."""
    def greet(name):
        print(f"Hello, {name}!")

    def add(a, b):
        return a + b

    greet("Alice")
    greet("Bob")
    print(f"Sum: {add(10, 20)}")

if __name__ == "__main__":
    function_with_arguments()
