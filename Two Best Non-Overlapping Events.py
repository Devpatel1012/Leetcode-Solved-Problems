class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        print(events)
        heap = []
        res1, res2 = 0,0
        for s,e,p in events:
            while heap and heap[0][0]<s:
                res1 = max(res1,heapq.heappop(heap)[1])
            res2 = max(res2,res1+p)
            heapq.heappush(heap,(e,p))
        
        return res2