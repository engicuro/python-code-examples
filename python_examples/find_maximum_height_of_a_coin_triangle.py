"""Program to find the maximum height of a coin triangle."""

def find_maximum_height_of_a_coin_triangle():
    """Find the maximum height of a triangle that can be formed with n coins."""
    n = 10

    height = 0
    while (height + 1) * (height + 2) // 2 <= n:
        height += 1

    print(f"Number of coins: {n}")
    print(f"Maximum triangle height: {height}")
    print(f"Coins used: {height * (height + 1) // 2}")
    return height

if __name__ == "__main__":
    find_maximum_height_of_a_coin_triangle()
