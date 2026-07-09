from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k==0:
            return []
        a = Counter(nums)
        sorted_dict = dict(sorted(a.items(), reverse =True,key=itemgetter(1)))
        # sorted_dict = dict(a)
        final = []
        for i in sorted_dict:
            final.append(i)
            k-=1
            if k<1:
                break
        return final
