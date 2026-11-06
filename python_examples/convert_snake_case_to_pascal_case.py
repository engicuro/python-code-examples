"""Program to convert a snake_case string to PascalCase."""

def convert_snake_case_to_pascal_case():
    """Convert snake_case string to PascalCase."""
    test_strings = ["hello_world", "python_programming", "data_structures"]

    for s in test_strings:
        pascal = ''.join(word.capitalize() for word in s.split('_'))
        print(f"snake_case: '{s}' -> PascalCase: '{pascal}'")

if __name__ == "__main__":
    convert_snake_case_to_pascal_case()
