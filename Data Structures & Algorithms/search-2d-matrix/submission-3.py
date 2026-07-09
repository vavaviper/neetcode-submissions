class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        row = 0
        column = n-1

        while row < m and column >= 0:
            if matrix[row][column] > target:
                column -= 1
            elif matrix[row][column] < target:
                row += 1
            else:
                return True
        return False
        