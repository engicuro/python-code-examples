"""Program to reverse the content of a file and store it in another file."""

def reverse_the_content_of_a_file_and_store_it_in_another_file():
    """Reverse the entire content of a file and write it to another file."""
    with open("source_reverse.txt", "w") as f:
        f.write("Line 1\nLine 2\nLine 3\n")

    with open("source_reverse.txt", "r") as src:
        content = src.read()

    reversed_content = content[::-1]

    with open("reversed_output.txt", "w") as dest:
        dest.write(reversed_content)

    print("Original content:")
    print(content)
    print("Reversed content written to reversed_output.txt")

if __name__ == "__main__":
    reverse_the_content_of_a_file_and_store_it_in_another_file()
