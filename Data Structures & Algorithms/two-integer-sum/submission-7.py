class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force is to check every combination
        '''
        i=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        '''
        # Optimised solution is to not check the same number again. So we need to keep track of same numbers. 
        # We can use hashmap instead of list to lookup at O(1). Basically we lookup for difference of 1st element and the target, if yes give output.
        # If not, then store that element in the hashmap for future lookup. 
        hashm={}
        for i , num in enumerate(nums):
            diff=target-num
            if diff in hashm:
                return [hashm[diff],i]
            else:
                hashm[num]=i

