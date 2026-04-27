class Solution:
    def longestPalindrome(self, s: str) -> str:
        outputi, outputlen = 0, 0
        for center in range(len(s)):
            l, r = center, center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if outputlen < r - l + 1:
                    outputi = l
                    outputlen = r - l + 1
                l -= 1
                r += 1

            l, r = center, center + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if outputlen < r - l + 1:
                    outputi = l
                    outputlen = r - l + 1
                l -= 1
                r += 1
        return s[outputi:outputi + outputlen]