class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = 1
        check = 0
        for i in range(1,len(intervals)):
            if i == 0 :
                continue
            prev = [intervals[check][0],intervals[check][1]]
            if intervals[i][0] >=prev[0] and intervals[i][1] > prev[1]:
                ans+=1
                check = i
        return ans  



        