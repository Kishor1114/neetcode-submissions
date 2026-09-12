class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums) - 1:
                permutations.append(nums[:])  # Append a copy of the current permutation

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap elements
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack

        permutations = []
        backtrack(0)
        return permutations