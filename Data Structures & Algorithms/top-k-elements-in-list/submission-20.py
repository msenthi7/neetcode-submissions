class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Optimal Solution: we can have maximum of size n = len(nums)
        # as freq. So we can then store the num in the index
        # of their freq, in a DS like list called bucket
        hashm=Counter(nums)
        n=len(nums)
        # bucket=[]*(n+1) means its still [] empty
        # bucket=[[]]*(n+1) means it creates [[],[],..]
        # but it will have shared memory, so updating
        # bucket[2].append(5) will store 5 in all 
        # [[5],[5],...]
        # this is because [] is mutable, and doing [0]*n means
        # integer value 0. It is not immutable
        bucket=[]
        for i in range(n+1):
            bucket.append([])
        for num,freq in hashm.items():
            bucket[freq].append(num)
            # multiple distinct numbers can share the exact same
            # frequency, hence we cant use buck[fre]=num
        topk=[]
        for i in range(n,0,-1):
            for num in bucket[i]:
                topk.append(num)
                if len(topk)==k:
                    return topk
                
            
            

        
        