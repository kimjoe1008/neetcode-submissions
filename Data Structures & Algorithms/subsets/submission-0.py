class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        current = []
        n = len(nums)
        def dfs(i):
            if i >= n:
                output.append(current.copy())
                return
            current.append(nums[i])
            dfs(i + 1)
            current.pop()
            dfs(i + 1)
        dfs(0)
        return output