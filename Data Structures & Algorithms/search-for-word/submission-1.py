class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs keeping track of index of letter were looking for and row and column
        ROW, COL = len(board), len(board[0])
        visited = set()
        def dfs(r, c, i):
            # if the letter doesnt match then dont continue
            # if out of bounds
            # if already in path
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r, c) in visited or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            visited.add((r, c))
            temp = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1))
            visited.remove((r, c))
            return temp
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False