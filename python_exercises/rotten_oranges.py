"""Rotten Oranges - Exercise.

We have a grid of oranges:
  0 = empty cell
  1 = fresh orange
  2 = rotten orange

Every minute, any fresh orange that is next to a rotten orange becomes rotten.
We want to find the minimum time for all oranges to become rotten.
"""

def rotten_oranges():
    """Find the minimum time to rot all oranges using BFS."""
    # Our grid: 2=rotten, 1=fresh, 0=empty
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]

    # Get the size of the grid
    rows = len(grid)
    cols = len(grid[0])

    # We use a queue (a list) to keep track of rotten oranges to process
    # Each item is (row, column, time_when_it_became_rotten)
    queue = []
    fresh_count = 0  # Count of fresh oranges we haven't rotted yet

    # Step 1: Find all rotten oranges and count fresh ones
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                # This is a rotten orange - add it to our queue
                queue.append((row, col, 0))
            elif grid[row][col] == 1:
                # This is a fresh orange - count it
                fresh_count += 1

    # If there are no fresh oranges, we're done immediately
    if fresh_count == 0:
        print("No fresh oranges. Time = 0")
        return 0

    # The four directions we can spread rot: right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_time = 0  # Track the longest time it takes

    # Step 2: Process each rotten orange and spread rot to neighbors
    while queue:
        # Take the first rotten orange from the queue
        current_row, current_col, current_time = queue.pop(0)

        # Update the maximum time seen so far
        max_time = max(max_time, current_time)

        # Check all four neighboring cells
        for delta_row, delta_col in directions:
            neighbor_row = current_row + delta_row
            neighbor_col = current_col + delta_col

            # Check if the neighbor is within bounds and is a fresh orange
            if (0 <= neighbor_row < rows and
                0 <= neighbor_col < cols and
                grid[neighbor_row][neighbor_col] == 1):

                # The fresh orange becomes rotten!
                grid[neighbor_row][neighbor_col] = 2
                fresh_count -= 1  # One less fresh orange
                queue.append((neighbor_row, neighbor_col, current_time + 1))

    # If there are still fresh oranges left, they can never be rotted
    if fresh_count > 0:
        print("Not all oranges can rot!")
        return -1

    print(f"Minimum time to rot all oranges: {max_time}")
    return max_time

# Run the function when this file is executed
if __name__ == "__main__":
    rotten_oranges()
