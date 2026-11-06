"""Program to remove all duplicate words from a given sentence."""

def remove_all_duplicates_words_from_a_given_sentence():
    """Remove duplicate words from a sentence while preserving order."""
    test_sentences = [
        "hello world hello python world",
        "the quick brown fox jumps over the lazy dog the fox",
        "a a a b b c c c",
    ]

    for sentence in test_sentences:
        words = sentence.split()
        seen = set()
        result = []
        for word in words:
            if word not in seen:
                seen.add(word)
                result.append(word)
        print(f"Original: '{sentence}'")
        print(f"Without duplicates: '{' '.join(result)}'")
        print()

if __name__ == "__main__":
    remove_all_duplicates_words_from_a_given_sentence()
