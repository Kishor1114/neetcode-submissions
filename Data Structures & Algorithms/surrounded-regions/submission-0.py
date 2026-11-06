class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(row, col):
            if (
                row < 0
                or row >= len(board)
                or col < 0
                or col >= len(board[0])
                or board[row][col] != "O"
            ):
                return

            board[row][col] = "E"  # Mark as visited but not surrounded

            # Check adjacent cells
            dfs(row + 1, col)  # Check down
            dfs(row - 1, col)  # Check up
            dfs(row, col + 1)  # Check right
            dfs(row, col - 1)  # Check left

        # Traverse the boundary and mark connected 'O' cells as 'E'
        for row in range(len(board)):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][len(board[0]) - 1] == "O":
                dfs(row, len(board[0]) - 1)

        for col in range(len(board[0])):
            if board[0][col] == "O":
                dfs(0, col)
            if board[len(board) - 1][col] == "O":
                dfs(len(board) - 1, col)

        # Mark internal 'O' cells as 'X' and restore 'E' cells to 'O'
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "E":
                    board[row][col] = "O"