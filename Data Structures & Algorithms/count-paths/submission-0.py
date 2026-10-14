class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D dp grid of size m x n with all values set to 1.
        dp = [[1] * n for _ in range(m)]

        # Fill in the dp grid using dynamic programming.
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The value in dp[m-1][n-1] represents the number of unique paths.
        return dp[m - 1][n - 1]