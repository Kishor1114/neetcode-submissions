class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize a dynamic programming array dp with all values set to 1.
        dp = [1] * len(nums)

        # Iterate through the array to find the longest increasing subsequence.
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # Return the maximum value in dp, which represents the length of the longest increasing subsequence.
        return max(dp)