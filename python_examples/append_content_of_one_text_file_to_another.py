"""Program to append the content of one text file to another."""

def append_content_of_one_text_file_to_another():
    """Append content of one text file to another."""
    with open("source_file.txt", "w") as f:
        f.write("This is content from the source file.\n")
        f.write("It will be appended to the destination file.\n")

    with open("dest_file.txt", "w") as f:
        f.write("This is the destination file.\n")

    with open("source_file.txt", "r") as src:
        content = src.read()

    with open("dest_file.txt", "a") as dest:
        dest.write(content)

    print("Content appended successfully.")
    print("Destination file content:")
    with open("dest_file.txt", "r") as f:
        print(f.read())

if __name__ == "__main__":
    append_content_of_one_text_file_to_another()
