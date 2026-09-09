class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            subsets.append(subset[:])  # Append a copy of the current subset

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()  # Backtrack

        subsets = []
        backtrack(0, [])
        return subsets