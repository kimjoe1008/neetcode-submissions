class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        minBuy = prices[0]

        for sell in prices:
            mp = max(mp, sell - minBuy)
            minBuy = min(minBuy, sell)
        return mp