class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brutually, we can use min heap or max heap to 
        # print the top-k frequent elements
        # we store the elements and their count in hashmap.
        # use heap to push the elements based on their count.
        # min heap means we pop elements (min elements gets popped)
        # when len>k, thus leaving top k elements
        # max heap means we just store all elements with -freq
        # ( -ve because by default its min heap)
        # finally we pop until k elements are received
        hashm=Counter(nums)
        out=[]
        max_heap=[]
        for num,freq in hashm.items():
            heapq.heappush(max_heap,(-freq,num))
        while k > 0 and max_heap:
            freq, num = heapq.heappop(max_heap)
            out.append(num)
            k -= 1
        return out
        # This fails, which is why we use While:
        '''
        for freq,num in max_heap:
            if k>0:
                freq,num=heapq.heappop(max_heap)
                out.append(num)
                k-=1
        return out
        ''' 
        # It fails because when we pop, the next element 
        # goes to index 0 in heap. While for loop checks for index 1, 
        # which is the 3rd element.

        # Max heap stores all elements and then pops k
        # O(nlogn) to make heap of all ele; 
        # pop/push takes log time. logn means heapsize is n. 
        # We do k pops so klogn
        # Min heap stores only k elements, 
        # but still has to gothrough all elements
        # O(nlogk)
        # the O(nlogk) comes from performing n insertions 
        # (and popping to cap the size at k)
