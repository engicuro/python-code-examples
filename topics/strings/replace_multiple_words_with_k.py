"""Program to replace multiple words in a string with a given word K."""

def replace_multiple_words_with_k():
    """Replace multiple specified words in a string with a replacement word."""
    text = "The quick brown fox jumps over the lazy dog"
    words_to_replace = ["quick", "brown", "lazy"]
    replacement = "smart"

    for word in words_to_replace:
        text = text.replace(word, replacement)

    print(f"Original: 'The quick brown fox jumps over the lazy dog'")
    print(f"After replacement: '{text}'")
    return text

if __name__ == "__main__":
    replace_multiple_words_with_k()
