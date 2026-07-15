class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lm=rm=1
        n=len(nums)
        out=[1]*n
        for i in range(n):
            out[i]*=lm
            lm*=nums[i]
        for i in range(n-1,-1,-1):
            out[i]*=rm
            rm*=nums[i]
        return out

        
        