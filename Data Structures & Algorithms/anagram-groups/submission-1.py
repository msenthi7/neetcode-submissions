from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_m=defaultdict(list)
        for s in strs:
            key=tuple(sorted(s))
            anag_m[key].append(s)
        return list(anag_m.values())

                    
            
        