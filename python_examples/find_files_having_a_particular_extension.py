"""Program to find files with a particular extension."""

def find_files_having_a_particular_extension():
    """Find files with a specific extension in the current directory."""
    known_files = ['test.py', 'readme.txt', 'data.csv', 'script.py', 'notes.txt']
    for name in known_files:
        with open(name, 'w') as f:
            f.write('sample content')

    py_files = [f for f in known_files if f.endswith('.py')]

    print(f"Python files found: {py_files}")

    for name in known_files:
        try:
            with open(name) as f:
                pass
        except FileNotFoundError:
            pass

    return py_files

if __name__ == "__main__":
    find_files_having_a_particular_extension()
