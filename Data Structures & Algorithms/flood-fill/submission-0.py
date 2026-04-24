class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ogcolor = image[sr][sc]
        def dfs(row, col):
            if row >= len(image) or col >= len(image[0]) or row < 0 or col < 0 or image[row][col] != ogcolor or image[row][col] == color:
                return
            image[row][col] = color
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        dfs(sr, sc)
        return image