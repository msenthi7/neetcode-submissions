class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long=0
        inp=set(nums)
        for num in inp:
            if num-1 not in inp:
                l=1
                while num+l in inp:
                    l+=1
                long=max(l,long)
        return long