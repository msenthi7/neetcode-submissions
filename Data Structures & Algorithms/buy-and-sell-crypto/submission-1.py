class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar=99
        maxprofit=0
        for i in range(len(prices)):
            minsofar=min(prices[i],minsofar)
            maxprofit=max(prices[i]-minsofar,maxprofit)
        return maxprofit
    

        