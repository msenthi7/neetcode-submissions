class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lm=rm=1
        n=len(nums)
        out=[1]*n
        for i in range(n):
            j=-i-1
            out[i]*=lm
            lm*=nums[i]
            out[j]*=rm
            rm*=nums[j]
        return out
