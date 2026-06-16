class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        inp=set(nums)
        for num in inp:
            if num-1 not in inp:
                length=1
                while num + length in inp:
                    length+=1
                longest=max(longest,length)
        return longest
            
            
        
        