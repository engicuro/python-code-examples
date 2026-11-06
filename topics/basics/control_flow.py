"""Control Flow - Exercise (Quiz)."""

def control_flow():
    """Quiz: Demonstrate control flow statements."""
    # if-elif-else
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Score: {score}, Grade: {grade}")

    # for loop with else
    for i in range(5):
        if i == 3:
            break
        print(i, end=" ")
    else:
        print("\nLoop completed normally")
    print()

    # while loop with else
    count = 0
    while count < 3:
        print(count, end=" ")
        count += 1
    else:
        print("\nWhile loop completed normally")

if __name__ == "__main__":
    control_flow()
