import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<=r:
            thrs=0
            mid=l+(r-l)//2
            for i in piles:
                thrs+=math.ceil(i/mid)
            if thrs<=h:
                r=mid-1
            elif thrs>h:
                l=mid+1
            
        return l



        