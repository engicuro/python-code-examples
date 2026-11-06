"""Program to count occurrences of a key-value pair in a text file."""

def count_the_number_of_occurrences_of_a_key_value_pair_in_a_text_file():
    """Count how many times a specific key-value pair appears in a text file."""
    with open("data.txt", "w") as f:
        f.write("name=Alice\n")
        f.write("age=25\n")
        f.write("name=Bob\n")
        f.write("name=Alice\n")
        f.write("city=NYC\n")
        f.write("name=Alice\n")

    target_key = "name"
    target_value = "Alice"
    count = 0

    with open("data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if '=' in line:
                key, value = line.split('=', 1)
                if key == target_key and value == target_value:
                    count += 1

    print(f"Key-value pair '{target_key}={target_value}' appears {count} times.")
    return count

if __name__ == "__main__":
    count_the_number_of_occurrences_of_a_key_value_pair_in_a_text_file()
