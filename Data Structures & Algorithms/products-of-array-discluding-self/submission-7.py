class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        larr=[1]*n
        rarr=[1]*n
        lm=1
        rm=1
        for i in range(n):
            larr[i]=lm
            lm*=nums[i]
        for i in range(n-1,-1,-1):
            rarr[i]=rm
            rm*=nums[i]
        return [l*r for l,r in zip(larr,rarr)]