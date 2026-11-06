"""Program to reverse a single line of a text file."""

def reverse_a_single_line_of_a_text_file():
    """Reverse the content of a single line in a text file."""
    with open("sample_line.txt", "w") as f:
        f.write("Hello World! This is a test line.")

    with open("sample_line.txt", "r") as f:
        line = f.readline().strip()

    reversed_line = line[::-1]

    print(f"Original line: '{line}'")
    print(f"Reversed line: '{reversed_line}'")
    return reversed_line

if __name__ == "__main__":
    reverse_a_single_line_of_a_text_file()
