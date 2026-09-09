class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if count is not same, its defdinitely not an anagram. So we can filter it out at first layer.
        if len(s)!=len(t):
            return False
        #I can store count of a char in a list. Each character from 0 to 25 will be a to z (case insesnitive). If case sensitive then we can just use 0 to 51
        #One list is enough, since the same positions can be used. 's' can be used to incremenet and 't can be used to decerement. This saves space. O(26), 2 list means O(52)
        #if list has all 0s then return true. Else False
        count=[0]*26
        for j in range(len(s)):
            count[ord(s[j])-ord('a')]+=1
            count[ord(t[j])-ord('a')]-=1
        return all(v==0 for v in count)
        