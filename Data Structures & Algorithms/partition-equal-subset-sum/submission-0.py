class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # If the total sum is odd, it's impossible to partition into two equal subsets.
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2

        # Initialize a dynamic programming array dp with all values set to False.
        dp = [False] * (target_sum + 1)

        # It's always possible to achieve a sum of 0 using an empty subset.
        dp[0] = True

        for num in nums:
            for i in range(target_sum, num - 1, -1):
                # If it's possible to achieve a sum of 'i - num' using a subset,
                # then it's also possible to achieve a sum of 'i' using a subset.
                dp[i] = dp[i] or dp[i - num]

        return dp[target_sum]