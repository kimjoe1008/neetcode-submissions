class Solution:
    def findMin(self, nums: List[int]) -> int:
        output = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # if l < r then the current window is sorted
            if nums[l] < nums[r]:
                return min(nums[l], output)
            m = (l + r) // 2
            output = min(output, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return output