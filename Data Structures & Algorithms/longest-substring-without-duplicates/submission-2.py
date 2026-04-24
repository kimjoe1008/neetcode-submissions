class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2 pointer
        chars = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in chars and l < r:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            longest = max(longest, r - l + 1)
        return longest