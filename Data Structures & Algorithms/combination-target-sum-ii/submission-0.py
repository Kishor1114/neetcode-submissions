class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, combination):
            if target == 0:
                result.append(
                    combination[:]
                )  # Append a copy of the current combination
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates at the same depth level

                if candidates[i] > target:
                    continue  # Skip if the candidate is too large

                combination.append(candidates[i])
                backtrack(i + 1, target - candidates[i], combination)
                combination.pop()  # Backtrack

        candidates.sort()  # Sort the input to handle duplicates
        result = []
        backtrack(0, target, [])
        return result