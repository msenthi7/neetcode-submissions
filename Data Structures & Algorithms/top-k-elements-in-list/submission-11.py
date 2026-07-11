class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashm=Counter(nums)
        n=len(nums)
        minheap=[]
        out=[]
        for num,freq in hashm.items():
            heapq.heappush(minheap,(freq,num))
            if len(minheap)>k:
                heapq.heappop(minheap)
        for freq,num in minheap:
            out.append(num)
        return out
            
        