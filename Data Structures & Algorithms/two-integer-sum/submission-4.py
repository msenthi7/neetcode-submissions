class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in (range(len(nums)-1)):
            targets = target - nums[i]
            if targets in nums[i+1:]:
                return [i, nums.index(targets, i+1)]
        