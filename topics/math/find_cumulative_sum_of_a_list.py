"""Program to find the cumulative sum of a list."""

def find_cumulative_sum_of_a_list():
    """Calculate the cumulative sum of a list."""
    arr = [1, 2, 3, 4, 5]

    cumulative = []
    running_sum = 0
    for num in arr:
        running_sum += num
        cumulative.append(running_sum)

    print(f"Original list: {arr}")
    print(f"Cumulative sum: {cumulative}")
    return cumulative

if __name__ == "__main__":
    find_cumulative_sum_of_a_list()
