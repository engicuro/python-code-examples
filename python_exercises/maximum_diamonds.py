"""Maximum Diamonds - Exercise.

You have several bags of diamonds. Each time you pick a bag,
you collect all its diamonds, but the bag gets half as many
diamonds back (rounded down). You want to maximize your
collection by always picking the bag with the most diamonds.
"""

def maximum_diamonds():
    """Find the maximum number of diamonds that can be collected.

    Strategy: Always pick the bag with the most diamonds.
    After picking, put half the diamonds back (rounded down).
    """
    # Each number represents how many diamonds are in a bag
    bags = [3, 5, 2, 8, 1, 7, 4]
    k = 3  # How many times we get to pick a bag

    # Sort bags from most to least diamonds so the biggest is always first
    sorted_bags = sorted(bags, reverse=True)

    total_diamonds = 0  # This will track our total collection

    for pick in range(k):
        # Step 1: Pick the bag with the most diamonds (first in our sorted list)
        largest = sorted_bags.pop(0)
        total_diamonds += largest
        print(f"Pick {pick + 1}: Took {largest} diamonds (total: {total_diamonds})")

        # Step 2: Put half the diamonds back into the bag (rounded down)
        half = largest // 2
        sorted_bags.append(half)

        # Step 3: Re-sort so the biggest bag is always first again
        sorted_bags.sort(reverse=True)
        print(f"  Bag returned with {half} diamonds. Bags now: {sorted_bags}")

    print(f"\nOriginal bags: {bags}")
    print(f"Number of picks: {k}")
    print(f"Maximum diamonds collected: {total_diamonds}")
    return total_diamonds

# Run the function when this file is executed
if __name__ == "__main__":
    maximum_diamonds()
