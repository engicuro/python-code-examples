"""Namespace and Scope - Exercise (Quiz)."""

def namespace_and_scope():
    """Quiz: Demonstrate variable scope in Python."""
    global_var = "I am global"

    def outer_function():
        enclosing_var = "I am enclosing"

        def inner_function():
            local_var = "I am local"
            print(f"Inside inner: {global_var}")
            print(f"Inside inner: {enclosing_var}")
            print(f"Inside inner: {local_var}")

        inner_function()
        print(f"Inside outer: {enclosing_var}")

    outer_function()
    print(f"Global scope: {global_var}")

if __name__ == "__main__":
    namespace_and_scope()
