from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0
        l=0
        freq=defaultdict(int)
        maxfreq=0
        for r in range(len(s)):
            freq[s[r]]+=1
            maxfreq=max(maxfreq,freq[s[r]])
            while (r-l+1)-maxfreq>k:
                freq[s[l]]-=1
                l+=1
            longest=max(longest,r-l+1)
        return longest


        
        