"""Program to count characters, words, spaces, and lines in a file."""

def count_characters_words_spaces_and_lines_in_a_file():
    """Count characters, words, spaces, and lines in a text file."""
    with open("sample_text.txt", "w") as f:
        f.write("Hello World\n")
        f.write("This is a sample text file.\n")
        f.write("It has multiple lines.\n")

    char_count = 0
    word_count = 0
    space_count = 0
    line_count = 0

    with open("sample_text.txt", "r") as f:
        for line in f:
            line_count += 1
            char_count += len(line)
            space_count += line.count(' ')
            word_count += len(line.split())

    print(f"Characters: {char_count}")
    print(f"Words: {word_count}")
    print(f"Spaces: {space_count}")
    print(f"Lines: {line_count}")

    return char_count, word_count, space_count, line_count

if __name__ == "__main__":
    count_characters_words_spaces_and_lines_in_a_file()
