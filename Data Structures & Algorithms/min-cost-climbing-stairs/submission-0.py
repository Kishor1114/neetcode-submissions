class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 1:
            return 0  # No cost if there are 0 or 1 stairs

        dp = [0] * n  # Initialize a list to store minimum costs

        # Base cases
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[n - 1], dp[n - 2])