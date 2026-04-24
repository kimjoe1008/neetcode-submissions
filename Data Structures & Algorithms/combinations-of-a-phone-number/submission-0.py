class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        output = []
        def dfs(i, current):
            if i == len(digits):
                output.append("".join(current))
                return
            for char in digitToChar[digits[i]]:
                current.append(char)
                dfs(i + 1, current)
                current.pop()

        dfs(0, [])
        return output