# Last updated: 1/12/2026, 1:42:07 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxP = 0
        
        while r< len(prices):
            if prices[l] < prices[r]:
                profit = prices[r]- prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r+=1
        return maxP