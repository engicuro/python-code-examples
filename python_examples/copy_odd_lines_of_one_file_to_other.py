"""Program to copy odd lines from one file to another."""

def copy_odd_lines_of_one_file_to_other():
    """Copy odd-numbered lines from one file to another."""
    with open("source_odd.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"Line {i}\n")

    with open("source_odd.txt", "r") as src:
        lines = src.readlines()

    with open("odd_lines.txt", "w") as dest:
        for i, line in enumerate(lines):
            if i % 2 == 0:
                dest.write(line)

    print("Odd lines copied successfully.")
    print("Content of odd_lines.txt:")
    with open("odd_lines.txt", "r") as f:
        print(f.read())

if __name__ == "__main__":
    copy_odd_lines_of_one_file_to_other()
