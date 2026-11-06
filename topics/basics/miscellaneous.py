"""Miscellaneous - Exercise (Quiz).

This file shows several useful Python features.
Each section explains what's happening step by step.
"""

def miscellaneous():
    """Quiz: Various Python miscellaneous topics."""

    # --- List comprehension ---
    # A quick way to build a list using a short formula.
    # This creates a list of squares: [1, 4, 9, 16, 25]
    squares = [x ** 2 for x in range(1, 6)]
    print(f"Squares: {squares}")

    # --- Dictionary comprehension ---
    # A quick way to build a dictionary.
    # This creates a dictionary of word lengths.
    word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
    print(f"Word lengths: {word_lengths}")

    # --- Lambda functions ---
    # A lambda is a small one-line function.
    # "lambda x: x * 2" means: take x, return x times 2.
    double = lambda x: x * 2
    print(f"Double of 5: {double(5)}")

    # --- Map and filter ---
    # map(function, list) applies a function to every item in a list.
    # filter(function, list) keeps only items where the function returns True.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Filter: keep only even numbers (numbers divisible by 2)
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Evens: {evens}")

    # Map: double every number
    doubled = list(map(lambda x: x * 2, numbers))
    print(f"Doubled: {doubled}")

    # --- Zip ---
    # zip() combines two lists side by side into pairs.
    names = ["Alice", "Bob", "Charlie"]
    scores = [90, 85, 92]
    paired = list(zip(names, scores))
    print(f"Paired: {paired}")

    # --- Unpacking ---
    # You can unpack a list into separate variables in one line.
    # This is the same as: a = 1, b = 2, c = 3
    a, b, c = [1, 2, 3]
    print(f"Unpacked: a={a}, b={b}, c={c}")

if __name__ == "__main__":
    miscellaneous()
