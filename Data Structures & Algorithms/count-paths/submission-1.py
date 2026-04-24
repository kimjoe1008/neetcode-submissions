class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # can only move down and to the right
        # movement restriction prevents loops
        output = 0
        def dfs(r, c):
            nonlocal output
            if r >= m or c >= n or r < 0 or c < 0:
                return
            if r == m - 1 and c == n - 1:
                output += 1
                return
            dfs(r + 1, c)
            dfs(r, c + 1)
        dfs(0, 0)
        return output