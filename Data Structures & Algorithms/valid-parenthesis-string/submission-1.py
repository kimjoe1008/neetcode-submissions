class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        stars = []
        for i, char in enumerate(s):
            if char == "(":
                left.append(i)
            elif char == "*":
                stars.append(i)
            else:
                if not left and not stars:
                    return False
                if left:
                    left.pop()
                else:
                    stars.pop()
        while left and stars:
            if left.pop() > stars.pop():
                return False
        return not left