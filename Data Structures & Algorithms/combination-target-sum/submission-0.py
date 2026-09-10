class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, combination):
            if target == 0:
                result.append(
                    combination[:]
                )  # Append a copy of the current combination
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue  # Skip if the candidate is too large

                combination.append(candidates[i])
                backtrack(i, target - candidates[i], combination)
                combination.pop()  # Backtrack

        result = []
        backtrack(0, target, [])
        return result