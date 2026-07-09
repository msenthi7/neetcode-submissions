class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sort_list_fr(st):
            return "".join(sorted(list(st)))
        new_map = defaultdict()
        for  i in strs:
            temp = sort_list_fr(i) 
            if temp not in new_map:
                new_map[temp] = [i]
            else:
                new_map[temp].append(i)
        
        return list(new_map.values())
                

            