class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        n=len(strs)
        visited=[False]*n
        for i in range(n):
            if visited[i]:
                continue
            group=[strs[i]]
            visited[i]=True
            for j in range(i+1,n):
                if visited[j]:
                    continue
                if sorted(strs[i])==sorted(strs[j]):
                    group.append(strs[j])
                    visited[j]=True
            result.append(group)
        return result


                    
            
        