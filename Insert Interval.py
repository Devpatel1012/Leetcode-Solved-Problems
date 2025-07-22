class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i = 0 
        n = len(intervals)
        while i<n and intervals[i][1]<newInterval[0]:
            result.append(intervals[i])
            i=i+1
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i = i+1
        result.append(newInterval)

        while i<n:
            result.append(intervals[i])
            i = i+1
        return result


