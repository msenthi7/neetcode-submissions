class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashm=Counter(nums)
        bucket=[]
        out=[]
        n=len(nums)
        for _ in range(n+1):
            bucket.append([])
        for num,freq in hashm.items():
            bucket[freq].append(num)
        for i in range(n,0,-1):
            for num in bucket[i]:
                if len(out)<k:
                    out.append(num)
        return out
                
                
        