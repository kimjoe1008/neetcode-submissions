class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()

        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or (x, y) in visited or grid[x][y] == "0":
                return
            
            visited.add((x, y))

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1" and (x, y) not in visited:
                    dfs(x, y)
                    count += 1
        return count