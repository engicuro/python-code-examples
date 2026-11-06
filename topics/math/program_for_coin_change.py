"""Program to solve the coin change problem."""

def program_for_coin_change():
    """Find the minimum number of coins needed to make a given amount."""
    coins = [1, 5, 10, 25]
    amount = 63

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    print(f"Coins: {coins}")
    print(f"Amount: {amount}")
    print(f"Minimum coins needed: {dp[amount]}")
    return dp[amount]

if __name__ == "__main__":
    program_for_coin_change()
