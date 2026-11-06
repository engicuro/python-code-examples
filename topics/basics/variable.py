"""Variable - Exercise (Quiz)."""

def variable():
    """Quiz: Identify valid Python variable names."""
    valid_names = ["my_var", "_private", "var123", "ClassName"]
    invalid_names = ["2nd_var", "my-var", "class", "import", "my var"]

    print("Valid variable names:")
    for name in valid_names:
        print(f"  {name}: {'Valid' if name.isidentifier() else 'Invalid'}")

    print("\nInvalid variable names:")
    for name in invalid_names:
        print(f"  {name}: {'Valid' if name.isidentifier() else 'Invalid'}")

if __name__ == "__main__":
    variable()
