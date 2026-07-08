class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num, 0) + 1
        return any(c>1 for c in hashmap.values())