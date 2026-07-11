class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        out=[1]*n
        for i in range(n):
            p=1
            for j in range(n):
                if j!=i:
                    p*=nums[j]
            out[i]=p
        return out
        