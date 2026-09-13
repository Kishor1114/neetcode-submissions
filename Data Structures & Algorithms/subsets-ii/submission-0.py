class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            subsets.append(subset[:])  # Append a copy of the current subset

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue  # Skip duplicates at the same depth level
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()  # Backtrack

        nums.sort()  # Sort the input to handle duplicates
        subsets = []
        backtrack(0, [])
        return subsets