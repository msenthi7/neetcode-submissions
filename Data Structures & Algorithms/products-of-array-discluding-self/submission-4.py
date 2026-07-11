class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        out=[]
        for i in range(n):
            p=1
            for j in range(n):
                if j!=i:
                    p*=nums[j]
            out.append(p)
        return out
        