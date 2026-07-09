class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = math.prod(nums)
        a = []
        c = nums
        for i in range(len(nums)):
            nums = c
            temp = []
            if i==0:
                temp = (nums[i+1:])
            elif i==len(nums)-1:
                temp = nums[:i]
            else:
                temp = nums[:i]
                temp.extend(nums[i+1:])
            a.append(math.prod(temp))

        return a
         
        