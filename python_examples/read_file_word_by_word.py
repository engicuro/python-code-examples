"""Program to read a file word by word."""

def read_file_word_by_word():
    """Read a file one word at a time."""
    with open("sample_words_file.txt", "w") as f:
        f.write("Hello world this is a sample file")

    print("Reading file word by word:")
    with open("sample_words_file.txt", "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                print(f"Word: '{word}'")

if __name__ == "__main__":
    read_file_word_by_word()
