class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if count is not same, its defdinitely not an anagram. So we can filter it out at first layer.
        if len(s)!=len(t):
            return False
        return Counter(s)==Counter(t)
        