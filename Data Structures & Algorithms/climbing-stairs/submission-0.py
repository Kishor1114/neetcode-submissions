class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev1 = 1  # Number of ways to reach the 1st stair
        prev2 = 2  # Number of ways to reach the 2nd stair

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current  # Update for the next iteration

        return prev2  # Number of ways to reach the n-th stair
        