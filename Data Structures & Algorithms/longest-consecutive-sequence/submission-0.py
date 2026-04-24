class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 0
        numset = set(nums)
        for num in numset:
            if num - 1 not in numset:
                streak = 1
                while num + streak in numset:
                    streak += 1
                longest = max(longest, streak)
        return longest