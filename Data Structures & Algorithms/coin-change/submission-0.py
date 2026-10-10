class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the DP array with a maximum value to represent impossible cases.
        dp = [float("inf")] * (amount + 1)

        # Base case: It takes 0 coins to make up the amount of 0.
        dp[0] = 0

        # Iterate through the DP array and update the minimum number of coins needed.
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still float('inf'), it means it's impossible to make up the amount.
        # Otherwise, dp[amount] contains the minimum number of coins needed.
        return dp[amount] if dp[amount] != float("inf") else -1