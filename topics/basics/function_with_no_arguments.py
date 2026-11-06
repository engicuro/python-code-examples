"""Function With No Arguments - Exercise."""

def function_with_no_arguments():
    """Demonstrate functions with no arguments."""
    def greet():
        print("Hello, World!")

    def get_pi():
        return 3.14159

    greet()
    print(f"Pi: {get_pi()}")

if __name__ == "__main__":
    function_with_no_arguments()
