class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_buy=prices[0]
        for s in prices:
            if s<min_buy:
                min_buy=s
            profit=max(profit,s-min_buy)
        return profit