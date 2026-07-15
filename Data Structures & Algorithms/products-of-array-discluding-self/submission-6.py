class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lm=rm=1
        n=len(nums)
        out=[]
        for i in range(n):
            out.append(lm)
            lm*=nums[i]
        for i in range(n-1,-1,-1):
            out[i]*=rm
            rm*=nums[i]
        return out

        
        