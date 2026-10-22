class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        result = []

        # Define the boundaries of the current layer
        top, bottom, left, right = 0, rows - 1, 0, cols - 1

        while top <= bottom and left <= right:
            # Traverse the top row
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Traverse the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse the bottom row
            if top <= bottom:  # Avoid duplicate traversal
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # Traverse the left column
            if left <= right:  # Avoid duplicate traversal
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result