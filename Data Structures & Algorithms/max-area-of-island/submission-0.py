class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ma = 0
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in seen or grid[row][col] == 0:
                return 0
            seen.add((row, col))
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in seen and grid[row][col] == 1:
                    ma = max(ma, dfs(row, col))
        return ma
            