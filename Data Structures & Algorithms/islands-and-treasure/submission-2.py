from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return

        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[row][col] + 1
                    queue.append((nr, nc))