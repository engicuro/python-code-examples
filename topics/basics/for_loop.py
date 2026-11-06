"""For Loop - Exercise (Quiz)."""

def for_loop():
    """Quiz: Demonstrate for loop usage."""
    # Iterate over a range
    for i in range(1, 6):
        print(f"Number: {i}")

    # Iterate over a list
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"Fruit: {fruit}")

    # Iterate over a dictionary
    student = {"name": "Alice", "age": 20, "grade": "A"}
    for key, value in student.items():
        print(f"{key}: {value}")

    # Nested loop
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"({i}, {j})", end=" ")
        print()

if __name__ == "__main__":
    for_loop()
