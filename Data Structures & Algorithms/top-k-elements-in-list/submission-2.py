from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashm=Counter(nums)
        out=[]
        min_heap=[]
        for num,freq in hashm.items():
            heapq.heappush(min_heap,(freq,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        for freq,num in min_heap:
            out.append(num)
        return out
        
        