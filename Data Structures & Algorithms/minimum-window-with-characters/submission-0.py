from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        res,reslen="",float('inf')
        countt, windowl=Counter(t),defaultdict(int)
        have,need=0,len(countt)
        if not s or not t or len(t)>len(s):
            return ""
        for r in range(len(s)):
            windowl[s[r]]+=1
            if windowl[s[r]]==countt[s[r]]:
                have+=1
            while have==need:
                if r-l+1<reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                windowl[s[l]]-=1
                if windowl[s[l]]<countt[s[l]]:
                    have-=1
                l+=1
        return res

                    
            

       
        