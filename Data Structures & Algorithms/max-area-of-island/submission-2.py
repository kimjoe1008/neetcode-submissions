class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        output = 0
        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    output = max(output, dfs(row, col))
        return output