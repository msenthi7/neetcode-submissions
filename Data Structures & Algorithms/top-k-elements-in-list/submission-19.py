from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashm=Counter(nums)
        n=len(nums)
        bucket=[]
        for i in range(n+1):
            bucket.append([])
        for num,freq in hashm.items():
            bucket[freq].append(num)
        topk=[]
        for i in range(n,0,-1):
            for num in bucket[i]:
                topk.append(num)
                if len(topk)==k:
                    return topk
        
        
        