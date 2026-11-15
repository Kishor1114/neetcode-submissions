from collections import defaultdict
from typing import List


class CountSquares:
    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0

        for y2 in self.points[x]:
            if y2 != y:
                side_length = abs(y2 - y)

                for x2 in (x + side_length, x - side_length):
                    if x2 in self.points and y in self.points[x2]:
                        count += (
                            self.points[x2][y]
                            * self.points[x2][y2]
                            * self.points[x][y2]
                        )

        return count