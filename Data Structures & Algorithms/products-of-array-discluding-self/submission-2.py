class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tp=1
        n=len(nums)
        out=[0]*n
        nonzero_product=1
        zc=nums.count(0)
        if zc>=2:
            return out  
        for x in nums:
            if x != 0:
                nonzero_product *= x
        if zc==1:
            for i in range(n):
                if nums[i]==0:
                    out[i]=nonzero_product
                else:
                    out[i]=0
            return out
        for i in range(n):
            out[i]=nonzero_product//nums[i]
        return out

        