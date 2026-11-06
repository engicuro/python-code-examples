"""Program to read a file character by character."""

def read_character_by_character_from_a_file():
    """Read a file one character at a time."""
    with open("sample_chars.txt", "w") as f:
        f.write("Hello, World!")

    print("Reading file character by character:")
    with open("sample_chars.txt", "r") as f:
        while True:
            char = f.read(1)
            if not char:
                break
            print(f"Character: '{char}' (ASCII: {ord(char)})")

if __name__ == "__main__":
    read_character_by_character_from_a_file()
