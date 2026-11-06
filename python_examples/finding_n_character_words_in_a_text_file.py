"""Program to find words of n characters in a text file."""

def finding_n_character_words_in_a_text_file():
    """Find all words of a specific length in a text file."""
    n = 5
    with open("sample_words.txt", "w") as f:
        f.write("hello world python programming is fun and exciting\n")

    result = []
    with open("sample_words.txt", "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) == n:
                    result.append(word)

    print(f"Words with {n} characters: {result}")
    return result

if __name__ == "__main__":
    finding_n_character_words_in_a_text_file()
