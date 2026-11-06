"""Program to reverse the content of a file using a stack."""

def reverse_the_content_of_a_file_using_stack():
    """Reverse file content using a stack (LIFO) data structure."""
    with open("stack_source.txt", "w") as f:
        f.write("First line\nSecond line\nThird line\n")

    stack = []
    with open("stack_source.txt", "r") as f:
        for line in f:
            stack.append(line)

    with open("stack_reversed.txt", "w") as f:
        while stack:
            f.write(stack.pop())

    print("Content reversed using stack and written to stack_reversed.txt")

    with open("stack_reversed.txt", "r") as f:
        print("Reversed content:")
        print(f.read())

if __name__ == "__main__":
    reverse_the_content_of_a_file_using_stack()
