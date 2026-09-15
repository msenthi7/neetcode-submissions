class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force is to check every combination
        i=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

