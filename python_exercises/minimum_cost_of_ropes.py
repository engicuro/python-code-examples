"""Minimum Cost of Ropes - Exercise.

You have several ropes of different lengths. Connecting
two ropes costs the sum of their lengths. You want to
connect all ropes into one with the minimum total cost.

The trick: always connect the two shortest ropes first.
"""

def minimum_cost_of_ropes():
    """Find the minimum cost to connect all ropes."""
    # Lengths of each rope
    ropes = [4, 3, 2, 6]

    # Sort ropes from shortest to longest
    ropes.sort()
    total_cost = 0  # This will track the total cost

    # Keep connecting ropes until only one is left
    while len(ropes) > 1:
        # Always pick the two shortest ropes (first two in sorted list)
        first = ropes.pop(0)
        second = ropes.pop(0)

        # Cost to connect these two ropes
        cost = first + second
        total_cost += cost

        # Put the new connected rope back and keep the list sorted
        ropes.append(cost)
        ropes.sort()

    print(f"Ropes: [4, 3, 2, 6]")
    print(f"Minimum cost to connect all ropes: {total_cost}")
    return total_cost

# Run the function when this file is executed
if __name__ == "__main__":
    minimum_cost_of_ropes()
