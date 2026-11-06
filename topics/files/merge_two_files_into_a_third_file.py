"""Program to merge two files into a third file."""

def merge_two_files_into_a_third_file():
    """Merge the contents of two files into a third file."""
    with open("file1.txt", "w") as f:
        f.write("This is content from file 1.\n")

    with open("file2.txt", "w") as f:
        f.write("This is content from file 2.\n")

    with open("file1.txt", "r") as f1:
        content1 = f1.read()

    with open("file2.txt", "r") as f2:
        content2 = f2.read()

    with open("merged_file.txt", "w") as f3:
        f3.write(content1)
        f3.write(content2)

    print("Files merged successfully.")
    print("Merged file content:")
    with open("merged_file.txt", "r") as f:
        print(f.read())

if __name__ == "__main__":
    merge_two_files_into_a_third_file()
