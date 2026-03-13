class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        pq = []

        for time in workerTimes:
            heappush(pq,(time,time,1))
        
        ans = 0

        for _ in range(mountainHeight):
            currentTime, originalTime, iteration = heappop(pq)
            ans = currentTime

            heappush(pq,((currentTime + originalTime *(iteration +1)),originalTime,(iteration+1)))
        return ans
        