class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[0])
                or grid[row][col] == 0
            ):
                return 0

            grid[row][col] = 0  # Mark as visited
            area = 1

            area += dfs(row + 1, col)  # Check down
            area += dfs(row - 1, col)  # Check up
            area += dfs(row, col + 1)  # Check right
            area += dfs(row, col - 1)  # Check left

            return area

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area