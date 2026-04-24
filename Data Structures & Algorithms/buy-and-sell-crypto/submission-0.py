class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                mp = max(mp, prices[r] - prices[l])
        return mp