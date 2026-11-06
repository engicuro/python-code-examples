"""While Loop - Exercise (Quiz)."""

def while_loop_quiz():
    """Quiz: Demonstrate while loop usage."""
    # Countdown
    n = 5
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")

    # Sum of numbers until 0
    total = 0
    while True:
        num = int(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        total += num
    print(f"Total sum: {total}")

if __name__ == "__main__":
    while_loop_quiz()
