class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashm={}
        for i in range(len(nums)):
            if nums[i] in hashm:
                hashm[nums[i]]+=1
            else:
                hashm[nums[i]]=1
        sorted_ele = sorted(hashm.keys(),key = lambda x: hashm[x], reverse=True)
        return sorted_ele[:k]
        
        