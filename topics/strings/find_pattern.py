"""Find Pattern - Exercise."""

def find_pattern():
    """Find a pattern in a string."""
    text = "The quick brown fox jumps over the lazy dog"
    pattern = "fox"

    # Using find()
    index = text.find(pattern)
    print(f'Text: "{text}"')
    print(f'Pattern: "{pattern}"')
    print(f"Found at index: {index}")

    # Using string find
    matches = []
    start = 0
    while True:
        idx = text.find(pattern, start)
        if idx == -1:
            break
        matches.append(pattern)
        start = idx + 1
    print(f"String matches: {matches}")

if __name__ == "__main__":
    find_pattern()
