class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start in top right and move up if lower move right if greater
        ROW, COL = len(matrix), len(matrix[0])
        r, c = 0, COL - 1

        while r < ROW and c >= 0:
            if matrix[r][c] == target:
                return True
            if target > matrix[r][c]:
                r += 1
            else:
                c -= 1
        return False