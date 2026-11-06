"""Program to extract the maximum numeric value from a string."""

def extract_maximum_numeric_value_from_a_string():
    """Find the maximum numeric value in a string."""
    test_strings = [
        "The prices are 100, 250, and 50 dollars",
        "No numbers here!",
        "Temperatures: -5, 23, 18, -2, 30",
    ]

    for s in test_strings:
        numbers = []
        i = 0
        while i < len(s):
            if s[i].isdigit() or (s[i] == '-' and i + 1 < len(s) and s[i + 1].isdigit()):
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                numbers.append(int(s[i:j]))
                i = j
            else:
                i += 1
        if numbers:
            max_num = max(numbers)
            print(f'String: "{s}" -> Max number: {max_num}')
        else:
            print(f'String: "{s}" -> No numbers found')

if __name__ == "__main__":
    extract_maximum_numeric_value_from_a_string()
