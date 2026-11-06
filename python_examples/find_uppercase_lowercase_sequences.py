"""Program to find uppercase-lowercase sequences in a string."""

def find_uppercase_lowercase_sequences():
    """Find sequences of uppercase followed by lowercase letters."""
    test_strings = ["HelloWorld", "ABCdefGHI", "PythonIsGreat", "UPPERlower"]

    for s in test_strings:
        matches = []
        i = 0
        while i < len(s):
            if s[i].isupper():
                start = i
                while i < len(s) and s[i].isupper():
                    i += 1
                while i < len(s) and s[i].islower():
                    i += 1
                matches.append(s[start:i])
            else:
                i += 1
        print(f"String: '{s}' -> Sequences: {matches}")

if __name__ == "__main__":
    find_uppercase_lowercase_sequences()
