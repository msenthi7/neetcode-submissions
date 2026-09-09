class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # Size 123 covers all ASCII codes from 0 to 122 ('z')
        count = [0] * 123
        
        for j in range(len(s)):
            # Use the raw ASCII code directly as the index
            count[ord(s[j])] += 1
            count[ord(t[j])] -= 1
            
        return all(v == 0 for v in count)
