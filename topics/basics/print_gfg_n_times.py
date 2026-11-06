"""Print GFG n times - Exercise."""

def print_gfg_n_times():
    """Print 'GFG' n times."""
    n = 5

    # Using a loop
    for i in range(n):
        print("GFG", end=" ")
    print()

    # Using while loop
    count = 0
    while count < n:
        print("GFG", end=" ")
        count += 1
    print()

if __name__ == "__main__":
    print_gfg_n_times()
